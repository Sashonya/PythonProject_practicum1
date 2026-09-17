import math
m = float(input())
n = float(input())
k = float(input())


c = math.degrees( math.acos((m**2+n**2-k**2)/(2*m*n)))
a = math.degrees( math.acos((m**2+k**2-n**2)/(2*m*k)))
b = math.degrees( math.acos((n**2+k**2-m**2)/(2*n*k)))
print(c)
print(a)
print(b)
