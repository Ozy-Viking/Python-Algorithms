from sorting import *


@dataclass
class MergeSort:
    sorting_list: list
    condition: Callable = lambda x, y: x <= y

    def sort(
        self,
        reverse: bool = False,
        key: Optional[Callable[[Any], Any]] = None,
    ) -> Self:
        if reverse:
            self.condition = lambda x, y: x >= y
        if key:
            self.key_sort(key=key)
        else:

            self.merge_sort(self.sorting_list)

        return self

    def merge_sort(self, sorting_list: list[Any]) -> list[Any]:
        length = len(sorting_list)
        if length > 1:
            mid: int = length // 2

            left: list[Any] = sorting_list[:mid]
            right: list[Any] = sorting_list[mid:]
            self.merge_sort(left)
            self.merge_sort(right)

            i = j = k = 0

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
        sorting_dict = {}
        for value in self.sorting_list:
            sorting_dict[key(value)] = value
        sort_list = list(sorting_dict.keys())
        self.merge_sort(sort_list)
        sorted_list = [sorting_dict[x] for x in sort_list]
        self.sorting_list = sorted_list
