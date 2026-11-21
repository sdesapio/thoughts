# Thoughts

Thoughts is a skill that pushes Claude toward the truth: say what the evidence
supports, hold a well-supported position under pushback, and flag claims it
can't back up. It rests on the three laws of thought: identity,
noncontradiction, and excluded middle.

The story behind it and the published test results, failures included, are in
[Is your AI lying to you?](https://scottdesapio.com/thoughts). Source, tests,
and installs for other tools are at
[github.com/sdesapio/thoughts](https://github.com/sdesapio/thoughts).

## Install

In the Claude apps (web, desktop, and mobile) and Cowork, add Thoughts from the
plugin directory. Then say "Thoughts?" or ask Claude to use the Thoughts skill.

In Claude Code:

```
/plugin install thoughts --marketplace sdesapio/thoughts
```

## Use

- **"Thoughts?"** Ask for an assessment of an idea, plan, or argument. Claude
  examines it with the skill's Method in the current conversation.
- **`/thoughts:thoughts`** invokes the skill directly in Claude Code.
- **"Thoughts? Full council"** or **"Run a council review"** opts into council
  review: three independent subagents form positions, cross-review them, and
  verify the final answer, which ends with a short receipt. Council runs only
  when you ask for it, and it uses more tokens than a normal answer.

Opinion requests and challenges to Claude's reasoning also use the Method.
Quoting "Thoughts?" or discussing the skill does not start a council.

Claude decides from the skill's description whether to load it, and it can
miss a "Thoughts?" at the end of a long message. Use `/thoughts:thoughts` when
it matters, or add this line to `~/.claude/CLAUDE.md`:

```
When I say "Thoughts?", ask for your opinion, or challenge your reasoning, load the thoughts skill before answering.
```

## What this plugin contains

One skill, `skills/thoughts/SKILL.md`: plain Markdown instructions, no code. The
plugin has no hooks, scripts, or MCP server. It collects no data and contacts no
outside service.

## License

[MIT](LICENSE).
