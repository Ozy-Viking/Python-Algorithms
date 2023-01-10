"""
Selection Sort Algorithm
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable

from .util import swap


@dataclass
class SelectionSort:
    """
    Selection Sort Class
    """

    sorting_list: list[Any]

    def sort(
            self, reverse: bool = False,
            key: Optional[Callable[[Any], Any]] = None,
    ) -> SelectionSort:
        """
        sort

        Method to control the sorting.

        Args:
            reverse (bool, optional): Sort a sequence in reverse.
                                      Defaults to False.
            key (Optional[Callable[[Any], Any]], optional): a function to sort
                                                            by. Defaults to
                                                            None.

        Returns:
            SelectionSort: Returns itself.
        """
        if key:
            self.sorting_list = self.key_sort(reverse=reverse, key=key)
        else:
            self.sorting_list = self.selection_sort(
                sorting_list=self.sorting_list.copy(), reverse=reverse
            )

        return self

    @staticmethod
    def selection_sort(
            sorting_list: list[Any],
            reverse: bool = False,
    ) -> list[Any]:
        """
        selection_sort

        Method that runs the selection sort algorithm on a given
        ordered sequence.

        Args:
            sorting_list (list[Any]): Ordered sequence to sort.
            reverse (bool, optional): _description_. Defaults to False.

        Returns:
            list[Any]: Sorted sequence.
        """
        condition: Callable[[Any, Any], bool] = (
            lambda x, y: bool(x < y) if reverse else bool(x > y)
        )

        for i, number in enumerate(sorting_list):
            sorting_number_index: int = i
            sorting_number: int = number
            for j, compare_number in enumerate(sorting_list[i:]):
                if condition(compare_number, sorting_number):
                    sorting_number_index = j + i
                    sorting_number = compare_number
            swap(sorting_list, sorting_number_index, i)
        return sorting_list

    def key_sort(
            self,
            key: Callable[[Any], Any],
            reverse: bool = False,
    ) -> list[Any]:
        """
        key_sort method

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
        sorted_keys: list[Any] = self.selection_sort(
            unsorted_list, reverse=reverse
        )
        sorted_list: list[Any] = [sorting_dict[x] for x in sorted_keys]

        return sorted_list
