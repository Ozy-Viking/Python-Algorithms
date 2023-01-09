# Sorting Algorithms

## Interface Sorting Classes

```python
@dataclass
class ISortingAlgorithm:
    sorting_list: list[Any]

    def Sort(self,
             reverse: bool = False,
             key: Optional[Callable[[Any], Any]] = None,
            ) -> Self
        return self
```

## List of Completed Sorting Algorithms

1. Bubble Sort
2. Insertion Sort
3. Merge Sort
4. Selection Sort
5. The Builtin Sort

## Sorting Algorithms todo

1. Shell Sort
2. Radix Sort: <https://www.geeksforgeeks.org/radix-sort/>
3. Heap Sort: <https://www.geeksforgeeks.org/heap-sort/>
