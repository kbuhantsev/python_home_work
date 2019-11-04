class SchoolMember:
    """Представляет любого человека в школе."""

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Создан SchoolMember: {0})'.format(self.name))

    def tell(self):
        """Вывести информацию."""
        print('Имя:"{0}" Возраст:"{1}"'.format(self.name, self.age), end=" ")


class Teacher(SchoolMember):
    """Представляет преподавателя."""

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Создан Teacher: {0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Зарплата: "{0:d}"'.format(self.salary))


class Student(SchoolMember):
    """Представляет студента."""

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Создан Student: {0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Оценки: "{0:d}"'.format(self.marks))
