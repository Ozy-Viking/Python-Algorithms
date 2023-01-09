from python_algorithms.sorting import BubbleSort, ISortingAlgorithm
from test import *


def test_bubblesort_type_class(unsorted_list) -> None:
    assert isinstance(BubbleSort(unsorted_list), ISortingAlgorithm)


def test_bubblesort_sorted(unsorted_list, sorted_list) -> None:
    assert BubbleSort(unsorted_list).sort().sorting_list == sorted_list


def test_bubblesort_reverse(unsorted_list, reverse_sorted_list) -> None:
    assert (
        BubbleSort(unsorted_list).sort(reverse=True).sorting_list == reverse_sorted_list
    )


def test_bubblesort_sort_key(
    unsorted_tuple_list: list, sorted_tuple_list: list, test_sort_key: Callable
) -> None:
    temp_list = unsorted_tuple_list.copy()

    assert (
        BubbleSort(temp_list).sort(key=test_sort_key).sorting_list == sorted_tuple_list
    )


def test_bubblesort_sort_reverse_key(
    unsorted_tuple_list: list, reverse_sorted_tuple_list: list, test_sort_key: Callable
) -> None:
    temp_list = unsorted_tuple_list.copy()

    assert (
        BubbleSort(temp_list).sort(reverse=True, key=test_sort_key).sorting_list
        == reverse_sorted_tuple_list
    )


def test_bubblesort_sorted_swap_no_break(sorted_list: list) -> None:
    test_list = sorted_list
    test_list.reverse()
    test = BubbleSort(test_list)
    test.sort()
    assert test.swapped == True


def test_bubblesort_sorted_swap_break(sorted_list: list) -> None:
    test_list = sorted_list
    test = BubbleSort(test_list)
    test.sort()
    assert test.swapped == False


def test_bubblesort_string(
    unsorted_str_list: list[str],
    sorted_str_list: list[str],
) -> None:

    assert BubbleSort(unsorted_str_list).sort().sorting_list == sorted_str_list


def test_bubblesort_string(
    unsorted_str_list: list[str],
    reverse_sorted_str_list: list[str],
) -> None:

    assert (
        BubbleSort(unsorted_str_list).sort(reverse=True).sorting_list
        == reverse_sorted_str_list
    )
