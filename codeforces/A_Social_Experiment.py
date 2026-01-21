import sys 
data = sys.stdin.read().strip().split()
idx=0
t = int(data[idx]);idx+=1

for _ in range(t):
    n = int(data[idx]);idx+=1
    if n==2 or n==3:
        print(2)
    elif n%2==0 and (n//2)%2==0:
        print(0)
    elif n%3==0 and (n//2)%2==0:
        print(0)
    else:
        print(1)
    
        
        
        