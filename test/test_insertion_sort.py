from sorting_algorithms import InsertionSort, SortingAlgorithm
from test import *


def test_insertionsort_type_class(unsorted_list) -> None:
    assert isinstance(InsertionSort(unsorted_list), SortingAlgorithm)


def test_insertionsort_sorted(unsorted_list, sorted_list) -> None:
    assert InsertionSort(unsorted_list).sort().sorting_list == sorted_list


def test_insertionsort_reverse(unsorted_list, reverse_sorted_list) -> None:
    assert (
        InsertionSort(unsorted_list).sort(reverse=True).sorting_list
        == reverse_sorted_list
    )


def test_insertionsort_sort_key(
    unsorted_tuple_list: list, sorted_tuple_list: list, test_sort_key: Callable
) -> None:
    temp_list = unsorted_tuple_list.copy()

    assert (
        InsertionSort(temp_list).sort(key=test_sort_key).sorting_list
        == sorted_tuple_list
    )


def test_insertionsort_sort_reverse_key(
    unsorted_tuple_list: list, reverse_sorted_tuple_list: list, test_sort_key: Callable
) -> None:
    temp_list = unsorted_tuple_list.copy()

    assert (
        InsertionSort(temp_list).sort(reverse=True, key=test_sort_key).sorting_list
        == reverse_sorted_tuple_list
    )


def test_insertionsort_string(
    unsorted_str_list: list[str],
    sorted_str_list: list[str],
) -> None:

    assert InsertionSort(unsorted_str_list).sort().sorting_list == sorted_str_list


def test_insertionsort_string(
    unsorted_str_list: list[str],
    reverse_sorted_str_list: list[str],
) -> None:

    assert (
        InsertionSort(unsorted_str_list).sort(reverse=True).sorting_list
        == reverse_sorted_str_list
    )
