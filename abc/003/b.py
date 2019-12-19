s = input()
t = input()
c = "atcoder"

for cs, ct in zip(s, t):
    if cs == ct:
        continue
    elif (cs == "@" and ct in c) or (ct == "@" and cs in c):
        continue
    else:
        print("You will lose")
        break
else:
    print("You can win")