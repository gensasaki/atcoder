n = int(input())

a, b, c = 0, 0, 1
for _ in range(n - 3):
    a, b, c = b, c, (a + b + c) % 10007

print(c if n >= 3 else 0)