class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Fraction):
            x_n = self.denominator * other.numerator
            y_n = other.denominator * self.numerator
            denominator = other.denominator * self.denominator
            return Fraction(x_n + y_n, denominator)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Fraction):
            x_n = self.denominator * other.numerator
            y_n = other.denominator * self.numerator
            denominator = other.denominator * self.denominator
            return Fraction(y_n - x_n, denominator)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator == self.denominator * other.numerator
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator > self.denominator * other.numerator
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return not self > other
        return NotImplemented

    def __str__(self):
        return f"Fraction: {self.numerator}, {self.denominator}"


f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print('OK')
