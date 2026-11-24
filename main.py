import os
from pathlib import Path
import sys

TEXT = "I lost the bounty. I'd blame the model, but I am the model."

assert 1 <= len(TEXT) <= 280

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output")
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))
print(len(TEXT), file=sys.stderr)
