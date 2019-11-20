class BaseUser:
    def __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = int(age)

    def get_name(self):
        return "{} {}".format(self.first_name, self.last_name)


class User(BaseUser):
    def __init__(self, *args):
        self.friends = {}
        self.memory = []
        self.age_check = 50
        super().__init__(*args)

    def check_user(self, user):
        error_msg = "{} age diff is more than {} years"
        if not abs(self.age - user.age) <= self.age_check:
            raise ValueError(error_msg.format(user.get_name(),
                                              self.age_check))

    def say_hello_to(self, user):
        self.check_user(user)
        user_name = user.get_name()

        if not self.friends.get(user_name):
            self.friends[user_name] = user
            self.memory.append(user)
            user.say_hello_to(self)

    @property
    def friends_in_memory(self):

        if 25 < self.age < 50:  # пять последних
            return self.memory[-5:]
        elif 50 < self.age < 75:  # два последних
            return self.memory[-2:]
        elif 75 < self.age:  # никого не помнит :)
            return []
        else:
            return self.memory

    def __repr__(self):
        spec_str = "{}: {} {}, gender: {}, age: {}"
        return spec_str.format(self.__class__.__name__,
                               self.first_name,
                               self.last_name,
                               self.gender,
                               self.age)


class GenerateOperationsMixin:

    def get_test_names(self):

        return [["Carl", "Carlson", "male", 25],
                ["John", "Doe", "male", 35],
                ["Bruce", "Wayne", "male", 45],
                ["Jackie", "Chan", "male", 55],
                ["Bruce", "Willis", "male", 65],
                ["Pierre", "Richard", "male", 75]]

    def generate_test_users(self):

        for array in self.get_test_names():
            self.create_user(*array)


class Admin(GenerateOperationsMixin, User):
    _created_users = {}

    def __init__(self, first_name, last_name, position):
        self.position = position
        super().__init__(first_name, last_name, "", 0)
        pass

    def create_user(self, *args):

        user = User(*args)
        self._created_users[user.get_name()] = user

    def get_user(self, username):
        return self._created_users[username]

    def get_created_users(self):
        return self._created_users.values()


admin = Admin("internal", "user", "admin")
admin.generate_test_users()

carl = admin.get_user("Carl Carlson")
john = admin.get_user("John Doe")
bruce = admin.get_user("Bruce Wayne")
jackie = admin.get_user("Jackie Chan")
bruce_willis = admin.get_user("Bruce Willis")
pierre = admin.get_user("Pierre Richard")

bruce_willis.say_hello_to(jackie)
bruce_willis.say_hello_to(pierre)
bruce_willis.say_hello_to(bruce)
print(bruce_willis.friends_in_memory)
