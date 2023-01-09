from dataclasses import dataclass
from typing import Any, Callable, Optional, Protocol, Self, runtime_checkable


def swap(sorting_list: list, intial_index: int, ending_index: int) -> None:
    if intial_index == ending_index:
        return
    temp_item = sorting_list.pop(intial_index)
    sorting_list.insert(ending_index, temp_item)


@runtime_checkable
@dataclass
class ISortingAlgorithm(Protocol):
    """
    ISortingAlgorithm

    The sorting algorithm interface which all implementations will use.

    Args:
        Protocol (_type_): _description_

    Variables:
        sorting_list: list: this is the list to be sorted.

    Methods:
        Sort: Callable: This will sort the sorting_list in place.
    """

    sorting_list: list

    def sort(
        self,
        reverse: bool = False,
        key: Optional[Callable[[Any], Any]] = None,
    ) -> Self:
        """
        sort

        Sorts the sorting_list

        Args:
            reverse (bool, optional): Reverse sort boolean. Defaults to False.
            key (Callable[[Any], Any], optional): Lambda function on what to sort the sorting list on. Defaults to None.

        Returns:
            Self: returns this object.
        """
        return self
