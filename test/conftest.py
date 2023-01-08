from test import *


@pytest.fixture
def unsorted_list() -> list[int]:
    return [5, 6, 4, 2, 1, 0, 3].copy()


@pytest.fixture
def sorted_list() -> list[int]:
    return [0, 1, 2, 3, 4, 5, 6].copy()


@pytest.fixture
def reverse_sorted_list() -> list[int]:
    return [6, 5, 4, 3, 2, 1, 0].copy()


@pytest.fixture
def unsorted_tuple_list() -> list[tuple[int, int]]:
    return [(2, 2), (3, 4), (4, 1), (1, 3)].copy()


@pytest.fixture
def sorted_tuple_list() -> list[tuple[int, int]]:
    return [(4, 1), (2, 2), (1, 3), (3, 4)].copy()


@pytest.fixture
def reverse_sorted_tuple_list() -> list[tuple[int, int]]:
    return [(3, 4), (1, 3), (2, 2), (4, 1)].copy()


@pytest.fixture
def test_sort_key() -> Callable[[Any], Any]:
    return lambda x: x[1]


@pytest.fixture
def unsorted_str_list() -> list[str]:
    return ["ab", "aaa", "aaz"].copy()


@pytest.fixture
def sorted_str_list() -> list[str]:
    return ["aaa", "aaz", "ab"].copy()


@pytest.fixture
def reverse_sorted_str_list() -> list[str]:
    return ['ab', 'aaz', 'aaa'].copy()


