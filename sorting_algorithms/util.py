from dataclasses import dataclass
from typing import Any, Callable, Optional, Protocol, Self, runtime_checkable


def swap(sorting_list: list, intial_index: int, ending_index: int) -> None:
    if intial_index == ending_index:
        return
    temp_item = sorting_list.pop(intial_index)
    sorting_list.insert(ending_index, temp_item)


@runtime_checkable
@dataclass
class SortingAlgorithm(Protocol):
    sorting_list: list

    def sort(
        self,
        reverse: bool = False,
        key: Optional[Callable[[Any], Any]] = None,
    ) -> Self:
        return self
