import subprocess
from pathlib import Path

result = subprocess.run(
    ["git", "log", "-5", "--pretty=format:%h | %an | %ad | %s", "--date=short"],
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
