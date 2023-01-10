"""
Testing for List class
"""
import pytest

from python_algorithms.basic_python_recreations import List


@pytest.mark.skip
@pytest.mark.xfail
def test_dir_list() -> None:
    """
    test_dir_list
    """
    assert set(dir(List)) == set(dir(list))


@pytest.mark.skip
def test_list_creation_and_equality(test_list: list[int]) -> None:
    """
    test_list_creation_and_equality

    Args:
        test_list (list[int]): test fixture.
    """
    assert List(test_list) == [0, 1, 2, 3, 4]


@pytest.mark.skip
def test_list_get_item(test_list: list[int]) -> None:
    """
    test_list_get_item

    Args:
        test_list (list[int]): test fixture.
    """
    assert List(test_list)[0] == 0


@pytest.mark.skip
def test_list_len_call(test_list: list[int]) -> None:
    """
    test_list_len_call

    Args:
        test_list (list[int]): test fixture.
    """
    assert len(List(test_list)) == len(test_list)


@pytest.mark.skip
def test_list_slicing(test_list: list[int]) -> None:
    """
    test_list_slicing

    Args:
        test_list (list[int]): test fixture.
    """
    assert List(test_list)[:2] == [0, 1, 2]


@pytest.mark.skip
def test_list_repr(test_list: list[int]) -> None:
    """
    test_list_repr

    Args:
        test_list (list[int]): test fixture.
    """
    assert repr(List(test_list)) == repr(test_list)
