import encodings
import json
from config import CV_DATA_SOURCES
from interfaces.strategy.ICVDataStrategy import ICVDataStrategy
from models.cvDataModel import CVData
from models.cvMakerModel import CVDataSource


class CVDataFromInternalFileStrategy(ICVDataStrategy):
    def __init__(self):
        super().__init__()
        self.FILE_ENCODING = encodings.utf_8.getregentry().name
        self.FILE_READ_MODE = 'r'
        self.PERSON_ACRONYM = 'personAcronym'
    
    def get_person_data_source_by_acronym(self, person_acronym: str) -> CVDataSource:
        try:
            with open(CV_DATA_SOURCES, self.FILE_READ_MODE, encoding=self.FILE_ENCODING) as cv_data_sources:
                cv_data_sources_json = json.load(cv_data_sources)
                
                cv_person_data = next((item for item in cv_data_sources_json if item[self.PERSON_ACRONYM] == person_acronym), None)
                if cv_person_data: 
                    cv_data_source = CVDataSource(**cv_person_data)
                    
                    return cv_data_source
                else: raise IndexError(f"Datos de {person_acronym} no encontrados.")
        except Exception:
            raise
        
    def get_cv_data_by_path(self, data_path) -> CVData:
        try:
            with open(data_path, self.FILE_READ_MODE, encoding=self.FILE_ENCODING) as cv_data_json:
                cv_data = CVData.from_dict(json.load(cv_data_json))
                return cv_data
        except Exception:
            raise