my_list = [0, 1, 2, 3, 4, 5, 6]
my_list2 = [0, 1, 2, 3, 4]
my_list3 = "1234"


#print(tuple(map(lambda *args: args, my_list, my_list2, my_list3)))


def zipperMap(*args):

    return tuple(map(lambda *args_local: args_local, *args))


print(zipperMap(my_list, my_list2, my_list3))


def zipper(*args):

    args_list = list(args)
    if not len(args_list):
        return ()

    result_list = []
    min_len = len(sorted(args_list, key=len)[0])
    i = 0
    while i < min_len:
        list_tuple = []
        j = 0
        while j < len(args_list):
            list_tuple.append(args_list[j][i])
            j += 1
        result_list.append(tuple(list_tuple))
        i += 1
    return tuple(result_list)
#
#
# print(zipper(my_list, my_list2, my_list3))
