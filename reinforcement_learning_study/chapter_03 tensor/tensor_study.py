import torch
import numpy as np

## 텐서 선언 및 3*2 array import
tensor_float = torch.FloatTensor(3,2)
print(tensor_float)

# result
# tensor([[1.4585e-19, 6.3369e-10],
#        [2.5038e-12, 4.0513e-11],
#        [4.3920e-05, 8.2991e-33]])

## zero() 를 이용해 모든 값을 0으로 초기화
tensor_float.zero_()
print(tensor_float)

# result
# tensor([[0., 0.],
#        [0., 0.],
#        [0., 0.]])


x = torch.rand(1)
y = torch.rand(1)

print(f"before opertation")
print(f"x => {x} || y=> {y}")

x.add(y)

print(f"after opertation")
print(f"x => {x} || y=> {y}")