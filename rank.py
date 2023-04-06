from flask import Blueprint, request, jsonify
from pymongo import MongoClient
import json
from flask import Flask, render_template,request, make_response, flash, redirect
from flask_jwt_extended import (
    JWTManager, create_access_token, create_refresh_token)

rank_bp = Blueprint('rank', __name__)

client = MongoClient('mongodb://test:test@localhost',27017)
db = client.jranking

@rank_bp.route('/rank', methods=['POST', 'GET'])
def rank():
    token = request.cookies.get('refresh_token')
    if token is not None :
        users = list(db.users.find({}, {'_id' : False}).sort('total', -1))
        user = db.users.find_one({'token':token}, {'_id' : False})
        cnt = 0
        for i in users:
            cnt += 1
            if user['id'] == i['id']:
                break
        users_give = []
        newcnt = 0
        for temp in users:
            users_give.append(temp)
            newcnt += 1
            if newcnt == 5:
                break
        return render_template('rank.html', ranker = users_give, user = user, rank = cnt)
    else :
        flash("로그인 정보가 없습니다.")
        return render_template('index.html')

@rank_bp.route('/rank/red', methods=['POST', 'GET'])
def red():
    token = request.cookies.get('refresh_token')
    if token is not None :
        allusers = list(db.users.find({}, {'_id' : False}).sort('total', -1))
        users = list(db.users.find({'classroom':'레드반'}, {'_id' : False}).sort('total', -1))
        user = db.users.find_one({'token':token}, {'_id' : False})
        cnt = 0
        for i in allusers:
            cnt += 1
            if user['id'] == i['id']:
                break
        users_give = []
        newcnt = 0
        for temp in users:
            users_give.append(temp)
            newcnt += 1
            if newcnt == 5:
                break
        return render_template('rank.html', ranker = users_give, user = user, rank = cnt)
    else :
        flash("로그인 정보가 없습니다.")
        return render_template('index.html')

@rank_bp.route('/rank/blue', methods=['POST', 'GET'])
def blue():
    token = request.cookies.get('refresh_token')
    if token is not None :
        allusers = list(db.users.find({}, {'_id' : False}).sort('total', -1))
        users = list(db.users.find({'classroom':'블루반'}, {'_id' : False}).sort('total', -1))
        user = db.users.find_one({'token':token}, {'_id' : False})
        cnt = 0
        for i in allusers:
            cnt += 1
            if user['id'] == i['id']:
                break
        users_give = []
        newcnt = 0
        for temp in users:
            users_give.append(temp)
            newcnt += 1
            if newcnt == 5:
                break
        return render_template('rank.html', ranker = users_give, user = user, rank = cnt)
    else :
        flash("로그인 정보가 없습니다.")
        return render_template('index.html')

@rank_bp.route('/rank/green', methods=['POST', 'GET'])
def green():
    allusers = list(db.users.find({}, {'_id' : False}).sort('total', -1))
    token = request.cookies.get('refresh_token')
    if token is not None :
        users = list(db.users.find({'classroom':'그린반'}, {'_id' : False}).sort('total', -1))
        user = db.users.find_one({'token':token}, {'_id' : False})
        cnt = 0
        for i in allusers:
            cnt += 1
            if user['id'] == i['id']:
                break
        users_give = []
        newcnt = 0
        for temp in users:
            users_give.append(temp)
            newcnt += 1
            if newcnt == 5:
                break
        return render_template('rank.html', ranker = users_give, user = user, rank = cnt)
    else :
        flash("로그인 정보가 없습니다.")
        return render_template('index.html')