# names=["anna","boby"]
# ages=[25,30,32]
# # combined=zip(names,ages)
# # print(list(combined))
# for name,age in zip(names,ages):
#     print(f"{name} is {age} years old")

names=["anna","boby","asha"]
ages=[25,30,32]
cities=["tvm",'chennai','ekm']
for name,age,city in zip(names,ages,cities):
    print(f"{name} is {age} years old and lives in {city}")

#unzip

combined=[("alice",23),("boby",33),("asha",12)]
names,ages=zip(*combined)
print(names)
print(ages)