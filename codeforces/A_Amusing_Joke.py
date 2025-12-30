a = input().strip()
b = input().strip()
c = input().strip()

if sorted(a + b) == sorted(c):
    print("YES")
else:
    print("NO")
