# Dictionary is nothing but key value pair

'''dic1 = {}
print(type(dic1))'''
'''dic2 = {"Ankit":"Pizza", "Aman": "Non-veg", "Rakesh": "Veg" ,"Monty" : {"B":"Maggie","L":"Rice","D":"R"}}
print(dic2)
print(dic2["Rakesh"])
print(dic2["Monty"]["B"])
dic2["Sonu"] ="Normal Food"
del dic2["Sonu"] # if i want to remove the things from dictionary.
print(dic2)'''
'''# dictionary may be in the form of string as well as numbers.'''

# create a dictionary and take input from user and return the meaning of the word from the dictionary.
# print("Welcome to My Dictionary")
# dict = {"A": "Apple", "B": "Ball", "c": "Cat" ,"D": "Dog"}
#
# a = str(input("Enter the Random word from the dictionary: "))
# meaning = dict[a]
#
# print("The meaning of the selected word is: ", end=meaning)


# questions : The user will give the word as input. Suppose that the word is present in your dictionary along with its definition or meaning.
# The program will print the meaning or definition of that word.
# For example:
# The user inputs the word: “programming”
#
# The output will be:
#
#  "the process of writing computer programs"

d1 = {"c": "computer","programming": "the process of writting computer programs" , "output": "after completing the slution the variable comes is called output"}

print(d1["programming"])