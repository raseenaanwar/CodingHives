def second_largest(numbers):
    largest=sl=float("-inf")
    for num in numbers:
        if num>largest:
            sl=largest
            largest=num
        elif num>sl and num!=largest:
            sl=num
    return sl

numbers=[1,3,211,111,54,11]
print(second_largest(numbers))