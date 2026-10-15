num = int(input())
a = num%10
b = num%100//10
c = num%1000//100
d = num//1000
if a==b and c==d or a==d and b==c or a==b==c==d:
    print('Настоящее')
else: print('Кривое')