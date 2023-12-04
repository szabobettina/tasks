from __future__ import annotations

from itertools import chain
from typing import cast

from model import Car
from queries import Queries
from common.repository import Repository


class Solution(Repository, Queries):

    @staticmethod
    def type_mapper(values: dict[str, any]) -> Car | Car.Engine:
        if "id" in values:
            car = Car(**values)
            car.type = next(
                Car.Type[entry.name]
                for entry in Car.Type
                if entry.value == car.type
            )
            return car
        else:
            return Car.Engine(**values)

    @property
    def entities(self) -> list[Car]:
        return cast(list[Car], super().entities)

    def group_by_type(self) -> dict[Car.Type, list[Car]]:
        return {
            type: [
                car
                for car in self.entities
            ]
            for type in {
                car.type
                for car in self.entities
            }
        }

    def count_of_type(self, type: Car.Type) -> int:
        return len(
            [
                car
                for car in self.entities
                if car.type == type
            ]
        )

    def order(self) -> list[Car]:
        return sorted(
            self.entities,
            key=lambda car: (-len(car.engine), car.door)
        )

    def distinct_engine_nums(self) -> set[str]:
        return {
            engine.number
            for engine in chain.from_iterable(
                [
                    car.engine
                    for car in self.entities
                ]
            )
        }

    def set_having_the_greatest_henger_engine(self) -> Car:
        return next(
            car
            for car in self.entities
            if len(car.engine) == max(
                [
                    len(car.engine)
                    for car in self.entities
                ]
            )
        )


def main() -> None:
    repository = Solution(r"../data/cars.json")

    for car in repository.entities:
        print(car)


if __name__ == "__main__":
    main()