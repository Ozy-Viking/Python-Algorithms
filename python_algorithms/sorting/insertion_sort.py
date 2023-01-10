"""
Insertion Sort Algorithm
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any
from typing import Callable

from .util import swap


@dataclass
class InsertionSort:
    """
    Insertion Sort Class
    """

    sorting_list: list[Any]

    def sort(
            self,
            key: Callable[[Any], Any] | None = None,
            reverse: bool = False,
    ) -> InsertionSort:
        """
        sort

        Args:
            key (Callable[[Any], Any]): a function to sort by.
            reverse (bool, optional): Sort a sequence in reverse. Defaults to False.

        Returns:
            InsertionSort: Self
        """
        if key:
            self.key_sort(key=key, reverse=reverse)
        else:
            self.sorting_list = self.insertion_sort(
                self.sorting_list, reverse=reverse
            )
        return self

    @staticmethod
    def insertion_sort(
            sorting_list: list[Any], reverse: bool = False
    ) -> list[Any]:
        """
        insertion_sort method

        The method that uses the insertion sort algorithm.

        Args:
            sorting_list: list[Any]: the list to sort.
            reverse: bool, optional: Sort a sequence in reverse.
                                      Defaults to False.
        """
        condition: Callable[[Any, Any], bool] = (
            lambda x, y: bool(x > y) if reverse else bool(x < y)
        )

        for i, swap_number in enumerate(sorting_list):
            if i == 0:
                continue
            sorting_number_index: int = i
            for number in sorting_list[i - 1:: -1]:
                if condition(swap_number, number):
                    swap(
                        sorting_list,
                        sorting_number_index,
                        sorting_number_index - 1,
                    )
                    sorting_number_index -= 1
                else:
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
            reverse (bool, optional): Sort a sequence in reverse.
                                      Defaults to False.
        """
        sorting_dict: dict[Any, Any] = {}
        for value in self.sorting_list:
            sorting_dict[key(value)] = value
        unsorted_list: list[Any] = list(sorting_dict.keys())
        sorted_keys: list[Any] = self.insertion_sort(
            unsorted_list, reverse=reverse
        )
        sorted_list: list[Any] = [sorting_dict[x] for x in sorted_keys]
        self.sorting_list = sorted_list
