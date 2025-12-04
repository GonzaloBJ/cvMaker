from abc import ABC, abstractmethod

from models.cvDataModel import Root

class ICVDataRepository(ABC):
    @abstractmethod
    def get_by_acronym(self, person_acronym: str) -> Root:
        pass
