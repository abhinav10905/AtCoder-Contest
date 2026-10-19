**QUESTION**
A - Odd Index Sum
You are given an integer sequence of length N: A=(A1,A2,…,AN).
Find the sum of the odd-indexed terms of A.
More formally, find the sum of Ai over all odd i satisfying 1≤i≤N.

**CONSTRAINTS**
All input values are integers.
1≤N≤100
1≤Ai≤100

**CODE**
n=int(input())
a=list(map(int,input().split()))
c=0
for i in range (0,n):
  if i%2==0:
    c+=a[i]
print(c)

**ABOUT MY CODE**
Time :- O(n)
Space :- O(1)
Approach :- Array, Math
