from dataclasses import dataclass

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + ": " + str(self.age)

#P1 = Person("Albert",40)
#print(P1)


@dataclass
class DataCPerson:
    name: str
    age: int



DCP1 = DataCPerson("Todd",23)
print(DCP1)
print(DCP1.name)