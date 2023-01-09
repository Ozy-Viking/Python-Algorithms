from sorting import *


@dataclass
class BubbleSort:
    sorting_list: list
    swapped: bool = False

    def sort(
        self,
        reverse: bool = False,
        key: Optional[Callable[[Any], Any]] = None,
    ) -> Self:

        if key:
            self.key_sort(reverse=reverse, key=key)
        else:
            self.sorting_list = self.normal_sort(
                reverse=reverse, sorting_list=self.sorting_list
            )

        return self

    def normal_sort(self, sorting_list: list, reverse: bool = False) -> list[Any]:
        ic(self.swapped)
        condition = lambda x, y: x > y
        if reverse:
            condition = lambda x, y: x < y
        n = len(sorting_list)
        for i, _ in enumerate(sorting_list):
            if i == n-1:
                continue
            self.swapped = False
            for j, _ in enumerate(sorting_list[: -i - 1]):
                if condition(sorting_list[j], sorting_list[j + 1]):
                    swap(sorting_list, j, j + 1)
                    self.swapped = True
            if not self.swapped:
                break
        ic(self.swapped)
        return sorting_list

    def key_sort(self, key: Callable[[Any], Any], reverse: bool = False) -> None:
        sorting_dict = {}
        for value in self.sorting_list:
            sorting_dict[key(value)] = value
        unsorted_list = list(sorting_dict.keys())
        sorted_keys = self.normal_sort(unsorted_list, reverse=reverse)
        sorted_list = [sorting_dict[x] for x in sorted_keys]
        self.sorting_list = sorted_list
