# t = number of test cases: 2 
# test case 1: n=2 rows, m=3 columns
# 2             
# 2 3           
# 1 2 3
# 4 5 6
# 3 2           
# 7 8
# 9 10
# 11 12

import sys
idx=0 
data = sys.stdin.read().split()

t = int(data[0]);idx+=1
for _ in range(t):
    r = int(data[idx]);idx+=1
    c = int(data[idx]);idx+=1
    matrix = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            matrix[i][j]=int(data[idx]);idx+=1
    print(matrix)