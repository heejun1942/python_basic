from flask import Flask, escape, request, render_template
import random

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

#/hi로 접속하면 hi()함수가 실행됨.
@app.route('/hi')
def hi():
    name = "김희준"
    return render_template('hi.html', html_name = name)

@app.route('/greeting/<string:name>/')
def greeting(name):
    def_name=name
    return render_template('greeting.html',html_name=def_name)

# 연산은 되도록 여기서 끝낸 후 보내주자. (html에서 연산 노노~)
@app.route('/cube/<int:num>')
def cube(num):
    def_num = num
    def_cube = num**3
    return render_template('cube.html',html_num=def_num,html_cube=def_cube)

@app.route('/dinner')
def dinner():
    menu = ['삼각김밥', '컵라면', '스테이크', '마라탕', '훠궈']
    dinner=random.choice(menu)
    menu_img= {'삼각김밥' :"http://www.ourhometfs.co.kr/file/GoodImage/1/41015889.jpg",
                '컵라면' :"https://t1.daumcdn.net/cfile/tistory/99A7CB355A4B982A03",
                '스테이크' : "https://img.huffingtonpost.com/asset/5bf24ac824000060045835ff.jpeg?ops=scalefit_630_noupscale", 
                '마라탕' : "https://post-phinf.pstatic.net/MjAxOTA2MDRfNTYg/MDAxNTU5NjU5Njg3MjI0.SXzII9y0bWdJRel9fu2XknxNFrp8f6ok5HuFkq-6oNIg.yZ10p8eTr1GHFNlz8MN80UB2o8FHlPU7jgp1sl5qfJEg.JPEG/111.jpg?type=w1200", 
                '훠궈' :"http://cfs7.tistory.com/upload_control/download.blog?fhandle=YmxvZzU0MDg5QGZzNy50aXN0b3J5LmNvbTovYXR0YWNoLzAvMzYuanBn" }
    img_url = menu_img[dinner]
    return render_template('dinner.html', dinner=dinner, img_url=img_url)

@app.route('/movies')
def movies():
    movies= ['조커','겨울왕국2','터미네이터','어벤져스']
    return render_template('movie.html', movies=movies)


if __name__=="__main__":
    app.run(debug=True)
