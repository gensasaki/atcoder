a, b, c, k = map(int, input().split())
s, t = map(int, input().split())

T = a * s + b * t

if s + t >= k:
    T -= (s + t) * c
print(T)