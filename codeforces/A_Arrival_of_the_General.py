import sys 

data = sys.stdin.read().strip().split()
n = int(data[0])
arr = list(map(int, data[1:]))

max_value = max(arr)
min_value = min(arr)

# first max
for i in range(n):
    if arr[i] == max_value:
        max_idx = i
        break

# last min
for i in range(n-1, -1, -1):
    if arr[i] == min_value:
        min_idx = i
        break

ans = max_idx + (n - 1 - min_idx)

# overlap case
if max_idx > min_idx:
    ans -= 1

print(ans)
