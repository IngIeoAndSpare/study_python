지난 일차 복습

- python 변수 종류
(int, float, string, boolean, none)
임의 초기화 가능, del 변수명 으로 삭제 가능

(list[], tuple(), set{}, dictionary{key:value})

- class 종류
(attribute, function, generator)

- for문
[i, j for i, j in enumerate(10)]

- list 팁
기본 연산은 상관 없으나 대용량 데이터를 핸들링 할 때에는 numpy 객체를 이용하여 연산속도를 개선할 수 있다. (numpy - c type lib)

물론 대용량이라면 R을 사용하긴 하지만..

진도
- numpy
~~~~{.python}
import numpy as np
~~~~
np.ones((1,1,1))
3차원 배열을 만든다. prams 에 따라서 차원이 다른 배열을 만든다

np.array([1,2,3])
1,2,3 array를 생성한다

np.inner(a,b) a, b 에 대한 inner 값을 구한다.


- file handler 
.read() : 파일 전체를 읽음
.readline() : 1줄만 읽음
.readlines() : 여러줄을 읽고 list 반환
.xreadlines() : iterator (work2.md 참고)
.write() : 전체 쓰기
.writeline() : 1줄 쓰기

~~~~{.python}
    import pickle
    import os

    data1 = {'a' : [1,2,3,4], 'b' : 10000, 'c': None}
    output = open('data.pkl', 'wb')
    pickle.dump(data1, output)
    output.close()
    pkifile = open('data.pkl', 'rb')
    data2 = pickle.load(pkifile)

    print(data2)
~~~~

pickle 실습. sync 을 할 수 있나?


데이터 파일 구분
-csv : comma 구분
-tsv : tab 구분

~~~~{.python}
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
~~~~

다음을 입력하여 StringIO 를 import 하자


- databases
SQL : structur query lang
OCP(oracle) : PL-SQL

