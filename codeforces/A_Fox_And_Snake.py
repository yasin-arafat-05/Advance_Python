import sys 
data = sys.stdin.read().strip().split()
n = int(data[0]);m = int(data[1])
even = 1
for i in range(1,n+1):
    if i%2!=0:
        print("#"*m)
    elif even==1:
        print("."*(m-1),end="")
        print("#")
        even = -1
    else:
        print("#",end="")
        print("."*(m-1))
        even = 1
        