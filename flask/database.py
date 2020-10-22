# coding=utf-8


from flask import Flask
import configs
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# 加载配置文件
app.config.from_object(configs)
db=SQLAlchemy(app)
# db绑定app


