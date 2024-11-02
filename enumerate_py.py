fruits=["grapes","banana","orange"]
# for fruit in fruits:
#     print(fruit)

for index,fruit in enumerate(fruits):
    print(f"index{index}:{fruit}")
print()
for index,fruit in enumerate(fruits,start=1):
    print(f"index{index}:{fruit}")

