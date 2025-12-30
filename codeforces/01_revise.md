<br>
<br>

# `#01: Rating: 800,900,1000,1100 Problems`

<br>
<br>

# i) A_Beautiful_Year: 271A
- set(string) => unique character

<br>

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

<br>
<br>

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
<br>

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

<br>

# v) 706B
**TLE with list comprehation try with bisect module in python**

<br>

# vi) 490A

<br>

# vii) 469A

<br>

# viii) 492B

- সব ল্যান্টার্নের radius d একই। d যত ছোট সম্ভব রেখে 0 থেকে l পর্যন্ত পুরো রাস্তা ঢাকতে হবে।
- তাহলে যে জায়গাটায় সবচেয়ে বেশি অন্ধকার পড়ার chance, সেই জায়গাটাই ঠিক করে দিবে d কত হবে।
- Then we need to find maximum distance between two lanters then just divide it 2 we will get the minimum distance.

<br>

# ix) 1352A:
cnt = 1 
1505%10 = 5 
1505/10= 150

150%10= 0 
150/0=15

cnt=2 
15%10=5
15/10=1

cnt=3 
1%10=1 

arr = [5,0,5,1]
output:
cnt 
5, 00, 500,1000 // zero must be ignore:
final ans:
5, 500,1000

`something like this logic.If zero then it's round number like . see the test case from the problem. We just add the digit into an array from last to first num%10 then num/10 like this.`

<br>

# x) 276A
`ignore a case, i think that will not need but in the extreme case i need to consider that case.`

<br>

# xi) 472A
**What is composite number:** The number with more than 2 factors. For even number, 4 = 1,2,4 is the first composite number. And for odd number, 1,3,5,7,9 here, 9 is the first composite number for odd, 9 = 1,3,9

<br>

# xii) 110A 

<br>

# xiii) 112A

**Lexicographical order মানে হলো dictionary order, যেভাবে আমরা অভিধানে (a, b, c, … z) শব্দ সাজাই — ঠিক সেই নিয়মে string তুলনা করা।**

<br>

# xiv) 131A

`The second line contains n space-separated integers: the i-th number is pi — the number of a friend who gave a gift to friend number i. That's means kon kon frd gift paise koto number frd theke. input: 2 means oi gift paise 2 number index e jei ase tar kas theke. A litle bit confusing. `

<br>

# xv) 141A

`My initial through was count all the frequency of letter then just sum them up. But in this case maybe another letter is extra in total we have the same length. So, solve this ne need to match all the word frequency but it's a long process. In python, just sorted them and compare the string. `

<br>

# xvi) 144A

<br>

<br>
<br>

# `#02: Rating: 12+ DP`

<br>
<br>


