import sys 
data = sys.stdin.read().strip().split()
n = int(data[0])
if len(set(data[1].lower()))==26:
    print("YES")
else:
    print("NO")