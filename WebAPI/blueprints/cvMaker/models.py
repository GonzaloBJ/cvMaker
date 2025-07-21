from pydantic import BaseModel
from typing import Any

class DefaultResponse(BaseModel):
    id: int | None
    message: str | None
    data: Any | None
    
    def to_dict(self):
        return {
            'id': self.id,
            'message': self.message,
            'data': self.data,
        }
