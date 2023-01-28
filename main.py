mystr = "Vishwajeet is a good boy"
print(len(mystr))
print(mystr[0:10])
''' if i want to print the letter v,s,w,j,e like this gap of 1 word the we use slicing in another way.'''
print(mystr)
print(mystr[0:10:2])
print(mystr[0:10:3])
print(mystr[0:24:2])
print(mystr[0:24:3])
'''if i not write 0 it will automatically take 0 and if not write any letter after [0:19:] it will take 1.'''
print(mystr[0:24:])
print(mystr[::])

# another example of slicing in string
x = "monty python"
print(len(x))
''' if i want to print the words from python then we use -12,-11 like this and their is another way to solve the slicing of this question '''

print(x[:-4])
print(x[0:8])
''' as like this print value the value is coming same so we can slice the string in negative as like pisitive.'''

print(x[::-1])# this will interchange the word like python - nohtyp

print(x[::-2]) # if i try to print like this it will print the word with 1 word gap

print(mystr.isalnum()) # this will give false result because they are not present in the form of alphanumeric system.
# if i remove all space from mystr = "vishwajeetisagoodboy" it will print true in result.

print(mystr.isalpha()) # it will give the result false because there is no alphaumeric condition . means space present and no numeric value present .

y = "ramis2good"
print(y.isalnum()) # this is alphanum because there is no space in between words.

print(mystr.endswith("boy")) # it will give result true because the sentence is lasting with word boy. if i enter something else it will give result as false .

print(mystr.count("o")) # this will help to count the given word in sentence.

print(y.capitalize()) # by the help of this function i can captalized my letter as like in y= r is small  after using the function it will become R.
print(mystr.find("good")) # this will hrlp to find a particular word from sentenc.and given you count number by which you can find the word easily.

print(mystr.lower()) # it will show all word of sentence in lower alphabets.
print(mystr.upper()) # it will show all word of sentence in upper alphabets.

print(mystr.replace("Vishwajeet","Ram")) # by the help of this function we can replace word from string .