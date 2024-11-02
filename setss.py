list1=[1,2,3,4]

list1[0] #ordered collection
set #unordered 
#not allow duplicates values
#mutable datatype
my_set={1,2,3,4,5,1,2}
set2={1,4,5,9,11,0}
print(my_set)
print(set2)
# print(my_set)
# my_set.add(100)
# print(my_set)
# my_set.remove(1)
# print(my_set)
# set3=my_set.union(set2)
# print(set3)
# set3=my_set | set2
# print(set3)

#intersection
# set3=my_set.intersection(set2)
# print(set3)

# set3=set2 & my_set
# print(set3)

#difference
# set3=my_set.difference(set2)
# print(set3)

set3=my_set - set2
print(set3)
#to clear the set
set2.clear()
print(set2)
# my_set.remove(90) # if that item is not there it will show an error
my_set.discard(90) #not raise any error
