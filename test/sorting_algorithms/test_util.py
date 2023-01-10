"""
Testing for the utility module
"""
import pytest

from python_algorithms.sorting import ISortingAlgorithm
from python_algorithms.sorting import swap


def test_swap_01(unswaped_list: list[int]) -> None:
    """
    test_swap_01

    from index 0 to index 1.

    Args:
        unswaped_list (list[int]): Pytest fixture.
    """
    test_list: list[int] = unswaped_list.copy()
    swap(test_list, 0, 1)
    assert test_list == [1, 0, 2, 3]


def test_swap_n10(unswaped_list: list[int]) -> None:
    """
    test_swap_n10

    from index -1 to index 0.

    Args:
        unswaped_list (list[int]): Pytest fixture.
    """
    test_list: list[int] = unswaped_list.copy()
    swap(test_list, -1, 0)
    assert test_list == [3, 0, 1, 2]


def test_swap_21(unswaped_list: list[int]) -> None:
    """
    test_swap_n10

    from index 2 to index 1.

    Args:
        unswaped_list (list[int]): Pytest fixture.
    """
    test_list: list[int] = unswaped_list.copy()
    swap(test_list, 2, 1)
    assert test_list == [0, 2, 1, 3]


def test_swap_same_index(unswaped_list: list[int]) -> None:
    """
    test_swap_same_index

    from index 1 to index 1.

    Args:
        unswaped_list (list[int]): Pytest fixture.
    """
    test_list: list[int] = unswaped_list.copy()
    swap(test_list, 1, 1)
    assert test_list == [0, 1, 2, 3]


def test_sorting_algorithm_attributes() -> None:
    """
    test_sorting_algorithm_attributes
    """
    assert hasattr(ISortingAlgorithm, "sort")


def test_sorting_algorithm_sort_instantiation_error(
    unswaped_list: list[int],
) -> None:
    """
    test_sorting_algorithm_sort

    Args:
        unswaped_list (list[int]): pytest fixture
    """
    with pytest.raises(TypeError):
        ISortingAlgorithm(unswaped_list)  # type: ignore
