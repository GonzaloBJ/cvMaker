from dataclasses import dataclass

@dataclass(frozen=True)
class CVGenerationRequest:
    language_name: str
    color_scheme: str
    person_acronym: str
    template_name: str