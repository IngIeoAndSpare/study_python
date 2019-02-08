python 2일차 정리노트

대 용량 파일, 메모리 요구 시 iterator 사용

파일을 읽을 경우 한번에 메모리에 올리지 않고 fseek 단위로 읽고 처리한다. 나머지 부분은 return하고 대기.

iterator 의 중요한 기능중 하나 -> next

매우 큰 데이터 구조는 genartor 형식으로 정의한다.
ex) for i in xrange(100000)

enumerate - 리스트에서 인덱스. value를 튜플 형식으로 반환해줌
~~~~{.python}
    test = ['a','b','c']
    for i in enumerate(test) :
        print(i)
    ##결과
    (0, 'a')
    (1, 'b')
    (2, 'c')
~~~~

파이썬에서 object 생성 (class)
~~~~{.python}
    class Tree:
        x = 0
        y = 0
~~~~
주의할 점은 class의 이름 명명은 앞이 uppar cass 로 되어야 함.

여기서 파이썬의 특징은 class를 생성 하고 후에 className.새로운변수 로 정의가 또 가능하다. (무엇)

또한 private prototype 메소드를 정의가 가능하다. 마찬가지로 init function을 사용 가능하다

~~~~{.python}
    class Tree:
        x = 0
        y = 0
        def __init__(self, params1 = 1, params2 = 2): # =1, =2 는 옵션
            self.params1 = params1
            self.params2 = params2

    ... 다른 곳에서..
    Tree(params1, params2) #초기화
~~~~

다른 특이한 함수 몇 가지
string 문자열을 출력하고 싶을 때 '__str__' 이름 형식을 지키며 사용한다.
other 부분은 다른 class를 가지고 이용한다.

~~~~{.python}
    #위 코드 이어서..
    def __str__(self):
        return 'x => {}  || y=> {}'.format(self.params1, self.params2)

    def distance(self, other):
        return 'self => {} , {}   other => {}, {}'.format(self.parmas1, self.params2, other.params1, other.parmas2)
~~~~

파이썬은 정의된 클래스가 같으면 더할 수도 있다.
예컨대...

~~~~{.python}
    #위 코드 이어서..
    g1 = Tree(1,2)
    g2 = Tree(3,5)
    g3 = g1 + g2
~~~~



- escape 종류
1. \r : carriage return
1. \n : new line
1. \t : tab

- OS 별 EOL 종류
1. \r\n : window
1. \r : mac
1. \n : linux

- list function
1. remove : value remove in list
1. append : value append in list last index
1. pop : remove index and return remove value. params - index
1. sort : sorting. but not return.
1. reverse : desc sorting. but not return.

- tuple function
1. index : return value. params - index
1. count : check value count. return count

- set function
1. add : add value. but duplicate case is not add value

- dictionary 특징
1. key 값은 거진 다 들어가나 list, set, dictionary 는 불가

- string parser 에 사용되는 funtion
1. join : param - list , 리스트에 있는 아이템을 join 하여 return
1. rstrip : 특정 문자 제거 (EOS...) ex) 'test'.rstrip('\n') 같은..
1. list comprehensiion  : for 문 내부 for 문을 돌리는 경우
 -> [str(i) for i in myarray] : list 내부에 for문 loop 문 포함

~~~~{.python}
    values = range(100)
    values = [ix for ix in values if ix % 11 == 0]
    print(values)
    ##결과 : [0, 11, 22, 33, 44, 55, 66, 77, 88, 99]
~~~~

- list 특징
1. 다음과 같은 연산이 가능하다 [0] *4 => [0,0,0,0]
1. 다음과 같은 연산이 가능하다. [[0]*4]*2 => [[0,0,0,0], [0,0,0,0]]
1. 다항 리스트를 사용할 경우 numpy 기능을 사용하여 정의한다

- 조건문, loop 문
1. if, elif, else
1. for i in [1,2,3] :
1. while 조건 : ...
1. break, pass, continue

- exception handling
1. try - catch   -> try :    catch :


두개를 비교해보자. 어떤게 옳은 방법인지는 알겠지 뭐
~~~~{.python}
fileName = 'fileName.txt'
if os.path.exists(fileName) :
    outfile.write('myfile'\n')
else :
    outfile = open(myfilename, 'w')
    outfile.write('myfile'\n')

try:
    outfile.write('myfile'\n')
except :
    outfile = open(myfilename, 'w')
    outfile.write('myfile'\n')
~~~~


파이선 function 정의

def functionName (parmas...) :

특이하게 초기값을 params 에 정의할 수 있다.
ex) def add (x, y=4)
-> add(4) // add(4,7) 일 떄 값이 다르다.

module importing
-> 상단에 import string 같은거

Iterator - 일정한 변수 형식 컨버전 (나중에 찾아볼 것)

ex) test = iter([1,2,3,4])
    next(test) -> 결과값 1
    next(test) -> 결과값 2 ...

+ generator
    내부 value 를 yield객체에 담아 사용한다.
    next 로 하나씩 access 하여 사용함. (큰 용량에서 효율적으로 메모리 관리를 할 수 있음)


list, tuple 에선 맴버쉽 체킹을 하면 속도가 느리다. 
이 경우 numpy 패키지 사용하여 num 타입으로 변경하는 것이 좋음. (C 타입으로 define 되어 있으니까...)

