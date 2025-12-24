import sys
data = sys.stdin.read().strip().split()
idx = 0
ans = 0
matrix = [[0]*5 for _ in range(5)]
for i in range(5):
    for j in range(5):
        matrix[i][j] = int(data[idx])
        if int(data[idx])==1:
            ans = abs(2-i) + abs(2-j)
        idx +=1 
print(ans)