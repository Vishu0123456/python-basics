num = int(input("Enter your number here: "))

fact = 1

if num<0:
    print("factorial of 0 does'nt exist")

if num == 0:
    print("factorial of o is 1")

if num >0:
    for i in range(1,num+1):
        fact = fact*i

print("factorial of given number are",fact)

