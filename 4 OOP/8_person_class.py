# Create a new class level variable called person_counter
# Create a property called person_id and return a unique ID for each person object

class Person:

    def __init__(self, first_name: str, last_name: str):
        self.__first_name = first_name
        self.__last_name = last_name

    @property
    def full_name(self):
        return f'{self.__first_name} {self.__last_name}'


newPerson = Person("Luke", "Edmunds", )


print(newPerson.full_name)
print(newPerson.id) # should print unique ID
# try creating new person objects and print their IDs