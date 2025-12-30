import sys 
data = sys.stdin.read().strip().split()
idx = 0
t = int(data[idx]);idx+=1
for _ in range(t):
    l = int(data[idx]);idx+=1
    strng = data[idx];idx+=1
    if strng.find("2026")!=-1 or strng.find("2025")==-1:
        print(0)
    else:
        print(1)
