numbers=[1,2,3,4,5]
# square=[]
# for number in numbers:
#     square.append(number**2)
# print(square)
 
square=[number**2 for number in numbers]
print(square)

# odd=[]
# for number in numbers:
#     if number % 2==1:
#         odd.append(number)
# print(odd)

odd=[number for number in numbers if number%2==1]
print(odd)

even=[number for number in numbers if number%2==0]
print(even)

#write a program to convert temperature in celcius to farenheet usin lc