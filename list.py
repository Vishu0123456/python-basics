'''studymaterial=["Pen","Notebook","Pencil","Eraser","Laptop","Mouse","Mobile"]
print(studymaterial)

# if i put print(studymaterial[0]) i will get result Pen  so on.....'''

numbers = [1,3,11,9,13,7,15,5,21]
# numbers.sort() # when i use this function it will short the given list
# numbers.reverse() # it will reverse whole  given list
# print(numbers[::2]) # it will give result after jumping one place.
numbers.reverse()
print(numbers)

#in negative slicing never take any numbers like -2,-3  because it will give you [] only try to take -1.
'''print(numbers[1:9:2])'''

'''print(max(numbers)) # after using this function you will find the maximum number of list
print(min(numbers))# after using this function you will find the manimum number of list'''

'''numbers.append(10) # by the help of this function you can add the number in the last of the list .
print(numbers)'''

'''numbers.insert(1,25) # i write 1 means index number at which place you want to add that number as like  i add 25 on 1st index.
print(numbers)'''

'''numbers.remove(11) # after using this function you will be able to remove any numbers from list as i want to remove 11 from list.
print(numbers)'''

'''numbers.pop() # it will remove last number or item automatically
print(numbers)'''

# tuple = (1,2,3,5)
# print(tuple)
#
# tuple1 = (1,) # it will not give result in bracket , so for bracket with single element write like this tuple1=(1,
# print(tuple1)
#
# a=5
# b=10
# #a,b = b,a
# temp = a
# a=b
# b = temp
# print(a,b)
