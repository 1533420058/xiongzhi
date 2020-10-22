# coding=utf-8


from database import db
import datetime



#东方财经上市热门头条
class Test2(db.Model):
    __tablename__ = 'DFCJ_HOT_{}'.format(datetime.datetime.now().strftime('%Y/%m/%d'))
    id=db.Column(db.Integer, primary_key=True)
    dfcj_title=db.Column(db.String(100))
    dfcj_time=db.Column(db.String(30))
    dfcj_source=db.Column(db.String(30))
    dfcj_Summary=db.Column(db.Text)
    dfcj_Editor=db.Column(db.String(30))
    dfcj_hot_txt=db.Column(db.Text)

   


    
    def __repr__(self):
        return '<Test2 %r>' % self.dfcj_title
#个股排行榜
class Mysql_Stock(db.Model):
    __tablename__ = 'Stock_{}'.format(datetime.datetime.now().strftime('%Y/%m/%d'))
    id=db.Column(db.Integer, primary_key=True)
    stock_code=db.Column(db.String(20))
    stock_title=db.Column(db.String(20))
    stock_Latestprice=db.Column(db.String(20))
    stock_Quotechange=db.Column(db.String(20))
    stock_Increaseamount=db.Column(db.String(20))
    stock_Turnover=db.Column(db.String(20))
    stock_highest=db.Column(db.String(20))
    stock_lowest=db.Column(db.String(20))
    stock_Opentoday=db.Column(db.String(20))
    stock_Closedyesterday=db.Column(db.String(20))
    stock_Turnoverrate=db.Column(db.String(20))
    stock_PE_ratioP=db.Column(db.String(20))
    stock_PB_ratioB=db.Column(db.String(20))
    
    def __repr__(self):
        return '<Mysql_Stock %r>' % self.Stock_code