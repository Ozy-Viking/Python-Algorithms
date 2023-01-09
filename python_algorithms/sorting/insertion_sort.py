from python_algorithms.sorting  import *


@dataclass
class InsertionSort:
    sorting_list: list

    def sort(
        self,
        reverse: bool = False,
        key: Optional[Callable[[Any], Any]] = None,
    ) -> 'InsertionSort':
        if key:
            self.key_sort(key=key, reverse=reverse)
        else:
            self.sorting_list = self.normal_sort(self.sorting_list, reverse=reverse)
        return self

    @staticmethod
    def normal_sort(sorting_list: list, reverse: bool = False) -> list[Any]:
        condition = lambda x, y: x < y
        if reverse:
            condition = lambda x, y: x > y

        for i, swap_number in enumerate(sorting_list):
            if i == 0:
                continue
            sorting_number_index = i
            for number in sorting_list[i - 1 :: -1]:
                if condition(swap_number, number):
                    swap(sorting_list, sorting_number_index, sorting_number_index - 1)
                    sorting_number_index -= 1
                else:
                    break
        return sorting_list

    def key_sort(self, key: Callable[[Any], Any], reverse: bool = False) -> None:
        sorting_dict = {}
        for value in self.sorting_list:
            sorting_dict[key(value)] = value
        unsorted_list = list(sorting_dict.keys())
        sorted_keys = self.normal_sort(unsorted_list, reverse=reverse)
        sorted_list = [sorting_dict[x] for x in sorted_keys]
        self.sorting_list = sorted_list
