from datetime import date


class UserAccount:
    def __init__(self, user_name, email, password, date_of_birth):
        self.__user_name = user_name
        self.__email = email
        self.__password = password
        self.__dob = date_of_birth




aaron = UserAccount(user_name="Aaron Russel",
                    email="aaron.russel@gmail.com",
                    password="nunyabusiness",
                    date_of_birth=date(year=1997, month=6, day=29))

print(aaron.user_name)