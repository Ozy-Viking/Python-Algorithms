"""
Bubble Sort Algorithm
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable

from .util import swap


@dataclass
class BubbleSort:
    """
    Bubble Sort Class

    Handles sorting using the Bubble Sort Algorithm.


    """

    sorting_list: list[Any]
    swapped: bool = False

    def sort(
            self,
            reverse: bool = False,
            key: Optional[Callable[[Any], Any]] = None,
    ) -> BubbleSort:
        """
        sort

        Method to control the sorting.

        Args:
            reverse (bool, optional): Sort a sequence in reverse. Defaults to False.
            key (Optional[Callable[[Any], Any]], optional): a function to sort by. Defaults to None.

        Returns:
            BubbleSort: Returns itself.
        """

        if key:
            self.key_sort(reverse=reverse, key=key)
        else:
            self.sorting_list = self.bubble_sort(
                reverse=reverse, sorting_list=self.sorting_list
            )

        return self

    def bubble_sort(
            self, sorting_list: list[Any], reverse: bool = False
    ) -> list[Any]:
        """
        bubble_sort

        Args:
            sorting_list (list[Any]): Sequence to bubble sort.
            reverse (bool, optional): Sort a sequence in reverse.
                                      Defaults to False.

        Returns:
            list[Any]: Sorted List
        """
        condition: Callable[[Any, Any], bool] = (
            lambda x, y: bool(x < y) if reverse else bool(x > y)
        )
        length_list: int = len(sorting_list)
        for i, _ in enumerate(sorting_list):
            if i == length_list - 1:
                continue
            self.swapped = False
            for j, _ in enumerate(sorting_list[: -i - 1]):
                if condition(sorting_list[j], sorting_list[j + 1]):
                    swap(sorting_list, j, j + 1)
                    self.swapped = True
            if not self.swapped:
                break
        return sorting_list

    def key_sort(
            self, key: Callable[[Any], Any], reverse: bool = False
    ) -> None:
        """
        key_sort

        To use a custom key to sort a sequence.

        Args:
            key (Callable[[Any], Any]): a function to sort by.
            reverse (bool, optional): Sort a sequence in reverse. Defaults to False.
        """
        sorting_dict: dict[Any, Any] = {}
        for value in self.sorting_list:
            sorting_dict[key(value)] = value
        unsorted_list: list[Any] = list(sorting_dict.keys())
        sorted_keys: list[Any] = self.bubble_sort(
            unsorted_list, reverse=reverse
        )
        sorted_list: list[Any] = [sorting_dict[x] for x in sorted_keys]
        self.sorting_list = sorted_list
