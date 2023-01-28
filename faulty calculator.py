# FAULTY CALCULATOR
 # 45 * 3 = 555 , 56 + 9 = 77 , 56 / 6 = 4
 # Design a calculator which performs all the calculation corrrectly except these ones:45 * 3 = 555 , 56 + 9 = 77 , 56 / 6 = 4
 # your progrma should take operator and take two numbers from user as input then return the result.


print("Welcome to the Baap Calculator")

print("Enter your first number")
num1 = int(input())

print("Enter your second number")
num2 = int(input())

print("Enter your operator",'+','-','*','**','/')
operator = input()

if num1 == 45 and num2 == 3 and operator == '*':
    print("RESULT:",555)

if num1 == 56 and num2 == 9 and operator == '+':
    print("RESULT:",77)

if num1 ==56 and num2 == 6 and operator == '/':
    print("RESULT:",4)

elif operator == '+':
    plus = num1+num2
    print("RESULT:",plus)

elif operator == '-':
    subtract = num1-num2
    print("RESULT:",subtract)

elif operator == '*':
    multiply = num1*num2
    print("RESULT:",multiply)

elif operator == '/':
    divide = num1/num2
    print("RESULT:",divide)



else:
    print("unexpected error! ,please enter a valid input")

print("Do you want to calculate More?",'yes','no')
condition = input()

print("Again Run the program ")
print("Thank you for using")



