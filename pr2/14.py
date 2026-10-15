a = int(input())
gal = a//493
sikl = (a%493)//17
kv = (a%493)%17

if gal == 0:
    print(sikl, 'сиклей')
    print(kv, 'кнатов')
elif sikl == 0:
    print(gal, 'галлеонов')
    print(kv, 'кнатов')
elif kv == 0:
    print(gal, 'галлеонов')
    print(sikl, 'сиклей')
elif gal ==0 and sikl == 0:
    print(kv, 'кнатов')
elif sikl == 0 and kv==0:
    print(gal, 'галлеонов')
elif gal == 0 and kv == 0:
    print(sikl, 'сиклей')
elif gal == 0 and sikl == 0 and kv == 0:
    print("У вас нет денег")
else:
    print(gal, 'галлеонов')
    print(sikl, 'сиклей')
    print(kv, 'кнатов')
