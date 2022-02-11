from dataclasses import dataclass

@dataclass
class Car:
    make:str
    model:str
    year:int

    def drive(self):
        print(f"Driving my {self.year} {self.make} {self.model}.")

    def to_string(self):
        return f'Car {self.make} {self.model} {self.year}'


corolla2015 = Car('DC_Toyota', 'Corolla', 2015)
# print(corolla2015.make)
corolla2015.drive()
# print(corolla2015.to_string()) # will this print???

Car.drive(corolla2015) #
