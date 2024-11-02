#find largest number in  a list
numbers=[-3,-1,-4,-5,-9,-2,-6,-5] #9
# largest=float('-inf')
# # largest=0
# for num in numbers:
#     if num>largest:
#         largest=num
# print("largest: ",largest)
##2nd way
largest=max(numbers)
print(largest)

##3rd way

numbers.sort()#sort list in asc
print(numbers[-1])