# num  = int(input("Enter your Number for series: "))
# a = 0 # because in fibonacci series the number starts with 0 and 1.
# b = 1
# sum = 0
# if num<=0:
#     print("please enter a valid number")
# else:
#     for i in range(0,num):
#         print(sum," ")
#         a=b
#         b=sum
#         sum=a+b

num = int(input(""))
a=0
b=1
s=0
if num<0:
    print("enter a valid number")
else:
    for i in range(0,num):
        print(s," ")
        a=b
        b=s
        s=a+b
