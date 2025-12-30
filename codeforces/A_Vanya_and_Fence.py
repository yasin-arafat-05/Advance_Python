import sys 
import bisect
data = sys.stdin.read().strip().split()
idx = 0
n = int(data[idx]);idx+=1
h = int(data[idx]);idx+=1
arr = sorted(list(map(int,data[idx:idx+n])))
index = bisect.bisect_right(arr,h)
ans = index + (len(arr)-index)*2
print(ans)