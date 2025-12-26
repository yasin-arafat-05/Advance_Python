import sys 
import bisect
data = sys.stdin.read().strip().split();idx=0
n = int(data[idx]);idx+=1
arr = sorted(list(map(int,data[idx:idx+n])));idx+=n
t = int(data[idx]);idx+=1
for _ in range(t):
    coin = int(data[idx]);idx+=1
    
    #TLE with this apporach
    #ans = [1 if val<=coin else 0 for val in arr]
    #print(sum(ans))
    
    cnt = bisect.bisect_right(arr,coin)
    print(cnt)
    