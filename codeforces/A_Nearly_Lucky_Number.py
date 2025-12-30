n = input().strip()
total = n.count('4')+n.count('7')
if total==7 or total==4:
    print("YES")
else:
    print("NO")