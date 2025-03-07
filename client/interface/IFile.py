from abc import ABC, abstractmethod


class IFile(ABC):
    
    @abstractmethod
    def chose_file():
        pass
    
    @abstractmethod
    def check_correct_dir(dir):
        pass
    
    @abstractmethod
    def check_find():
        pass
    
    @abstractmethod
    def file_send_quantity(address):
        pass
    
    @abstractmethod
    def chose_file():
        pass
    
    @abstractmethod
    def get_files_list(files, file_path):
        pass
    
    @abstractmethod
    def file_send(chose_func):
        pass
    
    
    