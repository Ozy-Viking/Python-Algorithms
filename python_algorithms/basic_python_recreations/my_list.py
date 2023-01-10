"""
List recreation

Raises:
    NotImplementedError: on Planned but not Implemented parts.
"""
from __future__ import annotations

from typing import Any


class List:
    """
    List class
    """

    def __init__(self, *args: Any | None) -> None:
        self.List: dict[int, Any | None] = {
            i: arg for i, arg in enumerate(args)
        }

    def __getitem__(self, key: int | slice) -> Any:
        if isinstance(key, slice):
            raise NotImplementedError
        return self.List[key]

    def __eq__(self, __o: object) -> bool:
        for i, val in self.List.items():
            if val != __o[i]:  # type: ignore
                return False
        return True

    def __repr__(self) -> str:
        str_repr: str = "["
        if self.List:
            for i, item in self.List.items():
                if i == 0:
                    str_repr += str(item)
                    continue
                str_repr += ", " + str(item)
        str_repr += "]"
        return str_repr

    def __str__(self) -> str:
        return repr(self)

    def __len__(self) -> int:
        count: int = 0
        for _ in self.List:
            count += 1
        return count

    def append(self) -> None:
        """
        append
        """
        raise NotImplementedError

    def clear(self) -> None:
        """
        clear
        """
        raise NotImplementedError

    def copy(self) -> None:
        """
        copy
        """
        raise NotImplementedError

    def count(self) -> None:
        """
        count
        """
        raise NotImplementedError

    def extend(self) -> None:
        """
        extend
        """
        raise NotImplementedError

    def index(self) -> None:
        """
        index
        """
        raise NotImplementedError

    def insert(self) -> None:
        """
        insert
        """
        raise NotImplementedError

    def pop(self) -> None:
        """
        pop
        """
        raise NotImplementedError

    def remove(self) -> None:
        """
        remove
        """
        raise NotImplementedError

    def reverse(self) -> None:
        """
        reverse
        """
        raise NotImplementedError

    def sort(self) -> None:
        """
        sort
        """
        raise NotImplementedError


list_dir: str = """
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__'
 '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
 '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__',
 '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__',
 '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__',
 '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__',
 '__setitem__', '__sizeof__', '__str__', '__subclasshook__', ]
"""
