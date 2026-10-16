**QUESTION**
B - 459
You are given N strings S1​,S2​,…,SN​ consisting of lowercase English letters.
Define N digits C1,C2,…,CN​ as follows:
If the first character of Si is one of a, b, c, then Ci = 2
If the first character of Si is one of d, e, f, then Ci = 3
If the first character of Si is one of g, h, i, then Ci = 4
If the first character of Si is one of j, k, l, then Ci = 5
If the first character of Si is one of m, n, o, then Ci = 6
If the first character of Si is one of p, q, r, s, then Ci = 7
If the first character of Si is one of t, u, v, then Ci = 8
If the first character of Si is one of w, x, y, z, then Ci = 9
Output the string obtained by concatenating C1,C2,…,CN in this order.

**CONSTRAINTS**
1≤N≤10
N is an integer.
Si is a string of length between 1 and 10, inclusive, consisting of lowercase English letters.

**CODE**
n=int(input())
s=list(map(str,input().split()))
a=""
for i in s:
    if ord(i[0])<100:
        a+="2"
    elif ord(i[0])<103:
        a+="3"
    elif ord(i[0])<106:
        a+="4"
    elif ord(i[0])<109:
        a+="5"
    elif ord(i[0])<112:
        a+="6"
    elif ord(i[0])<116:
        a+="7"
    elif ord(i[0])<119:
        a+="8"
    else:
        a+="9"
print(a)

**ABOUT MY CODE**
Time :- O(m)
Space :- O(n)
Approach :- Array
