# intialisation --iter()
# iteration --- next()
# stopiteration ---to stop the loop
# my_list=[1,2,3,4]
# for item in my_list:
#     print(item)

#how internally this for loop works
my_list=[1,2,3,4]
my_iter=iter(my_list)
while True:
    try:
        item=next(my_iter)
        print(item)
    except StopIteration:
        break

