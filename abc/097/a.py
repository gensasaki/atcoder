a, b, c, d = map(int, input().split())

print("Yes" if abs(b - a) <= d and abs(c - b) <= d else "No")