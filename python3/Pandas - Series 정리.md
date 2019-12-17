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

