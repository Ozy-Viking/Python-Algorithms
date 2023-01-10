"""
Utilities for sorting module
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Protocol, runtime_checkable


def swap(
        sorting_list: list[Any], initial_index: int, ending_index: int
) -> None:
    """
    swap

    Moves an item in an ordered sequence from initial index to ending index.

    Args:
        sorting_list (list[Any]): the sequence of items which the swap will
                                  be applied to.
        initial_index (int): the initial index of the item to swap.
        ending_index (int): the ending index of the item to swap.
    """
    if initial_index == ending_index:
        return
    temp_item: Any = sorting_list.pop(initial_index)
    sorting_list.insert(ending_index, temp_item)


@runtime_checkable
@dataclass
class ISortingAlgorithm(Protocol):
    """
    ISortingAlgorithm

    The sorting algorithm interface which all implementations will use.

    Variables:
        sorting_list: list: this is the list to be sorted.

    Methods:
        Sort: Callable: This will sort the sorting_list in place.
    """

    sorting_list: list[Any]

    def sort(
            self,
            reverse: bool = False,
            key: Callable[[Any], Any] | None = None,
    ) -> ISortingAlgorithm:
        """
        sort

        Sorts the sorting_list

        Args:
            reverse (bool, optional): Reverse sort boolean. Defaults to False.
            key (Callable[[Any], Any], optional): Lambda function on what to
                                                  sort the sorting list
                                                  on. Defaults to None.

        Returns:
            Self: returns this object.
        """
        return self
