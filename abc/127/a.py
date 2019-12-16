A, B = map(int, input().split())
ans = 0

if A >= 13:
    ans = B
elif A <= 5:
    ans = 0
else:
    ans = int(B / 2)

print(ans)