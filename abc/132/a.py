S = input()
d = {}

for c in S:
    if c in d:
        d[c] += 1
    else:
        d[c] = 1

v = list(d.values())

ans = "Yes" if len(d) == 2 and v[0] == v[1] else "No" 
print(ans)