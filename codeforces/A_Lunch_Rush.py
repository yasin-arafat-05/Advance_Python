import sys

data = sys.stdin.read().split()
idx = 0

n = int(data[idx]); idx += 1
k = int(data[idx]); idx += 1

m = -10**18  

for _ in range(n):
    f = int(data[idx]); idx += 1
    t = int(data[idx]); idx += 1

    if t > k:
        joy = f - (t - k)
    else:
        joy = f

    m = max(m, joy)

print(m)
