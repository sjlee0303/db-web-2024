from flask import Flask
import sqlite3
# restaurant_menu.db 올려주신거 sqlite 에서 사용하는?? db인듯

app = Flask(__name__)

@app.route('/')
@app.route('/restaurants/')
def showRestaurants():
    db = sqlite3.connect('restaurant_menu.db')
    cursor = db.cursor()
    items = cursor.execute('SELECT name FROM restaurant').fetchall()
    # restaurant라는 테이블에서 name이라는 애트리뷰트를 불러오겠다는 것
    # 이후, items 라는 변수에 저장

    db.close()
    print(items) # 터미널 창에 출력 됨. 결과는 파이썬의 튜플의 list로 옴
    
    # html 로 만들기
    mydoc = "<h1> All Restaurants </h1>"
    mydoc += "<ul>"
    for item in items :
        mydoc += f"<li>{item[0]}</li>"
    mydoc += "</ul>"
    return mydoc

@app.route('/restaurants/')
def newRestaurants():
    return "This page will be for making a new restaurant"

@app.route('/restaurants/<int:restaurant_id>/delete/')
def deleteRestaurant(restaurant_id):
    return f"This page will be for deleting restaurant {restaurant_id}"


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)