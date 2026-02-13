import csv
from pathlib import Path
from typing import List

from .ilog_source import ILogSource


class CsvLogSource(ILogSource):
    def __init__(self, path: str):
        self._path = Path(path)

    def read_logs(self) -> List[str]:
        if not self._path.exists():
            return [f"[ERROR] CSV file not found: {self._path}"]

        logs: List[str] = []
        with self._path.open(encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                level = (row.get("level") or "INFO").upper()
                message = row.get("message") or ""
                if not message:
                    continue
                logs.append(f"[{level}] {message}")
        return logs

