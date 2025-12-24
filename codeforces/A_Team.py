import sys 
data = sys.stdin.read().strip().split()
idx=0
soln = 0
t = int(data[0]);idx+=1
for _ in range(t):
    arr = list(map(int,data[idx:idx+3]));idx+=3 
    if sum(arr)>=2:
        soln +=1 
print(soln)
    