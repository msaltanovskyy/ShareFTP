from abc import ABC, abstractmethod


class IFile(ABC):
    
    @abstractmethod
    def select_dir():
        pass
    
    @abstractmethod
    def proof_correct_dir(dir):
        pass
    
    @abstractmethod
    def file_send_quantity(address):
        pass
    
    @abstractmethod
    def select_file():
        pass
    
    @abstractmethod
    def get_files_list(files, file_path):
        pass
    
    @abstractmethod
    def file_send(chose_func):
        pass
    
    
    