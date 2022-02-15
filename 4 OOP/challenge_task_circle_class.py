# Create a circle class
# Data attributes: radius <- private
# property called radius which returns current radius
# setter called radius which allows you to set a radius > 0
# method get_area

class Circle:
    def __init__(self, radius: float):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, new_radius):
        assert new_radius > 0, 'Radius must be greater than 0'
        self.__radius = new_radius

    def get_area(self):
        return 3.14 * pow(self.radius, 2)

    def get_circumference(self):
        return 2 * 3.14 * self.radius


circle = Circle(125.0)
print(circle.get_area())
print(circle.get_circumference())
print(f'Accessing Radius: {circle.radius}')
circle.radius = 5.0
print(f'Accessing Radius: {circle.radius}')
circle.radius = -3
print(f'Accessing Radius: {circle.radius}')