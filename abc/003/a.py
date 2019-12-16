n = int(input())
t = 0

for i in range(n+1):
    t += i * 10000

print(int(t / n))