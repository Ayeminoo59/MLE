#!/usr/bin/env bash
set -euo pipefail

ZSHRC="$HOME/.zshrc"
BACKUP=""

echo "Fixing locale in $ZSHRC (may ask for sudo)..."

if [ ! -e "$ZSHRC" ]; then
  echo "$ZSHRC not found — creating empty file (with sudo)..."
  sudo touch "$ZSHRC"
  sudo chown "$(whoami):staff" "$ZSHRC"
  sudo chmod u+w "$ZSHRC"
fi

OWNER=$(ls -ld "$ZSHRC" | awk '{print $3}')
if [ "$OWNER" != "$(whoami)" ]; then
  BACKUP="${ZSHRC}.bak.$(date +%s)"
  echo "Backing up $ZSHRC -> $BACKUP"
  sudo cp "$ZSHRC" "$BACKUP"
  echo "Changing owner to $(whoami)"
  sudo chown "$(whoami):staff" "$ZSHRC"
  sudo chmod u+w "$ZSHRC"
fi

append_if_missing() {
  local line="$1"
  local file="$2"
  grep -Fqx -- "$line" "$file" || printf '%s\n' "$line" >> "$file"
}

append_if_missing "export LANG=en_US.UTF-8" "$ZSHRC"
append_if_missing "export LC_ALL=en_US.UTF-8" "$ZSHRC"

echo "Added locale exports to $ZSHRC."
if [ -n "$BACKUP" ]; then
  echo "Backup saved at $BACKUP"
fi

echo ""
echo "Note: run 'source ~/.zshrc' in your interactive shell (or restart Terminal/VSCode) to apply changes there."
echo ""
echo "Showing current values for verification (this script's environment):"
# shellcheck disable=SC1090
. "$ZSHRC" || true
echo "LANG=$LANG"
locale
python3 - <<'PY'
print("Python test output: မြန်မာစာ စမ်းသပ်ချက်")
PY

echo ""
echo "If output above shows Myanmar text correctly, restart VSCode/Cursor terminal and try running your code again."

