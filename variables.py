var1 = "84"
var2 = "39"
var3 = 85
var4 = 236.98
var5 = "hello world"
'''print(type(var1))
print(type(var3))
print(type(var4))
'''
# for chaining the type of variable we use int() , and str() just like var1 is in string , so if i want to change the type
#i can print(int(var1)) and print(int(var2))  like this i can change string into integer print(str(var3)).
'''print(100*"hello world\n")
print(int(var1)+int(var2))
'''
'''inpnum = input()
print("Your Result",int(inpnum)+10)
'''
''' if i remove int from int(inpnum) it show error because it is in str 
so i use int() . 

'''

'''# create a calculator with the help of two number which helps only to 
add the numbers.'''
print("Welcome to the Vishwajeet calculator")
print("Enter Your First Number")
num = input()
print("Enter Your Second Number")
num1 = input()
print("Sum Of These Two Numbers Are : ",int(num)+int(num1))
print("Want to use for more Calculation ? Yes/No")
