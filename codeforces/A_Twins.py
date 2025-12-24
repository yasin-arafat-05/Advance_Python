import sys
data = sys.stdin.read().strip().split()
idx=0
c = int(data[idx]);idx+=1
arr = list(map(int,data[idx:idx+c]));idx+=c
arr = sorted(arr)
ans = 0 
for i in range(1,c+1):
    if sum(arr[:i]) < sum(arr[i:]):
        ans = (c-i)
if ans==0:
    print(len(arr))
else:
    print(ans)