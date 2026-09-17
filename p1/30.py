ATT = float(input())
COMP = float(input())
YDS = float(input())
TD = float(input())
INT = float(input())
a = ((COMP / ATT) - 0.3) * 5
b = ((YDS / ATT) - 3) * 0.25
c = (TD / ATT) * 20
d = 2.375 - ((INT / ATT) * 25)

a = max(0,min(a, 2.375))
b = max(0,min(b, 2.375))
c = max(0,min(c, 2.375))
d = max(0,min(d, 2.375))

rating = ((a + b + c + d) / 6) * 100
print(rating)
