li = list(int(input()) for i in range(3))
a, b, n = li[0], li[1], li[2]
ans = 0

while n % a != 0 or n % b != 0:
    n += 1
print(n)