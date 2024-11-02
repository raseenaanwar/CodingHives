#madam racecar
#Reverse the string and compare 
# def is_palin(str):
#     str=str.lower()
#     # 
#     return str==str[::-1]
# print(is_palin("Madam"))

#using two pointer technique --madam --hai
# def is_palin(str):
#     str=str.lower()
#     left,right=0,len(str)-1
#     while left<right:
#         if str[left]!=str[right]:
#             return False
#         left+=1
#         right-=1
#     return True
# print(is_palin("race"))

#reversed() 
# def is_palin(str):
#     str=str.upper()
#     # print(reversed(str))
#     reversed_str="".join(reversed(str))
#     return str==reversed_str
# print(is_palin("madam"))

#using recursion
def is_palin(str):
    str=str.lower()
    if len(str)<=1: # base case
        return True
    if str[0]!=str[-1]: #compare first and last character
        return False
    return is_palin(str[1:-1]) #madam

print(is_palin("madam"))


   












#two pointer method 




