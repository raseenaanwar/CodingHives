# def function_name():
#     Code 
#     return result

# def say_hello():
#     return "Hello from Coding Hives"

# print(say_hello())

#functions with parameters
def greet(name):
    return f"Hello,{name}"

print(greet("Coders"))

#returning values from a function
def add_no(a,b):
    return a+b

result=add_no(4,6)
print(result)

#default parameters
def greet(name="Guest"):
    return f"Hello ,{name}"

print(greet())

# get multiple values from the function

def get_person_info():
    name="anu"
    age=30
    return name,age

person_name,person_age=get_person_info()
print(person_name,person_age)

#function scope(local & global variable)
def my_fun():
    local_var=10
    return local_var
print(my_fun())
print(local_var)
