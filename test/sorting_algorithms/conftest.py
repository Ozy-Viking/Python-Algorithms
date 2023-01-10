"""
Shared fixtures for pytest.
"""
from __future__ import annotations

from collections.abc import Callable
from typing import Any

import pytest


@pytest.fixture
def unswaped_list() -> list[int]:
    """
    unswaped_list

    Returns:
        list[int]: Pytest fixture.
    """
    return [0, 1, 2, 3]


@pytest.fixture
def unsorted_list() -> list[int]:
    """
    unsorted_list

    Returns:
        list[int]: [5, 6, 4, 2, 1, 0, 3]
    """
    return [5, 6, 4, 2, 1, 0, 3].copy()


@pytest.fixture
def sorted_list() -> list[int]:
    """
    sorted_list

    Returns:
        list[int]: [0, 1, 2, 3, 4, 5, 6]
    """
    return [0, 1, 2, 3, 4, 5, 6].copy()


@pytest.fixture
def reverse_sorted_list() -> list[int]:
    """
    reverse_sorted_list

    Returns:
        list[int]: [6, 5, 4, 3, 2, 1, 0]
    """
    return [6, 5, 4, 3, 2, 1, 0].copy()


@pytest.fixture
def unsorted_tuple_list() -> list[tuple[int, int]]:
    """
    unsorted_tuple_list

    Returns:
        list[tuple[int, int]]: [(2, 2), (3, 4), (4, 1), (1, 3)]
    """
    return [(2, 2), (3, 4), (4, 1), (1, 3)].copy()


@pytest.fixture
def sorted_tuple_list() -> list[tuple[int, int]]:
    """
    sorted_tuple_list

    Returns:
        list[tuple[int, int]]: [(4, 1), (2, 2), (1, 3), (3, 4)]
    """
    return [(4, 1), (2, 2), (1, 3), (3, 4)].copy()


@pytest.fixture
def reverse_sorted_tuple_list() -> list[tuple[int, int]]:
    """
    reverse_sorted_tuple_list

    Returns:
        list[tuple[int, int]]: [(3, 4), (1, 3), (2, 2), (4, 1)]
    """
    return [(3, 4), (1, 3), (2, 2), (4, 1)].copy()


@pytest.fixture
def test_sort_key() -> Callable[[Any], Any]:
    """
    test_sort_key

    Returns:
        Callable[[Any], Any]: lambda x: x[1]
    """
    return lambda x: x[1]


@pytest.fixture
def unsorted_str_list() -> list[str]:
    """
    unsorted_str_list

    Returns:
        list[str]: ["ab", "aaa", "aaz"]
    """
    return ["ab", "aaa", "aaz"].copy()


@pytest.fixture
def sorted_str_list() -> list[str]:
    """
    sorted_str_list

    Returns:
        list[str]: ["aaa", "aaz", "ab"]
    """
    return ["aaa", "aaz", "ab"].copy()


@pytest.fixture
def reverse_sorted_str_list() -> list[str]:
    """
    reverse_sorted_str_list

    Returns:
        list[str]: ['ab', 'aaz', 'aaa']
    """
    return ["ab", "aaz", "aaa"].copy()
