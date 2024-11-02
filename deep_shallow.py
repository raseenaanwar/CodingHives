#deep VS shallow copy
import copy
original_list=[1,2,[3,4]]
shallow_list=copy.copy(original_list)
original_list[2][0]=100
print("original_list",original_list)
print('shallow_list',shallow_list)
original_list=[1,2,[3,4]]
deep_list=copy.deepcopy(original_list)
original_list[2][0]=1000
print("original_list",original_list)
print('deep_list',deep_list)