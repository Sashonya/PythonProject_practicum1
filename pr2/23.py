n = int(input())

if n <= 10:
    print(n - 1)

elif n <= 190:
    x = (n - 11) // 2 + 10
    p = (n - 11) % 2

    if p == 0:
        print(x // 10)
    else:
        print(x % 10)