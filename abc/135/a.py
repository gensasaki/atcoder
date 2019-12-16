A, B = map(int, input().split())
K = (A + B) / 2
ans = int(K) if (A + B) % 2 == 0 else "IMPOSSIBLE"
print(ans)