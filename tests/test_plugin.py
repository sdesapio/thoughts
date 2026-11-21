"""Check the Claude Code plugin folder against the root sources and directory rules."""

import json
from pathlib import Path
import subprocess
import unittest


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugin"


class PluginTests(unittest.TestCase):
    def test_copies_match_root_sources(self):
        for source, copy in (("SKILL.md", "skills/thoughts/SKILL.md"), ("LICENSE", "LICENSE")):
            self.assertEqual((ROOT / source).read_bytes(), (PLUGIN / copy).read_bytes(),
                             f"{copy} is stale; run scripts/sync_plugin.py")

    def test_manifests(self):
        manifest = json.loads((PLUGIN / ".claude-plugin/plugin.json").read_text())
        self.assertEqual(manifest["name"], "thoughts")
        for key in ("version", "description", "author", "license"):
            self.assertTrue(manifest[key])
        marketplace = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
        self.assertEqual([(p["name"], p["source"]) for p in marketplace["plugins"]],
                         [("thoughts", "./plugin")])
        self.assertFalse((PLUGIN / "hooks").exists())
        self.assertFalse((PLUGIN / "scripts").exists())
        self.assertNotIn("network", manifest)

    def test_directory_file_rules(self):
        files = [path for path in PLUGIN.rglob("*") if not path.is_dir()]
        self.assertLessEqual(len(files), 512)
        for path in PLUGIN.rglob("*"):
            self.assertFalse(path.is_symlink(), path)
            self.assertNotIn(path.name, {".DS_Store", "Thumbs.db", "desktop.ini", "__MACOSX"})
        for path in files:
            self.assertLess(path.stat().st_size, 256 * 1024, path)
        self.assertGreaterEqual(len((PLUGIN / "README.md").read_text().split()), 40)


if __name__ == "__main__":
    unittest.main()
