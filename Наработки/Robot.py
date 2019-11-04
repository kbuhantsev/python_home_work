class Robot:
    """Представляет робота с именем."""

    # Переменная класса, содержащая количество роботов
    population = 0

    def __init__(self, name):
        """Инициализация данных."""
        self.name = name
        print('(Инициализация {0})'.format(self.name))
        # При создании этой личности, робот добавляется
        # к переменной 'population'
        Robot.population += 1

    def __del__(self):
        """Я умираю."""
        print('{0} уничтожается!'.format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print('{0} был последним.'.format(self.name))
        else:
            print('Осталось {0:d} работающих роботов.'.format(Robot.population))

    def sayHi(self):
        """Приветствие робота.
        Да, они это могут."""
        print('Приветствую! Мои хозяева называют меня {0}.'.format(self.name))

    @staticmethod
    def howMany():
        """Выводит численность роботов."""
        print('У нас {0:d} роботов.'.format(Robot.population))
