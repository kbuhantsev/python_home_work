
class Price:

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if 0 <= value <= 100:
            instance.__dict__[self.name] = value
        else:
            raise ValueError("Value may be from 0 to 100!")


class Book:

    price = Price()

    def __init__(self, author: str, title: str, price: int):
        self.author = author
        self.title = title
        self.price = price

    def __str__(self):
        return "{0} - {1}".format(self.author, self.title)


if __name__ == "__main__":

    book = Book("Author", "Boor", 100)
    book2 = Book("Author", "Boor", 101)
