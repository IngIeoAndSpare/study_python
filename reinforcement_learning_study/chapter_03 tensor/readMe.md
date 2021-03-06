# 강화학습을 공부하자 #

* 강화학습을 수업으로 듣기는 했는데 이제 책으로도 한번 훓어볼 때가 되었다.

    * [해법코드로 설명한 심층강화학습](https://book.naver.com/bookdb/book_detail.nhn?bid=16293174) 을 보면서 공부하도록 하자.

## 1주차 ##

1주차는 pytorch tensor object 에 대해 알아본다.

### tensor 기본 ###
**torch의 네트워크에 사용되는 데이터 object**

* 정말 간단하게 설명하면 tensor는 [pytorch.tensor](https://pytorch.org/docs/stable/tensors.html)를 보면 **multi-dimensional matirix** 즉 다차원 행렬이다. 이 때, 행렬에 들어가는 데이터는 실수 형태 혹은 bool 값으로 될 수 있으며 아래와 같이 선언할 수 있다.

* (+) 덧붙여서 tensor는 실제 학습 **[backward]**(https://pytorch.org/docs/stable/_modules/torch/tensor.html#Tensor.backward)에 필요한 데이터, 그리고 학습을 위한 `metadata`를 저장하는 객체 **[computation graphs]**(https://jdhao.github.io/2017/11/12/pytorch-computation-graph/) 와 함께 사용하여 학습을 진행한다.

```python
import torch
## tensor 선언 및 3*2 array import
tensor_float = torch.FloatTensor(3,2)

## result
# tensor([[1.4585e-19, 6.3369e-10],
#        [2.5038e-12, 4.0513e-11],
#        [4.3920e-05, 8.2991e-33]])
```

* tensor에서 사용되는 데이터는 대표적으로 아래와 같다.
    * torch.float32, torch.float
    * torch.float64, torch.double
    * torch.int32, torch.int

* 위 방법처럼 torch 생성 인자에 size 를 지정해도 되고 iterable(List, Tuple)혹은 numpy 객체를 이용하여 직접 값을 넣어 초기화 또한 가능하다.
```python
import torch
n_array = np.random.rand(3,2)
np_tensor = torch.tensor(n_array, dtype=torch.float32)
print(np_tensor)

it_tensor = torch.tensor([[1, 2, 3], [2, 3, 4]])
print(it_tensor)

## result
# tensor([[0.1308, 0.4890],
#        [0.7342, 0.2908],
#        [0.3934, 0.3642]], dtype=torch.float64)
# tensor([[1, 2, 3],
#        [2, 3, 4]])
```

* 책에 따르자면 pytorch verson이 `>=0.4.0` 인 tensor경우 `torch.tensor()` 사용을 권장하고 있다.
* [pytorch_document-tensor](https://pytorch.org/docs/stable/tensors.html)에 따르자면 사이즈가 작은 tensor 를 다량으로 생성되면 Memory Overhead 이슈가 발생되니 하나의 큰 tensor 구조로 사용을 권장하고 있다.
* 그 외 tensor 생성은 option 사용이 권장되고 있다. 옵션은 [pytorch_document-tensor-option](https://pytorch.org/docs/stable/torch.html#tensor-creation-ops)에서 확인할 수 있다.


### tensor calculate operation ###
**연산 후 tesnor 객체 내용이 변하거나 계산값만 반환하고 원본 tensor는 그대로이거나**

* tensor 계산 method는 아래와 같이 큰 분류로 나누어진다
    * in-place : tesnor 원본에 연산이 적용되어 연산 후 tensor 값이 변화된다. 쉽게 이해하자면 `i += y` 수식이라 생각하면 편하다.
        * ex) zero_(), add_() eta... 

    * functional : tensor 를 복사하여 연산을 수행하기에 tensor 값은 변하지 않는다.
        * ex) zero(), add()

#### in-place 예시 ####
```python
import torch
x = torch.rand(1) # random으로 1x1 tensor 생성
y = torch.rand(1) # random으로 1x1 tensor 생성

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
x = torch.rand(1) #random으로 1x1 tensor 생성
y = torch.rand(1) #random으로 1x1 tensor 생성

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

### tensor calcualte space define ###
**tensor 연산을 실행하는 주체를 결정한다**
보통 컴퓨터의 연산들은 cpu가 담당하지만, matrix 와 같은 데이터는 병렬처리 및 연산이 빠른 GPU가 담당할 수 있다.

* 연산 주체는 다음과 같이 설정할 수 있다.
```python
import torch
cuda0 = torch.device('cuda:0')
x = torch.rand(1).to(cuda0) # tensor 계산 주체를 cuda 0 로 설정
```
cuda:0 은 컴퓨터의 `GPU 0`번을 쓰겠다는 의미이다. GPU가 많다면 0번부터 n 번까지 설정할 수 있다.

주의할 점으론 실제 쿠다에 tensor 가 생성되는 것은 아니고, CPU에 tensor를 생성하고 이를 GPU에 복사한 후 사용되는 형식이다.

