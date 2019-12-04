class Celsius:

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = (value - 32) / 1.8


class Temperature:
    celsius = Celsius()

    def __init__(self, initial: float):
        self.fahrenheit = initial
        self.celsius = initial

    def __str__(self):
        return "F: {}, C: {}".format(self.fahrenheit, self.celsius)


if __name__ == "__main__":

    temp = Temperature(100)
    print(temp)
