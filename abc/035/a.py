w, h = map(int, input().split())

print("16:9" if w % 16 == 0 and h % 9 == 0 else "4:3")