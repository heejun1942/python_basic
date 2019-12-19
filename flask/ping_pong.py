from flask import Flask, render_template, request
# 플라스크를 사용하는 파일의 이름은 app.py로 쓰기로 약속되어있음

app = Flask(__name__)

# /ping에서 보내서 /pong으로 받을것
# 전처리 후 넘겨주기.?

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    data=request.args.get("keyword")
    return render_template('pong.html', data = data)


# naver검색창으로 이동
@app.route('/naver')
def naver():
    return render_template('naver.html')

#google검색창으로 이동
@app.route('/google')
def google():
    return render_template('google.html')



# app을 디버그 모드로 실행할꺼야
# debug모드를 켜놓으면 저장할 때마다 자동으로 새로고침됨
if __name__=="__main__":
    app.run(debug=True)


