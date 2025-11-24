from pydantic import BaseModel
from typing import Any

class DefaultResponse(BaseModel):
    status: str | None
    message: str | None
    file: str | None
    html: Any | None
    
    def to_dict(self):
        return {
            'status': self.status,
            'message': self.message,
            'file': self.file,
            'html': self.html,
        }
