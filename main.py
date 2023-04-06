from flask import Flask
from auth import auth_bp
from menu import menu_bp
from mypage import mypage_bp
from rank import rank_bp
from times import times_bp
from slack import slack_bp
from flask import Flask, render_template,request
from flask_jwt_extended import (JWTManager)

app = Flask(__name__)
app.secret_key = "green-eight"
app.register_blueprint(auth_bp, url_prefix='/')
app.register_blueprint(menu_bp, url_prefix='/')
app.register_blueprint(mypage_bp, url_prefix='/')
app.register_blueprint(rank_bp, url_prefix='/')
app.register_blueprint(times_bp, url_prefix='/')
app.register_blueprint(slack_bp)

jwt = JWTManager(app)
# 메인 창
@app.route('/')
def home():
    jwtToken = request.cookies.get('access_token')
    if jwtToken is None :
        return render_template('index.html')
    else :
        return render_template('menu.html')
    
if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)