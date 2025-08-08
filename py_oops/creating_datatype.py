class fraction:
    def __init__(self,n,d):
        self.num=n
        self.den=d

    def __str__(self):
        return f'{self.num}/{self.den}'


    def __add__(self, other):
        num=self.num*other.den + other.num*self.den
        den=self.den * other.den
        return  f'{num}/{den}'

    def __truediv__(self, other):
        num=self.num*other.den
        den=self.den*other.num
        return f'{num}/{den}'

    def __mul__(self, other):
        num=self.num*other.num
        den=self.den * other.den
        return  f'{num}/{den}'

    def __sub__(self, other):
        num = self.num * other.den - other.num * self.den
        den = self.den * other.den
        return f'{num}/{den}'



x=fraction(1,1)
y=fraction(1,1)
print(x)
print(y)
print(x+y)
print(x/y)
print(x*y)
print(x-y)