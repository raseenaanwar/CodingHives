# person=['asha',23,'tvm']
# print(person[1])
# person={"name":'asha',"age":23,"city":"tvm"}
# print(person[age])
#creating a dict
# student={"name":"asha","age":23,"grade":'A'}
# print(student)

#dict()
# student=dict(name="asha",age=23,grade="A")
# print(student)

# #access a dict
# print(student["name"])
# # print(student["subject"])
# #get()
# print(student.get("age"))
# print(student.get("subject"))

# #add or update elements

# student["age"]=24
# print(student)
# student["subject"]="Maths"
# print(student)

# #removing elemnt--del()
# # del student["subject"]
# # print(student)
# #pop()
# grade=student.pop("grade")
# print(student)
# print(grade)
# student.clear()
# print(student)
student=dict(name="asha",age=23,grade="A")
#dict opns and methods

if "subject" in student:
    print('name is exist in student')
else:
    print("not")

#.keys()
print(student.keys())

#.values()
print(student.values())

#items()

print(student.items())
