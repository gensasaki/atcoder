A, P = map(int, input().split())

a_parts = (3 * A) + P
ap = a_parts // 2 if a_parts // 2 else 0

print(ap)