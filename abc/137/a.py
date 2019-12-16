A, B = map(int, input().split())

a = A + B
s = A - B
m = A * B

print(max(a, s, m))