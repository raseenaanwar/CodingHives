#positional arguments
#Keyword arguments
#Default arguments
#Variable length Arguments(*args)
#Variable length keyword arguments(**kwargs)
def greet(name,age):
    print(f"my name is {name} and age is {age}")
greet("Alice",33)
#keyword arguments
def greet(age,name):
    print(f"my name is {name} and age is {age}")
greet(name="alice",age=33)

#default arguments
def greet(name,age=22):
    print(f"my name is {name} and age is {age}")
greet("alice")

# *args
def add_numbers(*args):
    result=sum(args)
    print("result=",result)
add_numbers(1,2,3,4)

#**kwargs
def show_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

show_info(name="alice",age=25,city='tvm')







