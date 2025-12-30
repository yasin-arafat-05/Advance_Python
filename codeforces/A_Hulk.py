import sys 
data = sys.stdin.read().strip().split()
n = int(data[0])
if n==1:
    print("I hate it")
elif n==2:
    print("I hate that I love it")
elif n%2==0:
    val = int(n/2)
    print("I hate that I love that "*(val-1),end="")
    print("I hate that I love it")
else: 
    val = int((n-1)/2)
    print("I hate that I love that "*val,end="")
    print("I hate it")
    