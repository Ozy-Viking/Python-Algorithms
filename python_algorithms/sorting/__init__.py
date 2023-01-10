"""
Different Sorting Algorithms

Currently available:
    MergeSort
    BubbleSort
    InsertionSort
    SelectionSort
    PythonSort
"""
from __future__ import annotations

from .bubble_sort import BubbleSort
from .builtin_sort import PythonSort
from .insertion_sort import InsertionSort
from .merge_sort import MergeSort
from .selection_sort import SelectionSort
from .util import ISortingAlgorithm
from .util import swap

__all__: list[str] = ["ISortingAlgorithm", "swap"]

__all__ += ["PythonSort"]

__all__ += ["SelectionSort"]

__all__ += ["InsertionSort"]

__all__ += ["BubbleSort"]

__all__ += ["MergeSort"]
