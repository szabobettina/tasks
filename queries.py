from abc import abstractmethod, ABC

from model import Car


class Queries(ABC):

    @abstractmethod
    def count_of_type(self, theme: Car.Type) -> int:
        """
        Returns the count of Cars that belong to the given type.
        :param type: the type
        :return: the count
        """

    @abstractmethod
    def order(self) -> list[Car]:
        """
        Returns a copy of Cars sets ordered by:
        * the count of their engine in descending order
        * the number of their door in ascending order
        :return: the sorted list
        """

    @abstractmethod
    def group_by_type(self) -> dict[Car.Type, list[Car]]:
        """
        Groups the sets by their type.
        :return: the grouping
        """

    @abstractmethod
    def distinct_engine_ids(self) -> set[str]:
        """
        Returns the IDs of all the engine.
        :return: the IDs
        """

    @abstractmethod
    def set_having_the_greatest_henger_engine(self) -> Car:
        """
        Returns the set that contains the greatest number of henger of engine.
        :return: the set
        """