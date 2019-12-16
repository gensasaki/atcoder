l = []

for i in range(4+1):
    l.append(int(input()))

k = int(input())

ans = "Yay!"

for elm1 in l:
    for elm2 in l:
        if elm2 - elm1 > k:
            ans = ":("

print(ans) 