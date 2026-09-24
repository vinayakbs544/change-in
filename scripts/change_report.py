import subprocess
import sys
from pathlib import Path

try:
    count = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    if count < 1:
        raise ValueError
except ValueError:
    print("Usage: python3 scripts/change_report.py [positive number]")
    sys.exit(1)

result = subprocess.run(
    ["git", "log", f"-{count}", "--pretty=format:%h | %an | %ad | %s", "--date=short"],
    capture_output=True,
    text=True,
    check=True
)

report = (
    "Recent Git Changes\n"
    "------------------\n"
    "COMMIT | AUTHOR | DATE | MESSAGE\n"
    f"{result.stdout}\n"
)

output_file = Path("reports/recent_changes.txt")
output_file.parent.mkdir(parents=True, exist_ok=True)
output_file.write_text(report, encoding="utf-8")

print(report)
print(f"Saved report to: {output_file}")
