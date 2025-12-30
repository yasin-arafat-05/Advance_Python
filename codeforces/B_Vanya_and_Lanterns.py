import sys

data = sys.stdin.read().split()
idx = 0

n = int(data[idx]); idx += 1
l = int(data[idx]); idx += 1

arr = sorted(map(int, data[idx:idx+n]))

# start gap
max_dis = arr[0]

# middle gaps
for i in range(len(arr)-1):
    max_dis = max(max_dis, (arr[i+1] - arr[i]) / 2)

# end gap
max_dis = max(max_dis, l - arr[-1])

print(f"{max_dis:.10f}")
