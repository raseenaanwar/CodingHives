#To find index of largest no in a list

# largest=float('-inf')
# index_of_largest=0
# for i,num in enumerate(numbers):
#     if num>largest:
#         largest=num
#         index_of_largest=i

# print("index of largest no :",index_of_largest)    

#max()
numbers=[10,25,5,10,3,21]
largest=max(numbers)
index_of_largest=numbers.index(largest)
print(index_of_largest)

#wap to find index of second largest elemnt in a list