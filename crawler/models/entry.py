from dataclasses import dataclass


@dataclass
class Entry:
    rank: int
    title: str
    points: int
    number_comments: int
