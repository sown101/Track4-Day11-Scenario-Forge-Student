"""Run the supplied pipeline with the five-digit student code in REPORT.md.

Usage: python run_lab.py all
The original runner accepts only 6-12 digits in REPORT.md. Its documented
LAB11_MSSV override preserves our five digits, including the leading zero.
"""
from pathlib import Path
import os
import re
import runpy


def main():
    root = Path(__file__).resolve().parent
    report = (root / "REPORT.md").read_text(encoding="utf-8")
    first = next((line for line in report.splitlines() if line.strip()), "")
    match = re.fullmatch(r"MSSV:\s*(\d{5})\s*", first)
    if match is None:
        raise SystemExit("REPORT.md must start with MSSV: followed by five digits.")
    os.environ["LAB11_MSSV"] = match.group(1)
    runpy.run_path(str(root / "run_all.py"), run_name="__main__")


if __name__ == "__main__":
    main()
