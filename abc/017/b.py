x = input()

ans = "YES"

for idx, c in enumerate(x):
    if c in "oku":
        continue
    elif c == "c" and x[idx+1] == "h":
        continue
    elif c == "h" and x[idx-1] == "c":
        continue
    else:
        ans = "NO"
        break

print(ans)