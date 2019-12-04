from functools import partial


class MyClassMethod:

    def __init__(self, function):
        self.function = function

    def __get__(self, instance, owner):
        if owner is None:
            owner = type(instance)

        return partial(self.function, owner)


class MyClass:

    @MyClassMethod
    def method(self, *args):
        print('{} class method. {}'.format(self.__name__, args))

    def call_class_method(self):
        self.method(10)


if __name__ == "__main__":

    MyClass.method(10, "", {"abra", })
    MyClass().method(20)
