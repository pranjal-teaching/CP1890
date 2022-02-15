class Dog:
    def __init__(self, name: str, age: int, tricks: list = []):
        self.name = name
        self.__age = age  # Private Variable
        self.tricks = tricks

    @property
    def dog_age(self):
        return self.__age

    @dog_age.setter
    def dog_age(self, new_age):
        assert new_age > self.dog_age, 'New age must be greater than current age'
        self.__age = new_age

    def bark(self):
        print('🐕 Woof woof')

    def train(self, new_trick):
        print(f'Teaching {self.name} how to {new_trick}')
        self.tricks.append(new_trick)


oliver = Dog('Oliver', 2)
print(f'Accessing Name: {oliver.name}') # Accessing Name: Oliver
print(f'Accessing Age: {oliver.dog_age}') # AttributeError: 'Dog' object has no attribute '__age'
oliver.dog_age = 1
print(f'Accessing Age: {oliver.dog_age}') # AttributeError: 'Dog' object has no attribute '__age'