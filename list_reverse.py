#reverse()
numbers=[1,2,3,4,5]
numbers.reverse()
print(numbers)
#slicing
numbers=[1,2,3,4,5]
reversed_num=numbers[::-1]
print(reversed_num)
#reversed()
reversed_num=list(reversed(numbers))
print(reversed_num)
#for loop
reversed_num=[]
for num in numbers:reversed_num.insert(0,num)
