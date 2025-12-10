from abc import ABC, abstractmethod

from models.cvDataModel import CVData
from models.cvMakerModel import CVDataSource

class ICVDataStrategy(ABC):
    @abstractmethod
    def get_person_data_source_by_acronym(self, person_acronym: str) -> CVDataSource:
        pass
    
    @abstractmethod
    def get_cv_data_by_path(self, data_path: str) -> CVData:
        pass
