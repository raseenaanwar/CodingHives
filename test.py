numbers = [10, 5, 20, 8, 30]
largest = second_largest = float('-inf')
for num in numbers:
if num > largest:
    second_largest = largest
    largest = num
elif num > second_largest and num != largest:
    second_largest = num
print(second_largest)