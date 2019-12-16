li = list(map(int, input().split()))
sli = sorted(li)

print((sli[1] - sli[0]) + (sli[2] - sli[1]))