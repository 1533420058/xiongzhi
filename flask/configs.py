import pymysql
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'mysqlxz'
USERNAME = 'root'
PASSWORD = '123456'

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,password=PASSWORD, host=HOST,port=PORT, db=DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
#SQLALCHEMY_ECHO = True
#"mysql+pymysql://root:123456@127.0.0.1:3306/my_db?charset=utf8mb4"