import math


def isPrime(n):
    if (n < 2): return 0
    for i in range(2, (n // 2)+1):
        if (n % i == 0): return 0
    return 1
for t in range (int(input())):
    n = int(input())
    k = 0
    for i in range (1, n):
        if (math.gcd(i, n) == 1):
            k += 1
    if isPrime(k): print("YES")
    else: print("NO")
