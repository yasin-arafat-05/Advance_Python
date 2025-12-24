import sys
data = sys.stdin.read().strip().split()
idx = 0
t = int(data[idx]);idx+=1
ans = 0
for _ in range(t):
    bits = data[idx];idx+=1
    if bits[0]=="+" or bits[-1]=="+":
        ans +=1
    else:
        ans -=1
print(ans)