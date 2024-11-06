from flask import Flask, render_template, request, redirect
import sqlite3
# restaurant_menu.db 올려주신거 sqlite 에서 사용하는?? db인듯

app = Flask(__name__)

@app.route('/')
@app.route('/restaurants/')
def showRestaurants():
    db = sqlite3.connect('restaurant_menu.db')
    cursor = db.cursor()
    items = cursor.execute('SELECT id, name FROM restaurant').fetchall()
    # restaurant라는 테이블에서 name이라는 애트리뷰트를 불러오겠다는 것
    # 이후, items 라는 변수에 저장

    db.close()
    print(items)
    return render_template('restaurants.html', restaurants=items)

@app.route('/restaurants/')
def newRestaurants():
    return "This page will be for making a new restaurant"

@app.route('/restaurant/<int:restaurant_id>/')
def showMenu(restaurant_id):
    return f"All menu items for restaurants {restaurant_id}"

# 새로운 값 추가하는 페이지
# default로는 get만 받아들이는데 POST도 같이 받겠다고 정의해 줘야 함.
@app.route('/restaurant/new/', methods=['GET','POST']) 
def newRestaurant():
    # 조건문으로 get, post를 구분해서 처리해야 함.
    if request.method == 'POST':
        db = sqlite3.connect('restaurant_menu.db')
        cursor = db.cursor()
        cursor.execute('INSERT INTO restaurant (name) VALUES (?)', (request.form['name'],))
        db.commit() # 데이터 베이스에 변경을 가하면 commit을 해야함. 이거를 해야 디스크에 완벽히 저장됨
        db.close() # 데이터 베이스 종료
        return redirect('/restaurants/') # 여기에서 저기 주소?로 이동하고 끝남
    #else:
    
    return render_template('restaurant_new.html')

@app.route('/restaurants/<int:restaurant_id>/delete/')
def deleteRestaurant(restaurant_id):
    return f"This page will be for deleting restaurant {restaurant_id}"


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)

# flask 웹 사이트나 html 사이트? 참고해서 하기

# !!프로젝트!!
# < 개발 과정의 기록 >
# git user.name 과 user.email 은 실제 이름과 이메일을 사용할 것
# git log 에서 확인이 가능하여야 함

# ( 평가 항목 )
# 웹 응용의 기능
#Database를 적절히 설계하였으면 데이터 접근..