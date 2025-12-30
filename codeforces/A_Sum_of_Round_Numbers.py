import sys 
data = sys.stdin.read().strip().split()
idx=0
t = int(data[idx]);idx+=1

for  _ in range(t):
    d = int(data[idx]);idx+=1
    cnt = 0 
    arr = []
    for _ in range(len(data[idx-1])):
        if d%10 !=0:
            cnt+=1
        arr.append(d%10)
        d = int(d/10)
    
    # printing output:
    print(cnt)
    p = 1
    for i in range(len(arr)):
        if arr[i]!=0:
            print(arr[i]*p,end=" ")
        p *=10
    print("")
    