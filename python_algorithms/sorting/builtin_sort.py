from sorting import *


@dataclass
class PythonSort:
    sorting_list: list

    def sort(
        self, reverse: bool = False, key: Optional[Callable[[Any], Any]] = None
    ) -> Self:
        self.sorting_list.sort(reverse=reverse, key=key)
        return self
