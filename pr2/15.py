n, k, m = map(int, input().split())
if m == k:
    print('Никуда ехать не надо')
elif abs(k-m) <= n/2:
    print(abs(k-m)-1)
elif abs(k-m) > n/2:
    if m<k: print(n-k+m-1)
    elif m>k: print(n-m+k-1)

