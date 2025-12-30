import sys 
data = sys.stdin.read().strip().split()
a = int(data[0])
b = int(data[1])

remaning_time = 240 - b

cnt = 0
total_time = 0 

for i in range(1,10000):
    total_time += i*5
    if total_time>remaning_time:
        break
    
    if cnt<a:
        cnt +=1 
        
print(cnt)

