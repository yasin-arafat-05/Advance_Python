import sys 
data = sys.stdin.read().strip()
set_arr = set(data)
if len(set_arr)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")