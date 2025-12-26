import sys

data = sys.stdin.read().split()
idx = 0

s = int(data[idx]); idx += 1
n = int(data[idx]); idx += 1

dragons = []

for _ in range(n):
    x = int(data[idx]); idx += 1
    y = int(data[idx]); idx += 1
    dragons.append((x, y))

# fight weakest dragons first
dragons.sort()

for x, y in dragons:
    if s > x:
        s += y
    else:
        print("NO")
        break
else:
    print("YES")
