
class Distance:

    def __init__(self, meters=None):
        if meters is None:
            self.__meters = 0
        else:
            self.__meters = meters

    def get_meters(self):
        return self.__meters

    @property
    def in_steps(self):
        return self.__meters / 2

    @in_steps.setter
    def in_steps(self, value):
        self.__meters = value / 2

    @property
    def in_feet(self):
        return self.__meters / 0.3048

    @in_feet.setter
    def in_feet(self, value):
        self.__meters = value / 0.3048

    @property
    def in_parsecs(self):
        return self.__meters / 30856775714409184.00

    @in_parsecs.setter
    def in_parsecs(self, value):
        self.__meters = value / 30856775714409184.00


dis = Distance(1)
print("Метров {}".format(dis.get_meters()))
print("В футах это {}, шагах: {}, парсеках: {}".format(dis.in_feet, dis.in_steps, dis.in_parsecs))
print("*** Устанавливаем 100 метров в шаги ***")
dis.in_steps = 100
print("Метров {}".format(dis.get_meters()))
print("В футах это {}, шагах: {}, парсеках: {}".format(dis.in_feet, dis.in_steps, dis.in_parsecs))

