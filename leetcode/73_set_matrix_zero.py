import numpy as np 
data = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# matrix = np.array(data)
# matrix = np.array(matrix)
# rows, cols = np.where(matrix == 0)
# print(rows,cols)
# for r, c in zip(rows, cols):
#     matrix[r, :] = 0      
#     matrix[:, c] = 0 
# print(matrix)
# for a in data:
#     print(a)
len_col = len(data)
len_row = len(data[0])

index = [(i,j)  for i in range(len(data)) for j in range(len(data[0])) if data[i][j]==0]

for row,col in index:
    #for row:
    for i in range(len(data[0])):
        data[row][i]=0 
    #for col:
    for i in range(len(data)):
        data[i][col]=0
print(data) 
    