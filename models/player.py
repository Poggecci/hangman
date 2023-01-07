from dataclasses import dataclass
from typing import List

@dataclass
class Player:
    uid: str
    room: str
    attempted: List[str]
