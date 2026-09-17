import math

n = float(input())
min = 2*n
h = min//60
min = min%60
min = math.floor(min)
print(h, min)