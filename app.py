from flask import Flask, render_template, jsonify, request, flash
from pymongo import MongoClient

app = Flask(__name__)
app.config["SECRET_KEY"] = "ABCD"

client = MongoClient('localhost', 27017)
db = client.jranking

@app.route('/')
def home():
    return render_template('signup.html')

# 회원가입
@app.route('/signup', methods=['POST'])
def postUser():
    if request.method == 'POST':
        id = request.form['id']
        password = request.form['password']
        name = request.form['name']
        classroom = request.form['classroom']
        
        # 이름 입력 확인
        if name == '':
            flash("이름을 입력해주세요!")
            return render_template('signup.html')
        
        # id 중복 확인
        temp = list(db.users.find({}))
        for user in temp:
            if id in user['id']:
                flash("중복된 ID입니다!")
                return render_template('signup.html')
        
        # pw 길이 확인
        if len(password) < 8:
            flash("8글자 이상의 비밀번호를 입력해주세요!")
            return render_template('signup.html')
        
        # db에 저장
        db.users.insert_one({'id':id, 'pw':password, 'name':name, 'classroom':classroom, 'total':0, 'token':''})
        flash("가입이 완료되었습니다!")
        return render_template('signup.html')
    else:
        return render_template('signup.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)