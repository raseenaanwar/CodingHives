#searching a number
numbers=[1,2,3,4,5]
for num in numbers:
    if num==99:
        print("Found No")
        break
else:
    print("Not Found")

#checking prime (2,3,5,7,...)
#7--2,3,4,5,6
num=6
for i in range(2,num):
    if num%i==0:
        print("Not Prime")
        break
else:
    print("Prime")

#SEARCHING FOR A STRING IN A LIST
names=["sipsa","gopika","sanath","hima"]
for name in names:
    if name=="asha":
        print("found")
        break
else:
    print("not found")
