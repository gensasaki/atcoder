N = int(input())
S = input()
ans = ""
a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(len(S)):
    if a.index(S[i]) + N > 25:
        ans += a[a.index(S[i]) + N - 26]
    else:
        ans += a[a.index(S[i]) + N]

print(ans)
