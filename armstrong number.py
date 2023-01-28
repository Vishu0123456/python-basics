# num = int(input("num: "))
# sum = 0
# order = len(str(num))
# copy_n = num
# while(num>0):
#     digit = num%10
#     sum+= digit**order
#     num= num//10
#
# if(sum==copy_n):
#     print("this is a armstrong number")
# else:
#     print("this is not a armstrong number")
#
num=int(input("n: "))
sum=0
order=len(str(num))
copy_num=num
while(num>0):
    digit=num%10
    sum+= digit**order
    num = num//10
if sum==copy_num:
    print("armstrong number")
else:
    print("not a armstring number")