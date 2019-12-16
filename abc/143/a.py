A, B = map(int, input().split())

ans = A - 2*B if 2*B < A else 0
print(ans)