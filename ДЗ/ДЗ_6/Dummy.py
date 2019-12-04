from itertools import *
import timeit


def dummy_grouper(data, n):
    groups_count = len(data) // n
    return [tuple(data[i*n:(i+1)*n]) for i in range(groups_count)]


def chunks(lst, count):
    return list(x for x in zip_longest(*[iter(lst)] * count))


def group(iterable, count):
    return zip(*[iter(iterable)] * count)


def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


if __name__ == "__main__":

    test_num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # print(dummy_grouper(range(10000000), 2))
    # print(dummy_grouper(test_num_list, 2))

    # res = list(group(range(10000000), 10))
    # res = grouper(range(10000000), 2)

    print(list(grouper(test_num_list, 3)))

    # print(timeit.timeit("chunks(range(10000000), 2)",
    #                     setup="from __main__ import chunks, test_num_list",
    #                     number=1))
    #
    # print(timeit.timeit("group(range(10000000), 2)",
    #                     setup="from __main__ import group, test_num_list",
    #                     number=1))
