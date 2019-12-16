from functools import lru_cache

n = int(input())

@lru_cache(maxsize=None)
def tri(n):
    a, b, c, d = 0, 0, 1, 0
    if n <= 2:
        return 0
    elif n == 3:
        return 1
    else:
        for _ in range(n - 3):
            d = (a + b + c) % 10007
            a, b, c = b, c, d
        return d
 
print(tri(n))