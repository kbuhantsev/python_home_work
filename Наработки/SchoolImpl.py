from Наработки.School import *

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)
print()  # печатает пустую строку
members = [t, s]
for member in members:
    member.tell()  # работает как для преподавателя, так и для студента
