import sys

data = sys.stdin.read().strip().split()
idx = 0
t = int(data[idx]); idx += 1

for _ in range(t):
    n = int(data[idx]); idx += 1
    arr = list(map(int, data[idx:idx+n]))
    idx += n


    if all(x == 1 for x in arr):
        print("Alice")
    elif arr[0] == 0 and arr[-1] == 0:
        print("Bob")
    else:
        print("Alice")
