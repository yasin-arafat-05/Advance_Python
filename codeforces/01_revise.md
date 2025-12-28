i) A_Beautiful_Year: 271A
- set(string) => unique character

# ii) 318A
- Formulazied the odd number:
- 3 তম odd number হবেঃ (2*3-1) = 5 
- 4 তম odd number হবেঃ (2*4-1) = 7 

<br>

- Formulazied the even number:
- 1 তম even number হবেঃ 2*1 = 2
- 2 তম even number হবেঃ 2*2 = 4 
- 3 তম even number হবেঃ 2*3 = 6 
- 4 তম even number হবেঃ 2*4 = 8 


# iii) 230B
t=p^2, where p is prime
Divisors of: 1, p, p²
total = 3
প্রবলেম হচ্ছে, যদি x value constrain 10^12 পযন্ত নেই তাহলে সব গুলোর ক্ষেত্রে যদি আলাদা আলাদা করে prime কিনা চেক করতে চায় তাহলে time limit খাবো । solution কি?? sieve of eratosthenes algorithrm. 
it's a very efficient algorhtm where all the prime number will save. But this sieve algorithrm is also very slow in term of python. Below we have a modified version of this.
```python
#MAX = int(math.sqrt(1e12))
MAX = 10**6 + 1
is_prime = [True]*MAX
for i in range(2,int(MAX**0.5+1)):
    if is_prime[i]:
        for j in range(i*i,MAX,i):
            is_prime[j] = False
```
# iv) 230A 
**Need to Sort the value it don't come in my mind** <br>
Kirito can fight the dragons in any order 

📌 এর মানে:
Input order বাধ্যতামূলক নয় 
তুমি নিজে order বেছে নিতে পারো
⇒ order optimize করার সুযোগ আছে

👉 যখনই দেখবে:
any order <br>
rearrange <br>
choose sequence <br>
can be done in any order

# v) 706B
**TLE with list comprehation try with bisect module in python**

# vi) 490A
# vii) 469A

