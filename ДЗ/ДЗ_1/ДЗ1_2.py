my_list = [0, 1, 2, 3, 4, 5, 6]
my_tuple = (0, 1, 2, 3, 4, 5, 6)
my_range = range(10)


def take(n, iterable):
    if hasattr(iterable, '__iter__'):
        try:
            return iterable[:n]
        except IndexError:
            return None
    else:
        print(str(type(iterable)) + " is not iterable!")
        return None


print(take(5, my_list))
print(take(5, my_tuple))
print(take(5, list(my_range)))
print(take(5, 23))
print(take(5, "34321434"))
