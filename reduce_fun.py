#reduce()---functools module

#multiplying all elmns in a list

from functools import reduce
def multiply(x,y):
    return x*y
numbers=[2,3,4]
result=reduce(multiply,numbers)
print(result)
# sum of all elmns

from functools import reduce
def add(x,y):
    return x+y
numbers=[1,2,3,4,5]
result=reduce(add,numbers)
print(result)
# to find maximum
from functools import reduce
def maximum(x,y):
    return x if x>y else y
numbers=[5,1,8,4,2]
result=reduce(maximum,numbers)
print(result)
