# Calkin-Wilf tree 1
from fractions import Fraction  
t = int(input())
for _ in range(1, t+1):
    tree = input()
    a, b = 1, 1
    for i in tree:
        if i == 'L':
            a, b = a, a+b
        else:
            a, b = a+b, b
    irr = Fraction(a, b)
    print(f"#{_} {irr.numerator} {irr.denominator}")
