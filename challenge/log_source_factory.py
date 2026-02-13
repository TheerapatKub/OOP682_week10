from pathlib import Path

from .ilog_source import ILogSource
from .file_log_source import FileLogSource
from .csv_log_source import CsvLogSource


def create_log_source(path: str) -> ILogSource:
    ext = Path(path).suffix.lower()

    if ext == ".csv":
        return CsvLogSource(path)

    return FileLogSource(path)

