# n (1 ≤ n ≤ 1000) 
# 4 7 47 74 
# 444 474 447 777 747 774
n = int(input());flag = 0 
luck_num = [4,7,47,74,44,77,444,477,474,447,777,747,774,744]
for val in luck_num:
    if n%val==0:
        flag = -1 
        print("YES")
        break
if flag!=-1:
    print("NO")