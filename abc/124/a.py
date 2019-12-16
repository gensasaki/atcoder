a, b = map(int, input().split())

if a == b:
    print(2 * a)
else:
    m = max(a, b)
    print(m + m-1)