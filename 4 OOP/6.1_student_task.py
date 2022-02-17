"""
Create a new class called Person
private attributes: fname, lname
derived attribute: full_name

create a couple of objects of type Person
test by printing p1.full_name
"""


class Person:

    def __init__(self, first_name: str, last_name: str):
        self.__first_name = first_name
        self.__last_name = last_name

    @property
    def full_name(self):
        return f'{self.__first_name} {self.__last_name}'


newPerson = Person("Luke", "Edmunds", )

print(newPerson.full_name)
