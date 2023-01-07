from dataclasses import dataclass

@dataclass
class Room:
    code: str
    creator: str
    word: str
    tries: int