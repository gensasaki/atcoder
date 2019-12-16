s = [int(input()) for i in range(3)]

s_s = sorted(s, reverse=True)

for elm in s:
    print(s_s.index(elm) + 1)