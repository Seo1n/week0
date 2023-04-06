from flask import Blueprint, request, jsonify
from pymongo import MongoClient
from flask import Flask, render_template,request, make_response, flash, redirect
from flask_jwt_extended import (
    JWTManager, create_access_token, create_refresh_token)

auth_bp = Blueprint('auth', __name__)

client = MongoClient('mongodb://test:test@localhost',27017)
db = client.jranking
    
# 로그인 기능 구현
@auth_bp.route('/login', methods=['POST'])
def login():
    id = request.form['id']
    password = request.form['password']
    user = db.users.find_one({'id' : id})
    
    if (user == None) or (user['password'] != password) :
        flash('아이디와 패스워드가 일치하지 않습니다.')
        return redirect("/")
    else :
        # DB에 access_token, refresh token 생성하기
        access_token = create_access_token(identity=id)
        refresh_token = create_refresh_token(identity=id)

        # DB에 refresh token 저장하기
        db.users.update_one({'id' : id},{'$set': {'token': refresh_token}})
        response = make_response(render_template('menu.html'))
        response.set_cookie('access_token', value=access_token)
        response.set_cookie('refresh_token', value=refresh_token)
        
        return response
    
# 로그아웃 기능 구현
@auth_bp.route("/logout", methods=['POST'])
def logout():
    token = request.cookies.get('access_token')
    response = make_response(render_template('index.html'))
    response.delete_cookie('access_token')
    response.delete_cookie('refresh_token')
    return response

@auth_bp.route('/signupbutton', methods=['POST'])
def signupbutton():
    return render_template('signup.html')

# 회원가입 기능 구현
@auth_bp.route('/signup', methods=['POST'])
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
        
        # id 입력 확인
        if id == '':
            flash("ID를 입력해주세요!")
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
        
        # 반 선택 확인
        if classroom == '---':
            flash("반을 선택해주세요!")
            return render_template('signup.html')
        
        # db에 저장
        db.users.insert_one({'id':id, 'password':password, 'name':name, 'classroom':classroom, 'total':0, 'token':''})
        flash("가입이 완료되었습니다!")
        return render_template('index.html')
    else:
        return render_template('signup.html')