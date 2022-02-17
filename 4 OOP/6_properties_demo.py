from datetime import date


class UserAccount:
    user_count = 0

    def __init__(self, user_name, email, password, date_of_birth):
        self.__user_name = user_name
        self.__email = email
        self.__password = password
        self.__dob = date_of_birth
        UserAccount.user_count += 1
        self.__user_id = f'USER_{UserAccount.user_count}'

    @property  # getter
    def uname(self):
        return self.__user_name

    @uname.setter
    def uname(self, new_user_name):
        self.__user_name = new_user_name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_email_address):
        assert isinstance(new_email_address, str), "Must be a str"
        assert '@' in new_email_address, "Must be a valid email address"
        self.__email = new_email_address


    def pword(self, new_password):
        assert isinstance(new_password, str), "Must be a string"
        digit_counter = 0
        for char in new_password:
            if char in '0123456789':
                digit_counter += 1
        assert digit_counter >= 2, "Must contain atleast 2 numbers"
        assert len(new_password) >= 8, 'Must be atleast 8 chars long'
        self.__password = new_password

    @property
    def age(self):
        return int((date.today() - self.__dob).days // 365.25)

    @property
    def user_id(self):
        return self.__user_id


aaron = UserAccount(user_name="Aaron Russel",
                    email="aaron.russel@gmail.com",
                    password="nunyabusiness",
                    date_of_birth=date(year=1997, month=6, day=29))

aaron2 = UserAccount(user_name="Aaron Russel",
                     email="aaron.russel@gmail.com",
                     password="nunyabusiness",
                     date_of_birth=date(year=1997, month=6, day=29))

print(aaron.uname)
aaron.uname = "aaron_r"
print(aaron.uname)

print(aaron.age)

print(aaron.user_id)
print(aaron2.user_id)
