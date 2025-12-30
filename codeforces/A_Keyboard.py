import sys 
data = sys.stdin.read().strip().split()

ch = data[0]
sen = data[1]
keyboard = "qwertyuiopasdfghjkl;zxcvbnm,./"
for i in range(len(sen)):
    if ch=="R":
        indx = keyboard.find(sen[i])
        print(keyboard[indx-1],end="")
    else:
        indx = keyboard.find(sen[i])
        print(keyboard[indx+1],end="")


