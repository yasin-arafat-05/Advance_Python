import sys 
data = sys.stdin.read().strip().split()

t = int(data[0])
arr = list(map(int,data[1:1+t]))
ans = arr.copy()

for i in range(len(arr)):
    ans[arr[i]-1] = i+1
print(*ans)
