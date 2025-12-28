import sys 
data = sys.stdin.read().strip().split()
ans = 0; idx = 0 
t = int(data[idx]);idx+=1
for _ in range(t):
    a = int(data[idx]);idx+=1
    b = int(data[idx]);idx+=1
    if abs((a-b))>=2:
        ans+=1
print(ans)