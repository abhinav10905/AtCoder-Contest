**QUESTION**
B - Longest Rainy Streak
Takahashi recorded the weather for N consecutive days, recording each day as "sunny" or "rainy".His record is given as a string S of length N in the following format.
The i-th character ( 1≤i≤N ) of S represents the weather on the i-th day from the start of the record.
If the i-th character of S is S, the record for that day was "sunny".
If the i-th character of S is R, the record for that day was "rainy".
Find the maximum number of consecutive days for which Takahashi recorded "rainy".
If Takahashi never recorded "rainy", the answer is 0.

**CONSTRAINTS**
N is an integer satisfying 1≤N≤100.
S is a string of length N consisting of S and R.

**CODE**
n=int(input())
s=input()
c=0
b=0
for i in s:
  if i=="R":
    b+=1
  else:
    c=max(b,c)
    b=0
c=max(b,c)
print(c)

**ABOUT MY CODE**
Time :- O(n)
Space :- O(1)
Approach :- String, Math
