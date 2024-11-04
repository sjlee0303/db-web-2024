from flask import Flask, render_template

app = Flask(__name__)

# 경로를 지정하는 것
@app.route('/') # 데코레이트는 hello 라는 함수를 가져가서 껍데기를 붙여주는 것..?
@app.route('/hello/') # 하나의 함수에 여러 개 경로를 지정할 수 있음
@app.route('/hello/<string:name>/') # 이 경로에 변수를 추가할 수 있음
def hello(name=None):
#    mydoc = ""
#    mydoc += "<h1> Hello, World! </h1>"
#    mydoc += "<h2> Welcome to my </h2>"
#    if name:
#        mydoc += f"<p>Hello, {name} World!</p>"
#    else :
#        mydoc += "<p>Hello, World!</p>"
#    return mydoc

    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)

    # 여기까지하면 application이 하나 완성된 것
    # 실행 : python ./hellowebapp.py
    # 이후 127.0.0.1:5000 이거 주소 웹 사이트 검색하면 됨
    # 근데, not found 404 떠서 def hello() 함수 만들어야 함(?)
    # Hello, World라고 하는 html 문서를 보낸 것! 그래서 not found 404 에러가 안나는 듯

    # 127.0.0.1:5000/hello/leeseojin/ 이런식으로 
    # 경로 값에 변수 값을 집어넣으면 이 변수 활용해서 처리할 수 있음