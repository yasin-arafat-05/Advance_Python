import sys 
data = sys.stdin.read().strip()
data_int = int(data)+1
while True:
    if len(set(str(data_int))) == len(str(data_int)):
        print(data_int)
        break
    data_int+=1
