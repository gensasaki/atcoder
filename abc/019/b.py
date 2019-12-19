from itertools import groupby

s = input()

g = groupby(s)
ans = ""

for k, v in g:
    ans += (k + str(len(list(v))))

print(ans)