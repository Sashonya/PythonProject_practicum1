a, b, c = map(int, input().split())
if a>b and a>c:
    print(a)
elif b>c and b>a:
    print(b)
elif c>a and c>b:
    print(c)
elif a==b and a>c:
    print(a)
elif a==c and a>b:
    print(a)
elif c==b and a<c:
    print(c)
else: print(a)