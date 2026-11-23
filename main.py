# One-Line Roast: The Gadget You Use Every Day — writes a single original
# roast line to /output/entry.txt.
# Python 3.13, standard library only, no network, no secrets.
import os
from pathlib import Path

LINE = (
    "My smartwatch buzzes to remind me to breathe, as if the last thirty "
    "years of doing it unsupervised were a fluke."
)

# The gate requires 1-200 characters of non-whitespace UTF-8 text.
if not 1 <= len(LINE.strip()) <= 200:
    raise SystemExit(f"entry line must be 1-200 characters, got {len(LINE)}")

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
entry_path = out_dir / "entry.txt"
entry_path.write_text(LINE + "\n", encoding="utf-8")
print(f"Wrote {len(LINE)} characters to {entry_path}")
