"""
Merge Sort
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable


@dataclass
class MergeSort:
    """
    Merge Sort Class
    """

    sorting_list: list[Any]
    condition: Callable[[Any, Any], bool] = lambda x, y: bool(x <= y)

    def sort(
            self,
            reverse: bool = False,
            key: Callable[[Any], Any] | None = None,
    ) -> MergeSort:
        """
        sort

        Handles the sorting.

        Args:
            reverse: bool, optional: Reverse the sort. Defaults to False.
            key: Optional[Callable[[Any], Any]]: Key to sort by.
                                                 Defaults to None.

        Returns:
            MergeSort: Self
        """
        if reverse:
            self.condition = lambda x, y: bool(x >= y)
        if key:
            self.key_sort(key=key)
        else:

            self.merge_sort(self.sorting_list)

        return self

    def merge_sort(self, sorting_list: list[Any]) -> None:
        """
        merge_sort

        Runs the merge sort algorithm on a sequence.

        Args:
            sorting_list: list[Any]: a sequence to sort.
        """
        length: int = len(sorting_list)
        if length > 1:
            mid: int = length // 2

            left: list[Any] = sorting_list[:mid]
            right: list[Any] = sorting_list[mid:]
            self.merge_sort(left)
            self.merge_sort(right)
            i: int = 0
            j: int = 0
            k: int = 0

            while i < len(left) and j < len(right):
                if self.condition(left[i], right[j]):
                    sorting_list[k] = left[i]
                    i += 1
                else:
                    sorting_list[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                sorting_list[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                sorting_list[k] = right[j]
                j += 1
                k += 1

    def key_sort(self, key: Callable[[Any], Any]) -> None:
        """
        key_sort

        To use a custom key to sort a sequence.

        Args:
            key (Callable[[Any], Any]): a function to sort by.
        """
        sorting_dict: dict[Any, Any] = {}
        for value in self.sorting_list:
            sorting_dict[key(value)] = value
        sort_list: list[Any] = list(sorting_dict.keys())
        self.merge_sort(sort_list)
        sorted_list: list[Any] = [sorting_dict[x] for x in sort_list]
        self.sorting_list = sorted_list
