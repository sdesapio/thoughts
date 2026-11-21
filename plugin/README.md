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

In Claude Code:

```
/plugin install thoughts --marketplace sdesapio/thoughts
```

## Use

- **"Thoughts?"** Ask for an assessment of an idea, plan, or argument. Claude
  examines it with the skill's Method in the current conversation.
- **`/thoughts:thoughts`** invokes the skill directly.
- **"Thoughts? Full council"** or **"Run a council review"** opts into council
  review: three independent subagents form positions, cross-review them, and
  verify the final answer, which ends with a short receipt. Council runs only
  when you ask for it, and it uses more tokens than a normal answer.

Opinion requests and challenges to Claude's reasoning also use the Method.
Quoting "Thoughts?" or discussing the skill does not start a council.

## What this plugin contains and runs

- **`skills/thoughts/SKILL.md`**: the instructions. Plain Markdown, no code.
- **`hooks/hooks.json` and `scripts/thoughts-trigger.sh`**: a
  `UserPromptSubmit` hook. Each time you send a message, Claude Code runs the
  script, which checks whether the message contains "Thoughts?". If it does,
  the script prints a one-line reminder to load the skill, which Claude Code
  adds to Claude's context for that turn. Otherwise it prints nothing. Without
  this, Claude decides from the skill's description whether to load it, and can
  miss a "Thoughts?" at the end of a long message.

The script reads the message from standard input and writes to standard output.
It does not write files, use the network, or store or send anything. The plugin
has no MCP server, collects no data, and contacts no outside service.

## License

[MIT](LICENSE).
