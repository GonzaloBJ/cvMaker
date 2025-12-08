from abc import ABC, abstractmethod

from models.cvDataModel import Root

class ICVDataRepository(ABC):
    @abstractmethod
    def get_path_by_person_acronym(self, person_acronym: str) -> Root:
        pass
    
    @abstractmethod
    def get_cv_data_by_path(self, data_path: str) -> Root:
        pass
