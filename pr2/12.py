a = int(input())
if a == 11 or a == 12 or a == 13 or a == 14:
    print(f'{a} попугаев')
elif 2<=a%10<=4:
    print(f'{a} попугая')
elif a%10==1:
    print(f'{a} попугай')
else: print(f'{a} попугев')