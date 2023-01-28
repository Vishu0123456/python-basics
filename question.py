# # dictionary number question 1
#
# #
#
# # dictionary question number 2
#
# # a = map(int,input("a").split(","))
#
#         #  FOR CHECKING NUMBER IS PALINDROME OR NOT
#
#
# #  question:
# #  1. fibonaci series
#
# num = int(input("Enter your number here: "))
# a = 0
# b = 1
# sum = 0
# if num<0:
#     print("enter the corret value")
# else:
#     for i in range(0,num):
#         print(sum,"")
#         a = b
#         b = sum
#         sum = a+b
#
# fact = 1
# if num<0:
#     print("the factorial of 0 does'nt exist")
# if num == 0:
#     print("factorial of 0 is 1")
# if num>0:
#     for i in range(1,num+1):
#         fact = fact * i
# print("the factorial of given number",fact)

# solution of 2nd question
# num = int(input("Enter your number: "))
# c=[]
# d=0
# for i in range(num):
#      b = input()
#      c.append(b)
#      if b==b[::-1]:
#          d=d+1
# print(c)
# print(d)


 #solution of 3rd question

# a = map(int,input("a ").split())
# b=0
# c=0
# d=0
# for i in a:
#      if i %2==0:
#         b=b+1
#      if i%3==0:
#         c=c+1
#      if i%5==0:
#          d=d+1
#          print({"2":b,"3":c,"5":d})


# solution of 4th
number = 2,3,4,5,7
for i in range(number):
    if number % i == 0:
        print("not prime")
        break
else:
    print("prime")
c = number **2
print("the square of prime number is",c)
