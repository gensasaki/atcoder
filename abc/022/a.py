n, s, t = list(map(int, input().split()))
w = int(input())
if s <= w <= t:
    c = 1
else:
    c = 0

for _ in range(n - 1):
    w += int(input())
    if s <= w <= t:
        c += 1

print(c)