# Linear Regression

> Machine Learning의 지도학습 방법 중 가장 기본이 되는 학습 방식
>
> 학습 : 해당 데이터를 이용해 모델(데이터에 가장 근접한)을 가장 정확히 만들어 가는 것

|  X   | Y(label) |
| :--: | :------: |
|  1   |    1     |
|  2   |    2     |
|  3   |    3     |

* 일반적으로, 많은 현상(Data)들이 linear한 형태를 가진다.
  + 많은 시간을 공부하면 시험성적이 높다!
  + 오랜시간 일을 하면 돈을 더 많이 번다!
  + 공을 세게 던지면 더 멀리 날라간다!
  + 배달지역이 멀면 배달시간은 더 걸린다!



* 우리의 예제도 이러한 linear 형태라고 가정한다.
  * 하나의 가설을 만들 수 있다
  * 이 가설을 수정해 나가면서 데이터를 가장 잘 표현하는 형태의 가설을 완성해 나가는 과정 => 학습

* 이 가설을 수정해 나갈 때 최소제곱법이라는 방식을 이용한다!
* 가설과 데이터의 간격의 제곱의 평균을 구해서 이 값이 작은 가설이 더 좋은 가설이라고 선언
  * 최소값은 0
  * 가설과 데이터의 간격의 제곱의 평균을 구하는 일반식 => 비용함수(Cost function, Loss function)

- 비용함수 =


$$
Cost(W, b) = \frac{\ 1}{\ n}\sum_{i=1}^n(H(x_i)-y_i)^2
$$

---

지금까지 설명한 내용을 코드로 표현해 보자!

- Google의 Tensorflow를 이용해 보자!

- package 설치!

  ```python
   pip install tensorflow==1.5.0
  ```

  

  





