n = int(input())
s = [input() for _ in range(n)]

print(max(s, key=s.count))

# import collections
# c = collections.Counter(s)
# print(c.most_common()[0][0])