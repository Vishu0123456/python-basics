# n = int(input("Enter the number: "))
# s =0
# num = n

# while(n>0):
#     digit = n%10
#     fact = 1
#     for i in range(1,digit+1):
#         fact = fact*i
#         s = s+fact
#         n = n//10

#     print("this is a strong number")
# else:
#     print("this is not a strong number")
# print("enter your number here:" )
# n = int(input())
# l=[]
# s = 0
# num = n
# while(n>0):
#     digit = n%10
#     fact =1
#
#     for i in range(1,digit+1):
#         fact = fact*i
#         s = s+fact
#         n = n//10
#     if i == s:
#         l.append(s)
# print(l)

import math
n = int(input(""))
l = []
for i in range(1,n+1):
    s=str(i)
    sm=0
    for j in s:
        n1 = int(j)
        fact=math.factorial(n1)
        sm=sm+fact
    if i==sm:
        l.append(i)
print(l)
