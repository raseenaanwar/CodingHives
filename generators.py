def my_generator():
    yield 1
    yield 2
    yield 3

# gen=my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# for value in my_generator():
#     print(value)

def squares_num(limit):
    for num in range(1,limit+1):
        yield num**2

for square in squares_num(5):
    print(square)