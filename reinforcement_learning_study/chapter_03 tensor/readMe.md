# 강화학습을 공부하자 #

* 강화학습을 수업으로 듣기는 했는데 이제 책으로도 한번 훓어볼 때가 되었다.

    * [해법코드로 설명한 심층강화학습](https://book.naver.com/bookdb/book_detail.nhn?bid=16293174) 을 보면서 공부하도록 하자.

## 1주차 ##

1주차는 pytorch tensor object 에 대해 알아본다.. 

### tensor 기본 ###
**torch의 네트워크에 사용되는 데이터 object**

* tensor는 [pytorch.tensor](https://pytorch.org/docs/stable/tensors.html)를 보면 **multi-dimensional matirix** 즉 다차원 행렬이다. 이 때, 행렬에 들어가는 데이터는 실수 형태 혹은 bool 값으로 될 수 있으며 아래와 같이 선언할 수 있다.

```python
import torch
## tensor 선언 및 3*2 array import
tensor_float = torch.FloatTensor(3,2)

# result
# tensor([[1.4585e-19, 6.3369e-10],
#        [2.5038e-12, 4.0513e-11],
#        [4.3920e-05, 8.2991e-33]])
```

* tensor에서 사용되는 데이터는 대표적으로 아래와 같다.
    * torch.float32, torch.float
    * torch.float64, torch.double
    * torch.int32, torch.int

### tensor calculate operation ###
**연산 후 tesnor 객체 내용이 변하거나 계산값만 반환하고 원본 tensor는 그대로이거나**

* tensor 계산 method는 아래와 같이 큰 분류로 나누어진다
    * in-place : tesnor 원본에 연산이 적용되어 연산 후 tensor 값이 변화된다.
    * 쉽게 이해하자면 `i += y` 수식이라 생각하면 편하다.
        * ex) zero_(), add_() eta... 
        * example

    * functional : tensor 를 복사하여 연산을 수행하기에 tensor 값은 변하지 않는다.
        * ex) zero(), add()
        * example

#### in-place 예시 ####
```python
import torch
x = torch.rand(1)
y = torch.rand(1)

print(f"before opertation")
print(f"x => {x} || y=> {y}")

x.add_(y)

print(f"after opertation")
print(f"x => {x} || y=> {y}")

## result
# before opertation
# x => tensor([0.4699]) || y=> tensor([0.7268])
# after opertation
# x => tensor([1.1966]) || y=> tensor([0.7268])
```

#### functional 예시 ####
```python
import torch
x = torch.rand(1)
y = torch.rand(1)

print(f"before opertation")
print(f"x => {x} || y=> {y}")

x.add(y)

print(f"after opertation")
print(f"x => {x} || y=> {y}")

## result
# before opertation
# x => tensor([0.7315]) || y=> tensor([0.0467])
# after opertation
# x => tensor([0.7315]) || y=> tensor([0.0467])
```


