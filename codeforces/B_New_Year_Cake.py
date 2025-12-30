import sys 
data = sys.stdin.read().strip().split()
idx = 0
t = int(data[idx]);idx+=1
for _ in range(t):
    a = int(data[idx]);idx+=1
    b = int(data[idx]);idx+=1
    total = a+b 
    k = 1 
    ans = 0 
    for i in range(2,total):
        if k>total:
            break
        k += (2*i);ans = i 
    print(ans)