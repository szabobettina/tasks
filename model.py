from __future__ import annotations

from dataclasses import field, dataclass
from enum import Enum


@dataclass
class Car:

    id: int = field(hash=True)
    name: str = field(compare=False)
    door: int = field(compare=False)
    engine: list[Engine] = field(compare=False, repr=False, default_factory=lambda: [])
    type: Type = field(compare=False, default_factory=lambda: Car.Type.AUDI)

    class Type(Enum):
        AUDI = "Audi"
        FERRARI = "Ferrari"
        MERCEDES = "Mercedes"
        SUZUKI = "Suzuki"

    @dataclass
    class Engine:

        number: str = field(hash=True)
        fordulat_szam: int = field(compare=False)
        henger: int = field(compare=False)