import sys 
data = sys.stdin.read().strip().split()
idx = 0 
one  = []
two = []
three = []
n = int(data[idx]);idx+=1 
for i in range(n):
    val = data[idx].strip();idx+=1
    #print(val)
    if val=='1':
        one.append(i+1)
    elif val=='2':
        two.append(i+1)
    elif val=='3':
        three.append(i+1)
total_team = min(len(one),len(two),len(three))
print(total_team)
for i in range(total_team):
    print(one[i],two[i],three[i])