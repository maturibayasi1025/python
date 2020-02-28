import numpy as  np

sample_array = np.arange(10)
print(sample_array + 5)

n1 = np.array([1,2,3,4,5])

# 配列の次元数取得はndim()で行う
np.ndim(n1)

n2 = np.array([[1,2],[3,4],[5,6]])
print(n2)

print(np.ndim(n2))
