import sys 
data = sys.stdin.read().strip().split()
idx = 0
n = int(data[idx]);idx+=1
k = int(data[idx]);idx+=1
arr = list(map(int,data[idx:idx+n]));idx+=n 
if arr[0]==0:
    print(arr[0])
else:
    ans = 0
    for i in range(n):
        if (arr[i]>=arr[k-1] and arr[i]!=0):
            ans = (i+1)
    print(ans)