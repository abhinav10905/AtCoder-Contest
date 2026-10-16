**QUESTION**
A - Hell, World!
You are given an integer X between 1 and 10, inclusive.
Output the string obtained by deleting only the X-th character from the string HelloWorld.

**CONSTRAINTS**
X is an integer between 1 and 10, inclusive.

**CODE**
n=int(input())
a="HelloWorld"
print(a[:n-1]+a[n:])
