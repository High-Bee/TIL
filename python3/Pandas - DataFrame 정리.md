

# Pandas

## Data Frame 

> DataFrame : Series를 모아서 Table 형태로 구성한 자료구조
>
> * 밑줄 부터` DF`라 표현

###  DF 를 가장 간단하게 만드는 방법부터 알아보자.

```python
import numpy as np
import pandas as pd

# dict를 생성
data = {"names" : ["홍길동", "김길동"],           #학생이름
        "year" : [2015, 2016],                   #입학연도
        "points" : [3.9, 4.5]} ## => JSON        #평균평점

df = pd.DataFrame(data)
display(df) # jupyter notebook에서 DataFrame보는 함수(print도 가능)

```

```reStructuredText
	names	year	points
0	홍길동		2015	3.9
1	김길동		2016	4.5
```

---



### DF 형태와 각  값에 대해  알아보자.

```python
print(df.values) # -> [['홍길동' 2015 3.9]
			    #    ['김길동' 2016 4.5]]
print(df.shape) # 데이터의 형태. -> (2, 3)
print(df.size) # 값의 개수 -> 6
print(df.ndim) # 차원의 수 -> 2

print("DataFrame의 index : {}".format(df.index))
# DataFrame의 index : RangeIndex(start=0, stop=2, step=1)
print("DataFrame의 index[0] : {}".format(df.index[0]))
# DataFrame의 index[0] : 0
print("DataFrame의 column : {}".format(df.columns))
# DataFrame의 column : Index(['names', 'year', 'points'], dtype='object')
print("DataFrame의 column[1] : {}".format(df.columns[1])) 
# DataFrame의 column[1] : year
```

---



###  DF의 index와 column에 이름을 부여해 보자.

```python
df.index.name = "sNum"
df.columns.name = "학생정보"
display(df)  
# 이런 표현은 잘 사용하진 않는 것 같다.
```

```reStructuredText
학생정보	names	year	points
sNum			
0		홍길동		2015	3.9
1		김길동		2016	4.5
```

---



### DF생성하는 법 중 File(CSV)를 읽어와 DF 생성하기

```python
import pandas as pd

df = pd.read_csv("./data/students.csv")
display(df)
```

```reStructuredText
	이름	 입학년도	성적
0	홍길동	   2015		3.5
1	최길동	   2017		4.2
2	신사임당  2013	   4.1
3	강감찬	   2011		1.3
```

---

## API를 이용해 DF 만들어 보기

1. 영화진흥위원회의 일일 박스오피스 정보를 이용해 DF 만들기
2. JSON형태로 추출해 분석하여 원하는 형태의 DF 생성

```python
import numpy as np
import pandas as pd
import urllib # network접속을 하기 위해서 필요
import json   # open API의 결과가 JSON을 읽어들이기 위한 module

k_val = "{나의 key값}"
n_date = "20191120"
movie_url = "http://www.kobis.or.kr/kobisopenapi/webservice/"+\
            "rest/boxoffice/searchDailyBoxOfficeList.json?"+\
            "key={}&targetDt={}".format(k_val, n_date)
        # " +\ "는 줄을 띄울때 연결첨자로 쓴다.
        
m_page = urllib.request.urlopen(movie_url) # 결과 JSON 문자열이 들어있는 page 객체
print(m_page) # -> <http.client.HTTPResponse object at 0x0000022A952606A0>

```

* 원하는 부분을 추려 DF로 만들어 보자.

```python
## 순위, 영화제목, 당일매출액 DF 생성
json_page = json.loads(m_page.read())
n_data = json_page["boxOfficeResult"]['dailyBoxOfficeList']
df = pd.DataFrame(n_data)
cut_df = df[["rank","movieNm","salesAmt"]]
display(cut_df)
```

```reStructuredText
	rank	movieNm				salesAmt
0	1	블랙머니				878324600
1	2	신의 한 수: 귀수편		   337306650
2	3	82년생 김지영			172048320
3	4	터미네이터: 다크 페이트	 122297470
4	5	엔젤 해즈 폴른			99257540
5	6	좀비랜드: 더블 탭		    67783560
6	7	윤희에게			  	 47291900
7	8	날씨의 아이				46296130
8	9	아이리시맨				22784120
9	10	아담스 패밀리			    16427100
```

### Pandas의 통계 요약 

```python
import pandas as pd
data = {"이름" : ["홍길동", "신사임당", "강감찬", "을지문덕"],
        "학과" : ["컴퓨터", "영어영문", "기계", "수학"],
        "학년" : [1, 3, 4, 2],
        "학점" : [1.5, 4.5, 2.2, 3.5]}

df = pd.DataFrame(data)
display(df.describe())
```

```reStructuredText
			학년		학점
count	4.000000	4.000000
mean	2.500000	2.925000
std		1.290994	1.337597
min		1.000000	1.500000
25%		1.750000	2.025000
50%		2.500000	2.850000
75%		3.250000	3.750000
max		4.000000	4.500000
```

* 결측치 설명

>**R**
>
>R에서 NA(Not Available)는 결측치
>R에서 NULL은 값이 존재하지 않음을 의미
>R에서 NaN(Not available Number)
>수학적으로 불가능함을 의미
>
>**Python**
>
>Python pandas에서 NaN (Not a Number) missing data를 지칭
>Python pandas의 NaN => R의 NA
>NULL은 Python에서 None으로 표현
>a == None (x)       a is None (o)
>
>np.nan을 이용해 NaN을 생성할 수 있다.

---

### DF의 column을 추출

```python
import numpy as np
import pandas as pd
import warnings

warnings.filterwarnings(action="ignore") # "default" <= warning을 켠다!
                                         # "ignore" <= warning을 끈다!

data = {"이름" : ["홍길동", "신사임당", "강감찬", "을지문덕"],
        "학과" : ["컴퓨터", "영어영문", "기계", "수학"],
        "학년" : [1, 3, 4, 2],
        "학점" : [1.5, 4.5, 2.2, 3.5]}

df = pd.DataFrame(data,
                  columns=["학년","학과","이름","학점","등급"],
                  index=["one","two","three","four"])

# 특정 column 들고오기 
# print(df["이름"]) # column명으로 indexing => Series로 리턴
# print(df.이름) # 가능하다!

## 주의해야 할 점
student_names = df["이름"] # view를 생성
student_names["three"] = "최길동" # view를 통해서 수정
print(student_names) 
print("=="*30)
display(df)  # 원본이 수정됨
```

```reStructuredText
one       홍길동
two      신사임당
three     최길동 
four     을지문덕
Name: 이름, dtype: object
===================================================
	  학년	학과		이름		학점	   등급
one		1	컴퓨터		홍길동		1.5		NaN
two		3	영어영문   신사임당	   4.5 		NaN
three	4	기계		최길동		 2.2	 NaN
four	2	수학		을지문덕	3.5		NaN
```

```python
display(df[["이름","학년"]]) # Fancy Indexing => 결과 DataFrame
                            # 당연히 view로 처리!
```

```reStructuredText
		이름		학년
one		홍길동		 1
two		신사임당	3
three	강감찬		 4
four	을지문덕	2
```

### DF의 column 삭제

```python
# del df["등급"] # <= 이렇게 지울 수 있지만  안쓴다!!
new_df = df.drop("등급", axis=1, inplace=False) 
# inplace=True   
# inplace True는 원본을 삭제, return값이 없다
# inplace False는 원본 변경 x, 삭제된 DataFrame return
```

```reStructuredText
	 학년		학과		이름		학점
one		1	컴퓨터		홍길동		1.5
two		3	영어영문   신사임당	   4.5
three	4	기계		강감찬		 2.2
four	2	수학		을지문덕	3.5
```

### DF의 row indexing

<h6>data = {
    "이름" : ["홍길동", "최길동", "이지안", "박동훈"],
    "학과" : ["컴퓨터", "철학", "영어영문", "의학"],
    "학년" : [1, 3, 4, 2],
    "학점" : [3.1, 2.4, 4.5, 3.3]
    }</h6>

```python
df = pd.DataFrame(data,
                  columns = ["학과", "학년", "이름", "학점", "등급"],
                  index = ["one", "two", "three", "four"] )
# df[] column은 slicing 할 수 없다.
# df[2] # column은 숫자 index로 들고 올 수 없다!
        # DataFrame에 대한 indexing에서 숫자를 이용하는
        # 경우는 row indexing
        
# df[1:]
# df[1:-1] # 일반적인 slicing 기법을 적용할 수 있다. 
# df[[0,3]] # 숫자를 이용하는 indexing에서 fancy indexing은 지원하지 않는다.
```























### 의도치 않는 에러 처리법

```python
# 의도치 않는 에러가 발생될 경우가 있다.
# 프로그래밍 단계에서 문제는 없지만
# 실행시 문제가 발생할 수 잇는 코드들이 있다!

# Exception Handling 

try:
    10/0 # Exception이 발생 => 극복해서 프로그램이 중지되지 않도록
         # 처리해 보자!
except Exception as inst:
    print(inst) # 예외상황에 대한 내용을 출력
finally:
    print("hoho") # 문제가 있건 없건 무조건 출력
```

```reStructuredText
division by zero 	# <- error code
hoho
```







