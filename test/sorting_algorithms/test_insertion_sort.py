"""
Testing for insertion sort algorithm
"""
from typing import Any
from typing import Callable

from python_algorithms.sorting import InsertionSort
from python_algorithms.sorting import ISortingAlgorithm


def test_type_class(unsorted_list: list[Any]) -> None:
    """
    test_type_class

    Args:
        unsorted_list (list[Any]): Pytest fixture.
    """
    assert isinstance(InsertionSort(unsorted_list), ISortingAlgorithm)


def test_sorted(unsorted_list: list[Any], sorted_list: list[Any]) -> None:
    """
    test_sorted

    Args:
        unsorted_list (list[Any]): Pytest fixture.
        sorted_list (list[Any]): Pytest fixture.
    """
    assert InsertionSort(unsorted_list).sort().sorting_list == sorted_list


def test_reverse(
    unsorted_list: list[Any], reverse_sorted_list: list[Any]
) -> None:
    """
    test_reverse

    Args:
        unsorted_list (list[Any]): Pytest fixture.
        reverse_sorted_list (list[Any]): Pytest fixture.
    """
    assert (
        InsertionSort(unsorted_list).sort(reverse=True).sorting_list
        == reverse_sorted_list
    )


def test_sort_with_key(
    unsorted_tuple_list: list[Any],
    sorted_tuple_list: list[Any],
    test_sort_key: Callable[..., Any],
) -> None:
    """
    test_sort_key

    Args:
        unsorted_tuple_list (list[Any]): Pytest fixture.
        sorted_tuple_list (list[Any]): Pytest fixture.
        test_sort_key (Callable[..., Any]): Pytest fixture.
    """
    temp_list: list[Any] = unsorted_tuple_list.copy()

    assert (
        InsertionSort(temp_list).sort(key=test_sort_key).sorting_list
        == sorted_tuple_list
    )


def test_sort_reverse_key(
    unsorted_tuple_list: list[Any],
    reverse_sorted_tuple_list: list[Any],
    test_sort_key: Callable[..., Any],
) -> None:
    """
    test_sort_reverse_key

    Args:
        unsorted_tuple_list (list[Any]): Pytest fixture.
        reverse_sorted_tuple_list (list[Any]): Pytest fixture.
        test_sort_key (Callable[..., Any]): Pytest fixture.
    """
    temp_list: list[Any] = unsorted_tuple_list.copy()

    assert (
        InsertionSort(temp_list)
        .sort(reverse=True, key=test_sort_key)
        .sorting_list
        == reverse_sorted_tuple_list
    )


def test_string(
    unsorted_str_list: list[str],
    sorted_str_list: list[str],
) -> None:
    """
    test_string

    Args:
        unsorted_str_list (list[str]): Pytest fixture.
        sorted_str_list (list[str]): Pytest fixture.
    """
    assert (
        InsertionSort(unsorted_str_list).sort().sorting_list == sorted_str_list
    )


def test_string_reverse(
    unsorted_str_list: list[str],
    reverse_sorted_str_list: list[str],
) -> None:
    """
    test_string_reverse

    Args:
        unsorted_str_list (list[str]): Pytest fixture.
        reverse_sorted_str_list (list[str]): Pytest fixture.
    """
    assert (
        InsertionSort(unsorted_str_list).sort(reverse=True).sorting_list
        == reverse_sorted_str_list
    )
