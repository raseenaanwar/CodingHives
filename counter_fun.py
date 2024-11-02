#count nos in a list
from collections import Counter
numbers=[1,2,3,2,4,4,4,5]
count=Counter(numbers)
print(count)
#counting characters in a str
str="Hello Coders"
count=Counter(str)
print(count)

def count_vowels(str):
    vowels="aeiouAEIOU"
    count=Counter(str)
    total_vowels=sum(count[char] for char in vowels)
    print(total_vowels)

count_vowels("Hello Coders")