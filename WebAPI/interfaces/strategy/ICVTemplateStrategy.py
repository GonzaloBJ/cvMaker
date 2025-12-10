from abc import ABC, abstractmethod
from typing import Any

from models.cvMakerModel import CVTemplate, CVTemplateConfig, RenderedTemplate

class ICVTemplateStrategy(ABC):
    @abstractmethod
    def get_config(self, language_name: str) -> CVTemplateConfig:
        # raise NotImplementedError
        pass
    
    @abstractmethod
    def get_by_name_and_color(self, template_name_param: str, color_scheme: str) -> CVTemplate:
        pass
    
    @abstractmethod
    def get_rendered_template(self, cv_template: CVTemplate, cv_context: dict[str, Any]) -> RenderedTemplate:
        pass

