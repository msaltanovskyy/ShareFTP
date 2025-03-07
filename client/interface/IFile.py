from abc import ABC, abstractmethod
from typing import List, Any


class IFile(ABC):

    @abstractmethod
    def select_and_verify_dir(self) -> str:
        pass

    @abstractmethod
    def get_files_list(self, files: List[str], dir_path: str) -> None:
        pass

    @abstractmethod
    def select_files(self, dir_path: str) -> List[str]:
        pass

    @abstractmethod
    def send_files(self, address, files: List[str]) -> None:
        pass

    @abstractmethod
    def file_send(self, chose_func) -> None:
        pass
