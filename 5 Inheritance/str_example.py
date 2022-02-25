class Hero:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'I am a Hero. My name is {self.name}.'


superman = Hero(name="Superman")
print(superman)