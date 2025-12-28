import sys 
data = sys.stdin.read().strip().split()
idx = 0;cnt = 1
n = int(data[0]);idx+=1
for _ in range(n-1):
    val1 = data[idx];idx+=1
    val2 = data[idx];idx+=1
    #print(val1,val2)
    if val1=="10" and val2=="01":
        cnt+=1
    elif val1=="01" and val2=="10":
        cnt+=1 
    idx -=1
print(cnt)
