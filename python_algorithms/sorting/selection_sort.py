from typing import Self
from sorting import *


@dataclass
class SelectionSort:
    sorting_list: list[Any]

    def sort(
        self, reverse: bool = False, key: Optional[Callable[[Any], Any]] = None
    ) -> Self:
        if key:
            self.sorting_list = self.key_sort(reverse=reverse, key=key)
        else:
            self.sorting_list = self.normal_sort(
                sorting_list=self.sorting_list.copy(), reverse=reverse
            )

        return self

    @staticmethod
    def normal_sort(
        sorting_list: list[Any],
        reverse: bool = False,
    ) -> None:
        condition = lambda x, y: x < y
        if reverse:
            condition = lambda x, y: x > y

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
    ) -> None:
        sorting_dict = {}
        for value in self.sorting_list:
            sorting_dict[key(value)] = value
        unsorted_list = list(sorting_dict.keys())
        sorted_keys = self.normal_sort(unsorted_list, reverse=reverse)
        sorted_list = [sorting_dict[x] for x in sorted_keys]

        return sorted_list
