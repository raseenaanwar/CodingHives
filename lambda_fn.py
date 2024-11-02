#lambda arguments:expression
#add 2 nos
add=lambda x,y:x+y
result=add(3,5)
print(result)

#using lambda with map(square of a list)
numbers=[1,2,3,4,5]
square_num=list(map(lambda x:x**2,numbers))
print(square_num)

#lambda with filter
numbers=[1,2,3,4,5,6]
even_no=list(filter(lambda x:x%2==0 ,numbers))
print(even_no)