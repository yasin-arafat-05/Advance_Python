import sys 
data = sys.stdin.read().strip().split()
idx=0
w = data[idx];idx+=1
val = data[idx]
ans = 0
prev = val[0]
for ch in val[1:]:
    if prev==ch:
        ans+=1
    prev = ch 
print(ans)