s = input()
n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]

for elm in l:
    l = elm[0]
    r = elm[1]
    s = s[:l-1] + s[l-1:r][::-1] + s[r:]

print(s)