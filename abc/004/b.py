c = [list(input().split()) for _ in range(4)]

for col in c[::-1]:
    print(*col[::-1])