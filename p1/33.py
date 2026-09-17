n = int(input())
c = int(input())
a = int(input())

if a%(n*c)==0:
    page = (a // (n * c))
else: page = (a//(n*c))+1

if (a - ((page-1)*c*n))%n == 0:
    stolb = ((a - ((page - 1) * c * n)) // n)
else: stolb = ((a - ((page - 1) * c * n)) // n) +1


stroka = (a - (page*c*n))%n
if stroka == 0:
    stroka=n
else: stroka = (a - (page*c*n))%n

print ( f'Страница {page}, столбец, {stolb}, строка, {stroka}')
#можно сделать короче с помощью math.ceil