class ImperialLength:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __str__(self):
        return f'{self.feet}ft {self.inches}in'

    def __add__(self, other):
        total_feet = 0
        total_inches = self.inches + other.inches
        if total_inches > 12:
            total_feet += 1
            total_inches -= 12
        total_feet += self.feet + other.feet
        return ImperialLength(feet=total_feet, inches=total_inches)

    def __sub__(self, other):
        # supports l1 - l2
        pass

    def __gt__(self, other):
        self_total_inches = self.feet * 12 + self.inches
        other_total_inches = other.feet * 12 + other.inches
        # if self_total_inches > other_total_inches:
        #     return True
        # else:
        #     return False
        return self_total_inches > other_total_inches

    def __lt__(self, other):
        self_total_inches = self.feet * 12 + self.inches
        other_total_inches = other.feet * 12 + other.inches
        return self_total_inches < other_total_inches

    def __eq__(self, other):
        self_total_inches = self.feet * 12 + self.inches
        other_total_inches = other.feet * 12 + other.inches
        return self_total_inches == other_total_inches


moms_height = ImperialLength(feet=5, inches=6)
kid_height = ImperialLength(feet=5, inches=6)

print(moms_height)

print(moms_height + kid_height)

# kid_height + moms_height
if moms_height > kid_height:
    print('Mom is taller')
elif moms_height < kid_height:
    print('Now the kid is taller')
else:
    print('Wow, both are equal!')

print(moms_height == kid_height)
