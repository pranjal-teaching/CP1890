"""
HOW TO FRACTION MATH:
https://www.google.com/search?q=fraction+math+cheat+sheet&rlz=1C1CHBF_enCA905CA905&sxsrf=APq-WBsWoO-Yu1PH6DoKMuu6tZEONOcB5g:1645794303674&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjmwt_G9Zr2AhVcjYkEHcJVARoQ_AUoAXoECAEQAw&biw=2133&bih=1041&dpr=0.9#imgrc=ER9tlsr3eqfN2M
"""

class Fraction:
    def __init__(self, numerator: int, denominator: int):
        self.numer = numerator
        self.denom = denominator

    def __str__(self):
        return f"{self.numer}/{self.denom}"

    @property
    def to_decimal(self):
        return self.numer / self.denom

    def __add__(self, other):
        # TODO: return a new Fraction which is the sum of self and other
        pass

    def __sub__(self, other):
        # TODO
        pass

    def __mul__(self, other):
        # TODO
        pass

    def __truediv__(self, other):
        # TODO
        pass

    def __eq__(self, other):
        # TODO
        pass

    def __gt__(self, other):
        # TODO
        pass

    def __lt__(self, other):
        # TODO
        pass

    def __le__(self, other):
        # TODO: less than or equal to
        pass

    def __ge__(self, other):
        pass



half = Fraction(numerator=1, denominator=2)
two_thirds = Fraction(numerator=2, denominator=3)

print(half)  # prints 1/2
print(two_thirds)

print(half + two_thirds)
