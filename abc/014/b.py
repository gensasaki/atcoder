n, x = map(int, input().split())
a = list(map(int, input().split()))

bx = bin(x)[::-1]
ans = 0

for i in range(n):
    if ((x >> i) & 1): ans += a[i]
    
print(ans)