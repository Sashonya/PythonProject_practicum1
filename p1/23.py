a = int(input())
mi = a//60
s = a%60
h = mi//60
mi = mi%60
d = h//24
print ( h,"часов", mi,"минут", s,"секунд")