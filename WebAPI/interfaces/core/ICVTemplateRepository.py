from abc import ABC, abstractmethod

from models.cvMakerModel import CVTemplate, CVTemplateConfig

class ICVTemplateRepository(ABC):
    @abstractmethod
    def get_config(self) -> CVTemplateConfig:
        raise NotImplementedError

    @abstractmethod
    def get_by_name_and_color(self, template_name_param: str, color_scheme: str) -> CVTemplate:
        raise NotImplementedError
    
    @abstractmethod
    def get_rendered_template(self) -> str:
        raise NotImplementedError

