class User:
    def __init__(self, first_name, last_name):
        self.user_name = first_name
        self.user_last_name = last_name

    def say_name(self):
        print("Имя пользователя: ", self.user_name)
        return self.user_name

    def say_last_name(self):
        print("Фамилия пользователя: ", self.user_last_name)
        return self.user_last_name

    def say_name_and_last_name(self):
        print("Пользователя зовут: ", self.user_name, self.user_last_name)
        return f"User: {self.user_name}, {self.user_last_name}"
