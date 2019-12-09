Python Numpy

> NumPy ( Numerical Python )
>
> 수학적 계산을 할 때, 수치연산을 할 때 사용됨.
>
> R의 vector를 사용하는 것 처럼 NumPy를 이용할 수 있다!
>
> Vector연산, Matrix연산을 빠르고 효율적으로 처리할 수 있다!
>
> Pandas, Matplotlib의 기본 Module이 NumPy
>
> NumPy module은 ndarry(n-dimensional array)라고 불리는 
>
> 자료구조를 이용한다. => R에서 Vector와 유사 (NumPy에서는 싹다 ndarray라고 함)
>
> R의 Vector자료구조는 같은 데이터 타입을 저장하는 구조
>
> ndarray도 같은 데이터 타입만 저장이 가능
>
> NumPy의 ndarray를 이용하려면 NumPy module이 설치되어야 한다!
>
> module을 설치할 때 conda명령어 이용해서 설치가능 (conda에서만 가능 but conda이용 시 conda로 설치 권장)
>
> python은 pip를 이용해서 module을 설치 (위에와 2가지 이용가능)

* 아래의 명령어로 설치하자!

```conda
conda install numpy
```



* ### Jupyter notebook

```python
import numpy as np
## ndarray를 생성하고 data type을 살펴보자

## python list
a = [1,2,3,4]
print("1. list => {}, type => {}".format(a,type(a)))
print("2. list[0] => {}, type => {}".format(a[0],type(a[0])))

## NumPy ndarray
b = np.array(a)
print("1. ndarray => {}".format(b))
print("2. ndarray type => {}".format(type(b)))
print("3. ndarray dtype => {}".format(b.dtype))
## int32 => 정수형이고 32bit로 구성되어 있다!.
## 2진수로 32개의 bit로 표현할 수 있는 최대 수
# 2진수 1개로 표현할 수 있는 수는 2 => 2 ** 1
# 2진수 2개로 표현할 수 있는 수는 4 => 2 ** 2
# 2진수 3개로 표현할 수 있는 수는 8 => 2 ** 3
# 2진수 32개로 표현할 수 있는 수는 ? => 2 ** 32
## int64를 이용하면 더 큰 수를 표현할 수 있다!

## NumPy ndarray를 만드는 가장 간단한 방법 => NumPy가 제공하는 array()함수 이용
c = np.array([100, "Hello", 3.14])
print(c) # 모두 같은 daya type이 되어야 한다!(R처럼 but 우선순위가 아닌 변환이 가능한 type으로!)
print(c.dtype)
print(type(c[0]))
```

```
1. list => [1, 2, 3, 4], type => <class 'list'>
2. list[0] => 1, type => <class 'int'>
1. ndarray => [1 2 3 4]
2. ndarray type => <class 'numpy.ndarray'>
3. ndarray dtype => int32
['100' 'Hello' '3.14']
<U11
<class 'numpy.str_'>
```



* ### 다차원 numpy array를 만들어 보아요!

```python
myList = [[1,2,3],[4,5,6]]
arr = np.array(myList) # 2차원의 ndarray
print(arr)

## 1행 2열의 값은 얼마인가요? (2행 3열)
print(arr[1,2]) # print(arr[1][2]) 이런 형태로 쓰지 않는다!
## index시작은 0부터!!
## n차원의 ndarray가 어떻게 표현되는지 확인해야 한다!
## 기본 데이터 타입은 정수일 경우 int32로 사용된다.

print(arr.dtype)

## 만약 데이터타입을 지정하려면
# arr = np.array(myList, dtype="int64") # 그다지 좋지 않다.
arr = np.array(myList, dtype=np.float64) # 이렇게 사용한다.
print(arr.dtype)
print(arr)


```

```
[[1 2 3]
 [4 5 6]]
 
6

int32

float64
[[1. 2. 3.]
 [4. 5. 6.]]
```



*  ### 차원의 개수와 크기 및 axis

```python
# myList = [1,2,3,4] # 열
# myList = [[1,2,3],[4,5,6]] # 행, 열
# myList = [[1,2],[3,4],[5,6],[7,8]] 
myList = [[[1,2],[3,4]],[[5,6],[7,8]]]

arr = np.array(myList) # python list를 이용해서 numpy array 생성
## 이렇게 numpy array를 생성하면 차원의 개수를 알 수 있다.
print(arr.ndim) # 차원의 개수를 알려주는 속성
## 차원의 개수와 원소 개수를 동시에 알려주는 속성
print(arr)
print(arr.shape) # (4,) 1차원에 원소 4개 있다고 알려주는 의미
                 # (2,3) 2행 3열 의미
                 # (2,2,2) 2면 2행 2열

```

```
3
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
(2, 2, 2)
```



* ### numpy array 차원 제어

```python
myList = [1,2,3,4,5,6,7,8,9,10,11,12]
# myList = [[1,2,3],[4,5,6]]
arr = np.array(myList) # ndarray 생성
print("ndarray의 차원의 수는 : {}".format(arr.ndim)) # 차원의 수
print("ndarray의 shape : {}".format(arr.shape)) # 원소의 개수
# ndarray의 차원에 상관없이 모든 요소의 개수
print("ndarray의 요소개수 : {}".format(arr.size)) # 요소의 개수

# python의 len()함수는 ndarray에 대해 적용하면 
# 1차원의 요소개수를 리턴
print("ndarray의 len() : {}".format(len(arr))) # 1차원의 개수 ( 1차원이 2개 있는 것 )

# shpe을 변경할 수 있다!
arr.shape = (2,2,3) # tuple 괄호 생략가능
print(arr)

## 이렇게 shape을 변경할 수 있는데
## arr.shape을 직접 바꾸는 방식은 잘 사용되지 않는다.
## 다른 방식이 있다! reshape() 함수를 이용한다.
```

```
ndarray의 차원의 수는 : 1
ndarray의 shape : (12,)
ndarray의 요소개수 : 12
ndarray의 len() : 12
[[[ 1  2  3]
  [ 4  5  6]]

 [[ 7  8  9]
  [10 11 12]]]
```

