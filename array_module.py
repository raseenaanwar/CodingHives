# 'i' for integers
# 'f' for floating-point numbers
# 'd' for doubles
# 'u' for Unicode characters
import array
int_array=array.array("i",[1,2,3,4,5])
print(int_array)
print(int_array[2])
int_array[2]=99
print(int_array)
int_array.append(100)
print(int_array)
int_array.remove(100)
print(int_array)
for num in int_array:
    print(num)
print("length= ",len(int_array))