firstList = [1, 2, 3, [4, 5, 6, [7, 8, 9]], 10]


def flatten(input_list):
    flatten_list = []
    for i in input_list:
        if isinstance(i, list):
            flatten_list = flatten_list + flatten(i)
        else:
            flatten_list.append(i)
    return flatten_list


def flattenBest(inputlist=[]):
    input_list = inputlist[:]
    flatten_list = []
    while len(input_list):
        first = input_list.pop(0)
        if isinstance(first, list):
            input_list = first + input_list
        else:
            flatten_list.append(first)
    return flatten_list


print(flatten(firstList))
print(flattenBest(firstList))
