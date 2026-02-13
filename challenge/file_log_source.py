from pathlib import Path
from typing import List

from .ilog_source import ILogSource


class FileLogSource(ILogSource):
    def __init__(self, path: str):
        self._path = Path(path)

    def read_logs(self) -> List[str]:
        if not self._path.exists():
            return [f"[ERROR] File not found: {self._path}"]

        lines: List[str] = []
        with self._path.open(encoding="utf-8") as f:
            for raw in f:
                line = raw.strip()
                if not line:
                    continue
                lines.append(line)
        return lines

