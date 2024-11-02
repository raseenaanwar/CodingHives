#loop
str="education"
vowels="aeiouAEIOU"
count=0
for char in str:
    if char in vowels:
        count+=1
print(count)

#list comprehension
print(len([char for char in str if char in vowels]))

#fliter() lambda fun
print(len(list(filter(lambda char:char in vowels,str))))
