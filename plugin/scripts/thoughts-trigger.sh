#!/bin/sh
# UserPromptSubmit hook for the Thoughts plugin.
#
# Claude Code passes the submitted prompt as JSON on standard input. If that
# input contains "Thoughts?" (any capitalization), print a one-line reminder
# that Claude Code adds to Claude's context for this turn. Otherwise print
# nothing. This script reads standard input and writes standard output only:
# no files, no network, no other programs besides grep.

if grep -qiF 'thoughts?' 2>/dev/null; then
  printf '%s\n' 'The user'"'"'s message contains "Thoughts?". If they are asking for your assessment, load the thoughts skill before you answer and follow its Method. If they are only quoting or discussing the phrase, answer normally.'
fi
exit 0
