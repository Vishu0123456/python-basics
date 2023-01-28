s=set()
print(type(s))

my_set = set([11,12,13,45])
print(my_set)
print(type(my_set))

s.add(1) # this function use for add element in the set . if i try to add the same element in set it will not shiow the both result .
print(s)
s.add(45)
print(s)
s1=s.union({2,3,4,5,6})
print(s,s1)
s2 = s.intersection({2,3,4,5,6})
print(s1,s2)