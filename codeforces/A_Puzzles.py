import sys 
data = sys.stdin.read().strip().split();idx=0
n_std = int(data[idx]);idx+=1
m = int(data[idx]);idx+=1
arr = sorted(list(map(int,data[idx:idx+m])));idx+=m
diff = [(arr[n_std-1+i]-arr[i]) for i in range((m-n_std+1))]
print(min(diff))
