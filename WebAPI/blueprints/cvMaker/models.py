from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class DefaultResponse(BaseModel):
    status: str | None
    message: str | None
    file: str | None
    html: str | None
    
    def __init__(self, status: str | None = None, message: str | None = None, file: str | None = None, html: str | None = None) -> None:
        super().__init__(status=status, message=message, file=file, html=html)
    
    # def to_dict(self):
    #     return {
    #         'status': self.status,
    #         'message': self.message,
    #         'file': self.file,
    #         'html': self.html,
    #     }
