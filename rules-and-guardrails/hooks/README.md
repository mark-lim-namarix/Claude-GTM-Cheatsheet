# Hook patterns

Two small hooks you can copy. Read each script before you use it; they run on your machine.

## stop-gate.py: do not finish while the check fails

A Claude Code Stop hook. It runs your check command when Claude tries to finish a turn. If the check fails, Claude is told why and keeps working. It fails closed: no command configured also blocks. After three blocks (a per-session count that resets when the check passes or the hook lets go; change it with STOP_GATE_MAX_BLOCKS) it lets go and prints a warning to the error stream, which Claude Code may not show you in its normal view. That way a broken check cannot trap a session.

Install:

```
mkdir -p ~/.claude/hooks && cp rules-and-guardrails/hooks/stop-gate.py ~/.claude/hooks/
```

Add to your project's `.claude/settings.json` (not the one in your home folder, which would run the check in every folder; merge with what you already have), and set your check command. A change to settings takes effect the next time you start a session. The check's last 20 output lines are sent to Claude, so do not make it print secrets. A long check also needs a longer hook timeout: add `"timeout": 600` to the hook entry.

```
{
  "env": { "STOP_GATE_CMD": "npm test" },
  "hooks": {
    "Stop": [
      { "hooks": [ { "type": "command", "command": "python3 ~/.claude/hooks/stop-gate.py" } ] }
    ]
  }
}
```

Try it first: set `STOP_GATE_CMD` to `false` and confirm Claude is blocked, then to `true` and confirm it can finish.

## secret-scan-before-commit.sh: refuse a commit that adds a secret

A git pre-commit hook. It reads only the lines being added and refuses the commit if one matches a common secret shape (private key header, cloud and chat tokens, long quoted values next to words like key, secret or password). It never prints the secret. It will not catch everything (for example short values, or secrets that are not next to a word like key or password); treat it as a seatbelt, not a vault.

Install (run inside your repo). If you already have a pre-commit hook, add this script to it instead of replacing it, and note that it does nothing if `core.hooksPath` points somewhere else:

```
cp /path/to/this/repo/rules-and-guardrails/hooks/secret-scan-before-commit.sh .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit
```

Try it first: stage a file containing a fake line such as `password = "not-a-real-secret-123"` and confirm the commit is refused.
