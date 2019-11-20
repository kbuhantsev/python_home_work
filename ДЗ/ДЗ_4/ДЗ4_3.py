import functools


def comparable(cls):

    def get_hash_sum(obj):
        return functools.reduce(lambda x, y: hash(x) + hash(y), obj.__dict__.values())

    @functools.wraps(cls.__eq__)
    def new_eq(self, other):
        return get_hash_sum(self) == get_hash_sum(other)

    @functools.wraps(cls.__ne__)
    def new_ne(self, other):
        return get_hash_sum(self) != get_hash_sum(other)

    @functools.wraps(cls.__lt__)
    def new_lt(self, other):
        return get_hash_sum(self) < get_hash_sum(other)

    @functools.wraps(cls.__gt__)
    def new_gt(self, other):
        return get_hash_sum(self) > get_hash_sum(other)

    cls.__eq__ = new_eq
    cls.__ne__ = new_ne
    cls.__lt__ = new_lt
    cls.__gt__ = new_gt

    return cls


@comparable
class Worker:

    def __init__(self, age: int, salary: int, gender: str):
        self.age = age
        self.salary = salary
        self.gender = gender


w1 = Worker(25, 1000, "male")
w2 = Worker(30, 2000, "female")

print(w1 != w2)
print(w1 == w2)
print(w1 > w2)
print(w1 < w2)
