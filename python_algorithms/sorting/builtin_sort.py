"""
Built-in Sorting Algorithm
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Optional


@dataclass
class PythonSort:
    """
    Python Sort

    A comparison class that uses the built-in Python sorting algorithm.
    """

    sorting_list: list[Any]

    def sort(
            self, reverse: bool = False,
            key: Optional[Callable[[Any], Any]] = None
    ) -> PythonSort:
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
            PythonSort: Returns itself.
        """
        self.sorting_list.sort(reverse=reverse, key=key)
        return self
