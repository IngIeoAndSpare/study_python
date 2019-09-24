## 2week ##

* function define
    - input : str 형태의 input method

* class define
```python
class CalculrationModule:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def add(self):
        return self.number1 + self.number2
```

    - self : javascript 의 this와 같은 존재. 모든 params의 한정자로 쓰인다
    - __init__ : 변수 초기화 생성자

만약 위 클래스를 다른 곳에 사용한다고 한다면 다음과 같이 선언한다.
```python
from Calculration import CalculrationModule
or
from Calculartion import *
or
from Calculartion import {{METHOD_NAME}}, {{METHOD_NAME}}
```


* regression analysis
    - 측정된 데이터를 표현할 수 있는 함수를 찾는 과정
    - 머신러닝에선 모델이라고 명한다
    - data를 target이라 하며 cost함수를 loss function 이라 한다.
    - underfitting : 모델이 적게 data fitting된 경우. 대표성이 떨어진다. 
    - overfitting : 모델이 과하게 data fitting된 경우. 데이터 규칙설명X

    