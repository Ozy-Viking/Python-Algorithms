from random import Random

from sorting_algorithms import *


# my_list = list(range(10))
# ic(my_list[1::-1])
# my_list.reverse()
# Random(1).shuffle(my_list)
my_list = [(2, 2), (3, 4), (4, 1), (1, 3)]
sort_algo = MergeSort(my_list)
# ic(sort_algo.sorting_list)
sort_algo = sort_algo.sort(key=lambda x: x[1])
# sorted = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
sorted = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ic(sort_algo.sorting_list == sorted)
ic(sort_algo.sorting_list)

str_list = [
    "ab",
    "aaa",
    "aaz",
]
str_list.sort(reverse=True)
ic(str_list)
