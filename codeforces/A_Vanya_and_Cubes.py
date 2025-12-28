import sys 
data = sys.stdin.read().strip().split()
n = int(data[0])
ans = 1
sum = 0
for i in range(n):
    num = (i+1)*(i)/2
    sum +=num
    if sum>=n:
        ans = (i+1)
        break
    
if ans==1:
    print(1)
elif sum==n:
    print(ans-1)
else:
    print(ans-2)
    