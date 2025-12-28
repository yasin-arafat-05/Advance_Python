import sys 
data = sys.stdin.read().strip()
data = set(data)
data.remove("{")
data.remove("}")
if len(data)==0:
    print(0)
elif len(data)==1:
    print(1)
else:
    print(len(data)-2)