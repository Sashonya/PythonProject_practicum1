
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if ((min(c, d) <= min(a, b) and max(c, d) <= max(a, b)) or
    (min(c, e) <= min(a, b) and max(c, e) <= max(a, b)) or
    (min(d, e) <= min(a, b) and max(d, e) <= max(a, b))):
    print("да")
else:
    print("нет")