from python_algorithms.sorting import *


@dataclass
class PythonSort:
    sorting_list: list

    def sort(
        self, reverse: bool = False, key: Optional[Callable[[Any], Any]] = None
    ) -> "PythonSort":
        self.sorting_list.sort(reverse=reverse, key=key)
        return self
