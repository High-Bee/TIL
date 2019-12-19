# Pandas

> python 에서 가장 많이 사용되는 데이터 분석용 최적의 Library or Module
>
> 2가지로 정의된 데이터 타입 사용
>
> 1. Series : Numpy의 1차원 array와 유사
> 2. DataFrame : Series를 모아서 Table 형태로 구성한 자료구조

## pandas module 설치

```reStructuredText
conda install Pandas
```

```python
import numpy as np
import pandas as pd
```

## Series 생성

* ### Series 생성 전 Numpy array review

```python
# NumPy array( ndarray )와 비교해서 확인.
# 먼저 ndarray부터 다시 한번 알아보자!

arr = np.array([-1,5,3.14,14,"Hello"], dtype = np.object)

print(arr)
print(arr.dtype)
print(arr[2])
print(type(arr[2]))
```

```reStructuredText
[-1 5 3.14 14 'Hello']
object
3.14
<class 'float'>
```

* ### Series 구조 확인하기

```python
s = pd.Series([-1,5,3.14,14,"Hello"], dtype = np.object)

print(s)
print("=" * 30)

# 1. Series의 value 부분
print("1. Series의 value부분 : {}".format(s.values))
print("1. Series의 value부분의 Type: {}".format(type(s.values)))

# 2. Series의 data type(dtype)
print("2. Series의 value부분의 DType: {}".format(s.dtype))

# 3. Series의 Index 부분 출력
print("3. Series의 index 부분 : {}".format(s.index))
print("3. Series의 index type : {}".format(type(s.index)))
```

```reStructuredText
0       -1
1        5
2     3.14
3       14
4    Hello
dtype: object
==============================
1. Series의 value부분 : [-1 5 3.14 14 'Hello']
1. Series의 value부분의 Type: <class 'numpy.ndarray'>
2. Series의 value부분의 DType: object
3. Series의 index 부분 : RangeIndex(start=0, stop=5, step=1)
3. Series의 index type : <class 'pandas.core.indexes.range.RangeIndex'>
```

* ### Series index 지정하기

> Series는 숫자 index가 기본으로 제공된다.

```python
s = pd.Series([-1,5,8,10],
               dtype = np.int32,
                 index = ["k","c","k","f"]) # 사용가능
print(s)     # 만약 찾으려는 index가 2개 이상 존재할 경우 그 결과가 Series로 return
print("=="*5) 
print(s[1])
print("=="*5)
print(s["k"])
```

```reStructuredText
k    -1
c     5
k     8
f    10
dtype: int32
==========
5
==========
k   -1       # index 값이 k 인 value가 Series로 return
k    8
dtype: int32
```

* ### Series index slicing 알아보기

```python
s = pd.Series([-1,5,8,10],
               dtype = np.int32,
                 index = ["a","c","k","f"])

# ndarray에서 indexing 사용할 수 있고 slicing도 사용할 수 있다
# Series도 Slicing 이용할 수 있다.

print(s[0:2]) # Seires가 return
print("-"*10)
print(s["a":"k"]) # 새로운 index로 slicing 할 때 범위가 inc -inc 된다

print("-"*10)
print(s[s % 2 == 0]) # boolean indexing

print("-"*10)
print(s[0:2])

print("-"*10)
print(s.sum())
```

```reStructuredText
a   -1
c    5
dtype: int32
----------
a   -1
c    5
k    8
dtype: int32
----------
k     8
f    10
dtype: int32
----------
a   -1
c    5
dtype: int32
----------
22
```

* ### For문을 활용한 List 생성해보기

```python
myList = [1,2,3,4]

result = [x*2 for x in myList]
print(result)

result = [x*2 for x in myList if x > 2]
print(result)

# dict 에도 사용할 수 있다.

result = {"stu"+str(x) : x**2 for x in range(0,10)}
print(result)
```

```reStructuredText
[2, 4, 6, 8]
[6, 8]
{'stu0': 0, 'stu1': 1, 'stu2': 4, 'stu3': 9, 'stu4': 16, 'stu5': 25, 'stu6': 36, 'stu7': 49, 'stu8': 64, 'stu9': 81}
```

* ### Series를 활용한 예제

> A공장의 2019-01-01부터 10일간  제품 생샌량을  Series로 저장
> 생산량은 랜덤으로 결정. 평균이 50이고 표준편차가 5인
> 정규분포에서 random하게 추출(정수로)
> 예) 2019-01-01 53 이런 형식
>
> B공장의 2019-01-01부터 10일간 제품생산량을 Series로 저장
> 생산량은 랜덤으로 결정 평균이 70이고 표준편차가 8인
> 정규분포에서 random하게 추출(정수)
>
> 모든공장의 날짜멸 생산량 (합계) 구하기

```python
today = parse("2019-01-01")
day = timedelta(days=1)
maDay = today+day
result = [maDay for day in range(1,10)]
arrA = np.random.normal(50,5,(10,))

print(arrA)
aFact = pd.Series(arrA,
                     index = [today + timedelta(days=i) for i in range(10)])

print(aFact)
```

```reStructuredText
[44.8902773  48.2406229  47.37823364 40.40731753 52.89180003 48.49049076
 51.07521087 55.32518807 49.31124606 53.81910781]
2019-01-01    44.890277
2019-01-02    48.240623
2019-01-03    47.378234
2019-01-04    40.407318
2019-01-05    52.891800
2019-01-06    48.490491
2019-01-07    51.075211
2019-01-08    55.325188
2019-01-09    49.311246
2019-01-10    53.819108
dtype: float64 <- "정수형이 아니다!!"
```

### A Factory 생산량

```python
start_day = parse("2019-01-01")
aFactory = pd.Series([int(x) for x in np.random.normal(50,5,(10,))],
                     index = [start_day + timedelta(days=i) for i in range(10)]) # int 형으로 입력받기 / random.randint로 정수를 받을 수 도 있다.


```

