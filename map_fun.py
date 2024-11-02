# square of numbers in a list
def square(num):
    return num**2

number=[1,2,3,4,5]
squared_num=list(map(square,number))
print(squared_num)

#converting strings to uppercase
def to_uppercase(str):
    return str.upper()
words=["hello","from","coding","hives"]
upper_words=list(map(to_uppercase,words))
print(upper_words)