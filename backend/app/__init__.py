from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'  # 替换为你的MySQL连接信息
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 're34re1q345#S#@EF'  # 用于JWT签名的密钥


db = SQLAlchemy(app)
jwt = JWTManager(app)
with app.app_context():
    db.create_all()
from app import views
from app import models