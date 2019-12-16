A, B, C = map(int, input().split())

c_left = C - (A - B)

ans =  c_left if c_left >= 0 else 0
print(ans)
