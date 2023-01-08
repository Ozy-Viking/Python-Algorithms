from sorting_algorithms import swap, SortingAlgorithm
from test import *


@pytest.fixture
def unswaped_list() -> list[int]:
    return [0, 1, 2, 3]


def test_swap_01(unswaped_list: list[int]) -> None:
    test_list = unswaped_list.copy()
    swap(test_list, 0, 1)
    assert test_list == [1, 0, 2, 3]


def test_swap_n10(unswaped_list: list[int]) -> None:
    test_list = unswaped_list.copy()
    swap(test_list, -1, 0)
    assert test_list == [3, 0, 1, 2]


def test_swap_21(unswaped_list: list[int]) -> None:
    test_list = unswaped_list.copy()
    swap(test_list, 2, 1)
    assert test_list == [0, 2, 1, 3]


def test_swap_same_index(unswaped_list: list[int]) -> None:
    test_list = unswaped_list.copy()
    swap(test_list, 1, 1)
    assert test_list == [0, 1, 2, 3]


def test_sorting_algorithm() -> None:
    assert hasattr(SortingAlgorithm,'sort')
    
def test_sorting_algorithm_sort(unswaped_list: list[int]) -> None:
    with pytest.raises(TypeError):
        SortingAlgorithm(unswaped_list)
