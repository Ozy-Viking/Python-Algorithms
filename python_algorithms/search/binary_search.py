"""
binary_search.py



Author: Zack Hankin
Started: 23/02/2023
"""
from __future__ import annotations

import random
import time
from collections import defaultdict

from icecream import ic


def binary_search(ordered_list, target) -> int | bool:
    max_length = len(ordered_list)
    search_idx: int = int(max_length // 2)
    top_offset: int = max_length
    bottom_offset: int = 0
    while top_offset != bottom_offset:
        search_value = ordered_list[search_idx]
        if search_value == target:
            return search_idx

        if target < search_value:
            top_offset = search_idx
            search_idx -= int((search_idx - bottom_offset) / 2)

        elif target > search_value:
            bottom_offset = search_idx
            search_idx += round((top_offset - search_idx) / 2)

    else:
        return False


def main() -> int:
    t0 = time.perf_counter_ns()
    max = 50_000
    l = list(range(max + 1))
    t = random.randint(0, max)
    result = binary_search(l, t)
    t1 = time.perf_counter_ns()
    correct = defaultdict(int)
    correct["incorrect_value"] = list()
    # ic(binary_search(l, t))
    # ic(f"Time: {(t1 - t0) / (10 ** 6):,.2f} ms")
    for num in l:
        tmp = binary_search(l, num)
        if tmp == num:
            correct["Correct"] += 1
        else:
            correct["Incorrect"] += 1
            correct["incorrect_value"].append((num, tmp))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
