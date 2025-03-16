import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k = 15))


@dataclass
class Student:
    name: string
    surname: string
    active: bool = field(default=True)
    login: string = field(init=False)
    id: str = field(default=generate_id(), init=False)

    def __post_init__(self):
        self.login = f'{self.name[0]}{self.surname}'
