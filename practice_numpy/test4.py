import numpy as  np

"""
配列操作
"""

sample_array = np.arange(10)
print(sample_array)

sample_array_2 = sample_array.reshape(2,5)

sample_array_3 = np.array([[1,2,3],[4,5,6]])
sample_array_4 = np.array([[7,8,9],[10,11,12]])

print(np.concatenate([sample_array_3,sample_array_4],axis=1)) # axis=1は行の結合

print(np.hstack((sample_array_3,sample_array_4)))

print(np.concatenate([sample_array_3,sample_array_4],axis=0)) # axis=0は列の結合

print(np.vstack((sample_array_3,sample_array_4)))
