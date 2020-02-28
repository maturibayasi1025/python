import numpy as  np

x = np.array([1.0,2.0,3.0,4.0,5.0])
print(x)

x = np.array([1,2,3])
print(x)
print(type(x))

my_list = [1,2,3,4,5]
my_array = np.array(my_list)

my_list_2 = [10,20,30,40,50]
my_lists = [my_list,my_list_2]

print(my_lists)

my_array_2 = np.array(my_lists)

print(my_array_2)
