class Dog:
    def __init__(self, name: str, age: int, tricks: list = []):
        self.name = name
        self.age = age
        self.tricks = tricks

    def bark(self):
        print('🐕 Woof woof')

    def train(self, new_trick):
        print(f'Teaching {self.name} how to {new_trick}')
        self.tricks.append(new_trick)


class Person:
    def __init__(self, name: str, age: int, pet: Dog):
        self.name = name
        self.age = age
        self.pet = pet

    def walk_dog(self):
        print(f'Walking {self.pet.name}') # Walking Oliver

oliver = Dog('Oliver', 2)
oliver.bark()
oliver.train('Sit')
oliver.train('Come Here')

pranjal = Person('Pranjal', 35, oliver)
pranjal.walk_dog()