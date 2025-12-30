import sys 
data = sys.stdin.read().strip().split()
n = int(data[0])
a = n//5
rem = n-(a*5)

b = rem//4 
rem = rem - (b*4)

c = rem//3 
rem = rem - (c*3)

d = rem//2
rem  = rem - (d*2)

e = rem

#print(a,b,c,d,e)
print(a+b+c+d+e)