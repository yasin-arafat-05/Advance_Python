import sys 
data = sys.stdin.read().strip().split()
t = data[0]
match = data[1]
if len(match.split("A"))>len(match.split("D")):
    print("Anton")
elif len(match.split("A"))==len(match.split("D")):
    print("Friendship")
else:
    print("Danik")

