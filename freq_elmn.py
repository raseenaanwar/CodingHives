#count()
#loop
#listcomprehension
#Counter()
number=[1,2,2,3,4,4,4,5]
#count()
print(number.count(4))
#for loop
count=0
for num in number:
    if num==4:
        count+=1
print(count)
#list comprehension
print(len([num for num in number if num==4]))
#Counter()
from collections import Counter
counts=Counter(number)
print(counts[4])
