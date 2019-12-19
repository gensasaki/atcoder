n = int(input())
a = list(map(int, input().split()))
c = 0

for i in a:
    if i in (4, 5, 6):
        c += (i - 3)
    elif i % 2 == 0:
        c += 1
        
print(c)