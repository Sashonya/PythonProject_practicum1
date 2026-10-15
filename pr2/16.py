

a = input()
b = int(a)
if len(a)==4 and a[0] != a[1] and a[0] != a[2] and a[0] != a[3] and \
a[1] != a[2] and a[1] != a[3] and \
a[2] != a[3] and (b<=1900 or b>=2050):
    print('ОК')
else: print('Error')