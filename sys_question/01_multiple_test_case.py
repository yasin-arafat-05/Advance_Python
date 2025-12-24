
# 2
# 5
# 100 99 98 97 96
# 4
# 2 5 7 9

import sys


data = sys.stdin.read().split()
idx = 0

t = int(data[idx]);idx+=1

for _ in range(t):
    n = int(data[idx]);idx+=1
    arr = list(map(int,data[idx:idx+n]));idx +=n 
    print(arr)
    