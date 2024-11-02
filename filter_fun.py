# filter even nos in a list
def is_even(num):
    return num%2==0
numbers=[1,2,3,4,5,6]
filtered_num=list(filter(is_even,numbers))
print(filtered_num)

#filter strings based on length

def longer_than_three(s):
    return len(s)>3

words=['cat','elephant','dog','lion']
filtered_words=list(filter(longer_than_three,words))
print(filtered_words)

#filter negative nos
def is_positive(num):
    return num>0

numbers=[-10,5,-3,7,-1,0,4]
filtered_numss=list(filter(is_positive,numbers))
print(filtered_numss)