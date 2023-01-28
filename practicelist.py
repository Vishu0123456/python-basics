# Exercise 1: Reverse a list in Python
#
# Given:
#
# list1 = [100, 200, 300, 400, 500]
# Expected output:
#
# [500, 400, 300, 200, 100]

# list1 = [100,200,300,400,500]
# list1.reverse()
# print(list1)

# ********This is a important question because add two list.********************

# Exercise 2: Concatenate two lists index-wise
# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.
#
# Given:
#
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# Expected output:
#
# ['My', 'name', 'is', 'Kelly']
# list1=["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# list3=[i + j for i,j in zip(list1,list2)]
# print(list3)


# Turn every item of a list into its square
# Given a list of numbers. write a program to turn every item of a list into its square.
#
# Given:
#
# numbers = [1, 2, 3, 4, 5, 6, 7]
# Expected output:
#
# [1, 4, 9, 16, 25, 36, 49]

# list1 = [1,2,3,4,5,6,7]
# b = [number ** 2 for number in list1]
# print(b)

# second method
# list1 = [1,2,3,4,5,6,7]
# b=[]
# for i in list1:
#     b.append(i*i)
# print(b)


#  Exercise 4: Concatenate two lists in the following order
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# Expected output:
#
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# list3 = [i+j for i in list1 for j in list2]
# print(list3)

# Exercise 5: Iterate both lists simultaneously
# Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.
#
# Given
#
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# Expected output:
#
# 10 400
# 20 300
# 30 200
# 40 100

#
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# for x,y in zip (list1,list2[::-1]):
#     print(x,y)

# another method through i solve this question

# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# d1 = {"a":"10  400", "b":"20  300", "c":"30  200", "d":"40  100"}
# print(d1["a"])
# print(d1["b"])
# print(d1["c"])
# print(d1["d"])

#
# Exercise 6: Remove empty strings from the list of strings
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
#
# Expected output:
#
# ["Mike", "Emma", "Kelly", "Brad"]

# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# # remove None from list1 and convert result into list
# g = list(filter(None, list1))
# print(g)

# list2 = ["Boy", "", "Good", "Bad", "", "or", "", "Not"]
# b = list(filter(None,list2))
# print(b)

# Exercise 7: Add new item to list after a specified item
# Write a program to add item 7000 after 6000 in the following Python List
#
# Given:
#
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# Expected output:
#
# [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)
# print(list1)

# list1 = [15, 59, 56,  [80, 70, 40, 50], 10, 21]

# output: [15,59,56[20,30,60,90[80,70,40,50,2],25],10,21]
# list1[3].append(2)
# print(list1)
# list1 =  [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(4000)
# print(list1)


# Exercise 9: Replace list’s item with new value if found
# You have given a Python list. Write a program to find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of an item.
#
# Given:
#
# list1 = [5, 10, 15, 20, 25, 50, 20]
# Expected output:
#
# [5, 10, 15, 200, 25, 50, 20]

#
# list1 = [5, 10, 15, 20, 25, 50, 20]
#
# # get the first occurrence index
# index = list1.index(20)
#
# # update item present at location
# list1[index] = 200
# print(list1)

# Exercise 10: Remove all occurrences of a specific item from a list.
# Given a Python list, write a program to remove all occurrences of item 20.
#
# Given:
#
# list1 = [5, 20, 15, 20, 25, 50, 20]
# Expected output:
#
# [5, 15, 25, 50]

# list1 = [5,20,15,20,25,50,20]
# list1.remove(20)
# list1.remove(20)
# list1.remove(20)
# print(list1)
