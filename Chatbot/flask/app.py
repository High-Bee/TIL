from datetime import datetime 
from flask import Flask, render_template, request
import random
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello World!~~!!'
@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route("/mulcam")
def mulcam():
    return '20층 skylounge!!'

@app.route("/dday")
def dday():
    today = datetime.now()
    new_year = datetime(2020, 1, 1)
    result = new_year - today
    return f"농익을 때까지{result.days}일 남았습니다!"

# 인사하는 페이지
@app.route("/greeting/<string:name>")
def greeting(name):
    # return f"반갑습니다. {name}님! :)"
    return render_template("greeting.html", html_name = name)

# 세제곱의 결과 돌려주는 페이지
@app.route("/cube/<int:number>")
def cube(number):
    result = number**3
    # return f"{number}의 세제곱 값은 {number**3}입니다."
    return render_template("cube.html", number = number , result = result)

# 인원 수에 맞게 메뉴를 추천해주는 페이지
@app.route("/lunch/<int:people>")
def lunch(people):
    menu = ["보쌈","족발","대게","가츠동","소오오오주","사아아아아케에에에에"]
    order = random.sample(menu, people)
    
    return str(order)



@app.route('/movie')
def movie():
    movies = ["장고", "바스터즈:거친녀석들", "조커", "세븐"]
    return render_template("movie.html", movies_t = movies)



@app.route("/ping")
def ping():
    return render_template("ping.html")


@app.route("/pong")
def pong():
    age = request.args.get("age")
    return render_template("pong.html", age = age)


@app.route("/naver")
def naver():
    return render_template("naver.html")

@app.route("/google")
def google():
    return render_template("google.html")







## app.py 가장 하단에 위치
# 1. 앞으로 flask run으로 서버를 켜는게 아니라,
# python app.py로 서버를 실행한다.
# 2. 내용이 바뀌어도 서버를 껐다 켜지 않아도 된다.

if __name__ == '__main__':
    app.run(debug=True)
