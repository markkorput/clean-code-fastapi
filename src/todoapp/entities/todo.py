from datetime import datetime
from dataclasses import dataclass

@dataclass
class Todo:
    text: str
    user_id: str
    id: str | None = None 
    done_at: datetime | None = None

