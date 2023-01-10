"""
Shared fixtures for pytest.
"""
import pytest


@pytest.fixture
def test_list() -> list[int]:
    """
    test_list fixture

    Returns:
        list[int]: [0, 1, 2, 3, 4]
    """
    return [0, 1, 2, 3, 4].copy()
