from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.jranking

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sign', methods=['POST'])
def sign_up():
    # 클라이언트로부터 데이터를 받기
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    name_receive = request.form['name_give']
    class_receive = request.form['class_give']

    user = {'id': id_receive, 'pw': pw_receive, 'name': name_receive, 'class': class_receive,
               'time': 0}

    # mongoDB에 데이터를 넣기
    db.users.insert_one(user)

    return jsonify({'result': 'success'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)