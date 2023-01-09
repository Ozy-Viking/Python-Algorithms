from __future__ import annotations
from dataclasses import dataclass
from icecream import ic
from typing import Any, Callable, Optional, Protocol

__all__: list[str] = [
    "annotations",
    "Any",
    "Callable",
    "Optional",
    "Protocol",
    "dataclass",
    "ic",
]

from .util import *

__all__ += ["swap", "ISortingAlgorithm"]

from .builtin_sort import PythonSort

__all__ += ["PythonSort"]

from .selection_sort import SelectionSort

__all__ += ["SelectionSort"]

from .insertion_sort import InsertionSort

__all__ += ["InsertionSort"]

from .bubble_sort import BubbleSort

__all__ += ["BubbleSort"]

from .merge_sort import MergeSort

__all__ += ["MergeSort"]
