#find the largest even no in a list
#n%2==0 even
numbers=[7,3,5,9,77,2,78,66]
largest_even=None
for num in numbers:
    if num%2==0:
        if largest_even is None or num>largest_even:
            largest_even=num
if largest_even:
    print("largest even ",largest_even )
else:
    print("No even numbers in the list")

#list comp
numbers=[7,3,5,9,77,2,78,66]
even_numbers=[num for num in numbers if num%2==0]
if even_numbers:
    print(max(even_numbers))
else:
    print("No even nos")

#Hw find second largest even no in a list