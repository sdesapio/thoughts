# Thoughts

Thoughts is a skill that pushes Claude toward the truth: say what the evidence
supports, hold a well-supported position under pushback, and flag claims it
can't back up. It rests on the three laws of thought: identity,
noncontradiction, and excluded middle.

In tests, Thoughts improved on a one-line prompt for all four models tested: by
a wide margin on Gemini and Sonnet, and by smaller margins on Opus 4.6 and
GPT-5.6 Sol. The story behind it is in
[Is your AI lying to you?](https://scottdesapio.com/thoughts), and the full
results are in
[tests/README.md](https://github.com/sdesapio/thoughts/blob/master/tests/README.md).
Source and installs for other tools are at
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
plugin has no hooks, scripts, or MCP server.

## Privacy

Thoughts collects no data. The plugin is a set of written instructions for
Claude and contains no code, so it cannot read, store, or send anything on its
own. It contacts no outside service, and its author receives no information
about you, your conversations, or your use of it.

When you use Thoughts, your conversation is handled by Claude under Anthropic's
own terms and privacy policy, as it is without the plugin. If Claude searches
the web while checking a claim, it does so with its own tools, not the
plugin's.

## License

[MIT](LICENSE).
