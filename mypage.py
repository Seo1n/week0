import datetime
from flask import Blueprint, request, jsonify
from pymongo import MongoClient
from bson.json_util import dumps
from flask import Flask, render_template,request, make_response, flash, redirect
from flask_jwt_extended import (
    JWTManager, create_access_token, create_refresh_token)

mypage_bp = Blueprint('mypage', __name__)

client = MongoClient('mongodb://test:test@localhost',27017)
db = client.jranking

@mypage_bp.route("/mypage", methods=['GET'])
def mypage():
    # 1. 내 정보 보여주는 곳
    # DB에서 refresh token 가지고 user id 정보 불러오기
    # 해당 id를 가지고 저장된 모든 데이터를 list로 불러오기
    # 날짜 시작시간 종료시간 데이터 넘겨주기
    
    token = request.cookies.get('refresh_token')
    user = db.users.find_one({'token' : token},{'_id' : False})
    user_id = user['id']
    total = user['total']
    cursor = db.times.find({'id': user_id}).sort('_id', -1)
    
    # 개인 일일 공부시간 평균
    timelist = list(db.times.find({'id': user_id},{'_id':False}))
    temp = []
    cnt = 0
    for i in timelist:
        if i['date'] not in temp:
            cnt += 1
            temp.append(i['date'])
    if cnt != 0:
        peravg = total // cnt
    else:
        peravg = 0
        
    # 전체 일일 공부시간 평균
    users = list(db.users.find({},{'_id':False}))
    tempavg = 0
    for i in users:
        temp_id = i['id']
        temptotal = i['total']
        times = list(db.times.find({'id': temp_id},{'_id':False}))
        temp = []
        cnt = 0
        for j in times:
            if j['date'] not in temp:
                cnt += 1
                temp.append(j['date'])
        if cnt != 0:
            tempavg += temptotal // cnt
        else:
            peravg = 0
    if len(users) != 0:
        allavg = tempavg // len(users)
    else:
        allavg = 0   
        
    my_data = []
    for document in cursor:
        my_data.append(document)
    
    # 2. 모든 정보 불러와서 평균내기 
    # 2-1. 1위 시간에서 내시간 빼서 보여주기 
    cursor_all = db.users.find({})
    all_data = []
    for document in cursor_all:
        all_data.append(document)
    
    all_data.sort(key=lambda x: x.get('total'),reverse=True)
    number_one = all_data[0]['total'] - user['total']
    
    
    
    
    return render_template('mypage.html', mydata = my_data, number_one= number_one, total = total, average = peravg, total_average = allavg)

    # 2-2 나의 일일 평균 공부 시간 보여주기
    # 해당 id를 가지고 저장된 모든 데이터를 list로 불러와서,
    # 날짜별로 join 하고 
    # 총 날짜별 length 체크해서 
    # 총 합산 시간 / length 
    # my_data
    
    # 2-3 전체인원 일일 평균 공부시간 보여주기
    # 모든 데이터에서 날짜별로 join 
    # 모든 데이터의 총 합산 시간 / 날짜 length
    # return render_template('mypage.html', mydata = my_data_json, number_one = number_one )

