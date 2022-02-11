class Car:
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year

    def drive(self):
        # print(f"Driving my {self.year} {self.make} {self.model}.")
        print(f"Driving my {self.to_string()}.")

    def to_string(self):
        return f'{self.make} {self.model} {self.year}'


corolla2015 = Car('Toyota', 'Corolla', 2015)
# print(corolla2015.make)
corolla2015.drive()
# print(corolla2015.to_string()) # will this print???

Car.drive(corolla2015) #
