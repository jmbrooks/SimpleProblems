from math import gcd


def greatest_common_divisor(, denominator):
    """Find greatest common factor using Euclidean algorithm."""
    return gcd(numerator, denominator)


class Fraction():
    """Fraction object."""
    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator
    
    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)

    def __add__(self, fraction):
        # return ((self.numerator * fraction.denominator) + (fraction.numerator * self.denominator)) / (self.denominator * fraction.denominator)
        numerator = (self.numerator * fraction.denominator) + (fraction.numerator * self.denominator)
        denominator = self.denominator * fraction.denominator
        gcd = greatest_common_divisor(numerator, denominator)
        new_numerator = int(numerator / gcd)
        new_denominator = int(denominator / gcd)
        return Fraction(new_numerator, new_denominator)

    def evaluate_fraction(self):
        return self.numerator / self.denominator
    

fraction_one = Fraction(5, 7)
fraction_two = Fraction(2, 7)

fraction_three = Fraction(5, 11)

print(fraction_one)
print(fraction_one.evaluate_fraction())
print(fraction_one)
print('fraction', fraction_one, "is cool")

print(fraction_one + fraction_two)

print(fraction_one + fraction_three)
