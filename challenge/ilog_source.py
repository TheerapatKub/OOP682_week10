from abc import ABC, abstractmethod
from typing import List


class ILogSource(ABC):
    @abstractmethod
    def read_logs(self) -> List[str]:
        raise NotImplementedError

