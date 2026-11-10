#!/usr/bin/env python3
"""Stop hook: do not let Claude Code finish a turn while your check fails.

Setup: see hooks/README.md. Set the check command in STOP_GATE_CMD (for example "npm test").
Behaviour (fail closed):
  - check passes            -> exit 0, Claude may stop
  - check fails             -> exit 2, the output goes back to Claude to fix
  - no command configured   -> exit 2, says so (a gate that cannot run must not pass)
  - after STOP_GATE_MAX_BLOCKS consecutive blocks (default 3) it lets go and prints a warning,
    so a broken check cannot trap a session forever.
"""
import json, os, subprocess, sys, tempfile

def env_int(name, default):
    try:
        return int(os.environ.get(name, str(default)))
    except ValueError:
        return default

def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        data = {}
    session = str(data.get("session_id", "default")).replace("/", "_")
    counter = os.path.join(tempfile.gettempdir(), f"stop-gate-{session}.count")
    max_blocks = env_int("STOP_GATE_MAX_BLOCKS", 3)
    cmd = os.environ.get("STOP_GATE_CMD", "").strip()

    def blocks():
        try:
            return int(open(counter).read().strip() or "0")
        except Exception:
            return 0

    def block(message):
        n = blocks() + 1
        if n > max_blocks:
            sys.stderr.write(f"stop-gate: still failing after {max_blocks} blocks, letting go. Last problem: {message}\n")
            try:
                os.remove(counter)
            except OSError:
                pass
            return 0
        open(counter, "w").write(str(n))
        sys.stderr.write(f"stop-gate: not done. {message}\n")
        return 2

    if not cmd:
        return block("STOP_GATE_CMD is not set, so nothing was checked. Set it to your test command.")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=env_int("STOP_GATE_TIMEOUT", 600))
    except subprocess.TimeoutExpired:
        return block(f"the check timed out: {cmd}")
    if result.returncode != 0:
        tail = (result.stdout + result.stderr).strip().splitlines()[-20:]
        return block(f"the check failed (exit {result.returncode}): {cmd}\n" + "\n".join(tail))
    try:
        os.remove(counter)
    except OSError:
        pass
    return 0

if __name__ == "__main__":
    sys.exit(main())
