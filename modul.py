from functools import total_ordering

@total_ordering

class Accommodation:
    name: str
    _city: str
    __price: int


    def __init__(self, name: str, price: int, city: str = "Debrecen") -> None:
        self.name = name
        self._city = city
        self.__price = price


    def __repr__(self) -> str:
        return f"{self.name}, {self._city}, {self.__price}"

    def __str__(self) -> str:
        return f"{self.name} ({self._city}): {self.__price} Ft"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Accomodation):
            return False
        return (self.name, self._city, self.__price) == (other.name, other._city, other.__price)

    def __lt__(self, other) -> bool:
        if not isinstance(other, Accomodation):
            return NotImplemented
        return (self._city, self.__price, self.name) < (other._city, other.__price, other.name)

    @property
    def city(self) -> str:
        print("accessing city")
        return self._city

    @property
    def price(self) -> int:
        print("accessing price")
        return self.__price

    @price.setter
    def price(self, value: int) -> None:
        print(f"setting price to {value}")
        if value < 0:
            raise ValueError(f"Invalid price {value}")
        self.__price = value

    @staticmethod
    def count(l: list[object], c: str) -> int:
        db = 0
        for i in l:
            if i._city == c:
                db+=1
        return db

class Hotel(Accommodation):

    _stars: int

    def __init__(self, name, price, city, stars) -> None:
        super().__init__(name, price, city)
        self._stars = stars

    @property
    def stars(self) -> int:
        print("accessing stars")
        return self._stars

    @stars.setter
    def stars(self, value: int) -> None:
        print(f"setting stars to {value}")
        if value < 1 or value > 5 :
            raise ValueError(f"Invalid stars {value}")
        self._stars = value

    def __repr__(self) -> str:
        return f"{super().__repr__()}, {self._stars}"

    def __str__(self) -> str:
        return f"{super().__str__()} // {self._stars}*"