n = int(input())
a = int(input())

while n >= 500:
    n -= 500
    
print("Yes" if a >= n else "No")