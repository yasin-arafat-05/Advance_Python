import sys 
data = sys.stdin.read().strip().split()
idx = 0
n = int(data[0]);idx+=1
arr = sorted(list(map(int,data[idx:idx+n])));idx+=n 
print(*arr)
