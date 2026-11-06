"""No-network behavior tests for the portable entry point."""
import json, os, pathlib, subprocess, tempfile, unittest
ROOT=pathlib.Path(__file__).resolve().parent
FAKE=r"""#!/usr/bin/env python3
import json,sys,os
p=sys.argv[-1]
if 'Context audit:' in p: text=json.dumps(dict(catalog_names=[],loaded_skill_contents=[],other_user_rules=[],thoughts_visible=False))
elif 'You are a blind grader' in p:
 text='invalid' if os.getenv('FAIL_GRADES') else json.dumps(dict(half_A='PASS',half_B='PASS',same_standard=True,unit_grade='PASS',reason='Fixture'))
else: text='A fixture answer.'
print(json.dumps(dict(type='user',message=dict(content=[dict(type='text',text=p)]))))
print(json.dumps(dict(type='result',result=text,session_id='fixture',usage=dict(inputTokens=100,cacheReadTokens=0,cacheWriteTokens=0,outputTokens=10))))
"""
class RerunBehavior(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup); self.base=pathlib.Path(self.tmp.name)
  self.fake=self.base/'fake-agent'; self.fake.write_text(FAKE); self.fake.chmod(0o755)
 def run_cli(self,*extra,env=None):
  base=[str(ROOT/'rerun.sh'),'--suite','pilot','--model','fixture-model','--grader','fixture-grader','--items','24','--runs','1','--out',str(self.base/'out'),'--agent-bin',str(self.fake)]
  e=os.environ.copy()
  for name in ['GRADER2','FAIL_GRADES','INPUT_OVERHEAD_RESERVE']: e.pop(name,None)
  if env: e.update(env)
  return subprocess.run(base+list(extra),capture_output=True,text=True,env=e)
 def records(self,name): return [json.loads(x) for x in (self.base/'out'/name).read_text().splitlines()]
 def test_one_pair_three_conditions_one_grader(self):
  r=self.run_cli(); self.assertEqual(r.returncode,0,r.stderr)
  ans=self.records('answers.jsonl'); self.assertEqual(len(ans),6)
  self.assertEqual({x['item'] for x in ans},{'24'}); self.assertEqual({x['cond'] for x in ans},{'N','S','T'})
  self.assertEqual({x['run'] for x in ans},{1}); self.assertEqual(len(self.records('grades-1.jsonl')),3)
  self.assertFalse((self.base/'out/grades-2.jsonl').exists()); self.assertEqual(len(self.records('calls.jsonl')),10)
 def test_optional_second_grader(self):
  r=self.run_cli('--grader2','fixture-second'); self.assertEqual(r.returncode,0,r.stderr)
  self.assertEqual(len(self.records('grades-2.jsonl')),3); self.assertEqual(len(self.records('calls.jsonl')),13)
 def test_pre_call_stop(self):
  r=self.run_cli('--max-input-tokens','1'); self.assertNotEqual(r.returncode,0)
  self.assertFalse((self.base/'out/calls.jsonl').exists()); self.assertEqual(len(self.records('budget-stops.jsonl')),1)
 def test_dry_run_never_invokes_executable(self):
  self.fake.unlink(); r=self.run_cli('--dry-run'); self.assertEqual(r.returncode,0,r.stderr)
  plan=json.loads(r.stdout); self.assertEqual(plan['model_calls'],0); self.assertEqual(len(plan['planned_calls']),10)
  self.assertFalse((self.base/'out').exists())
 def test_completed_grades_are_not_repeated(self):
  r=self.run_cli(); self.assertEqual(r.returncode,0,r.stderr)
  r=self.run_cli('--grade-only','--run-cwd',str(self.base/'fresh-grade-cwd')); self.assertEqual(r.returncode,0,r.stderr)
  self.assertEqual(len(self.records('calls.jsonl')),10); self.assertEqual(len(self.records('grades-1.jsonl')),3)
 def test_invalid_grade_is_not_suppressed(self):
  r=self.run_cli(env={'FAIL_GRADES':'1'}); self.assertNotEqual(r.returncode,0)
  self.assertFalse((self.base/'out/grades-1.jsonl').exists()); self.assertEqual(len(self.records('calls.jsonl')),8)
if __name__=='__main__': unittest.main()
