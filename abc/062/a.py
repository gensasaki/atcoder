x, y = map(int, input().split())
g = "acababaababa"

print("Yes" if g[x - 1] == g[y - 1] else "No")