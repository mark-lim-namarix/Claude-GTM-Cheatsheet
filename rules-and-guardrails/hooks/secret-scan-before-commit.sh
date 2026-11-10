#!/usr/bin/env bash
# Git pre-commit hook: refuse a commit that adds something that looks like a secret.
# Setup: see hooks/README.md. It checks only the lines you are adding, and never prints the secret.
set -u
BEGIN='-----BEGIN'
# Shapes where upper and lower case matter.
exact_patterns=(
  "${BEGIN} [A-Z ]*PRIVATE KEY"
  'AKIA[0-9A-Z]{16}'
  'gh[pousr]_[A-Za-z0-9]{36,}'
  'xox[abprs]-[A-Za-z0-9-]{10,}'
  '(^|[^A-Za-z0-9])sk-[A-Za-z0-9_-]{20,}'
)
# Words like key, secret, token, password followed by a long value (quoted, or unquoted without brackets).
named_patterns=(
  '(api[_-]?key|secret|token|passwd|password)[A-Za-z0-9_]*["'"'"']?[[:space:]]*[:=][[:space:]]*["'"'"'][^"'"'"'[:space:]]{12,}["'"'"']'
  '(api[_-]?key|secret|token|passwd|password)[A-Za-z0-9_]*[[:space:]]*[:=][[:space:]]*[A-Za-z0-9/+=_.-]{16,}[[:space:]]*$'
)
if ! command -v git >/dev/null 2>&1; then
  echo "secret-scan: git not found, so nothing was checked. Commit refused." >&2
  exit 1
fi
diff_out=$(git diff --cached -U0 --no-color) || { echo "secret-scan: git diff failed, so nothing was checked. Commit refused." >&2; exit 1; }
added=$(printf '%s\n' "$diff_out" | grep -E '^\+' | grep -Ev '^\+\+\+ ' || true)
status=0
for p in "${exact_patterns[@]}"; do
  if printf '%s\n' "$added" | grep -Eq -- "$p"; then
    echo "secret-scan: staged changes match a secret pattern ($p). Commit refused. Remove it and rotate it if it was ever real." >&2
    status=1
  fi
done
for p in "${named_patterns[@]}"; do
  if printf '%s\n' "$added" | grep -Eiq -- "$p"; then
    echo "secret-scan: staged changes match a secret pattern ($p). Commit refused. Remove it and rotate it if it was ever real." >&2
    status=1
  fi
done
exit $status
