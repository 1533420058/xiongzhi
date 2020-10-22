# coding=utf-8


from database import db
from Get_dfcj import Get_html,Get_Individualstocks
from models import Test2,Mysql_Stock
import threading
#调用GET_html类的函数得到热门标题和内容
def Mysql_hot_text():
    spider = Get_html()
    title_text=spider.Download()       
    for i in title_text:  
        DFCJ_title,DFCJ_TIME,DFCJ_source,DFCJ_Summary,DFCJ_Editor,DFCJ_text=i
        DFCJ_title=''.join(DFCJ_title)
        DFCJ_TIME=''.join(DFCJ_TIME)
        DFCJ_Summary=''.join(DFCJ_Summary)
        DFCJ_source=''.join(DFCJ_source)
        DFCJ_Editor=''.join(DFCJ_Editor)

        db.create_all()
        DFCJ_DATA=Test2(dfcj_title=DFCJ_title,dfcj_time=DFCJ_TIME,dfcj_source=DFCJ_source,dfcj_Summary=DFCJ_Summary,dfcj_Editor=DFCJ_Editor,dfcj_hot_txt=DFCJ_text)
        db.session.add(DFCJ_DATA)
        db.session.commit()
#调用个人股票涨跌函数获取第一页信息
def Mysql_Stock_StocksUpAndDown():
    spider=Get_Individualstocks()
    test=spider.gei_dfcj_Stockrise_json_data()
    for i in test:
        db.create_all()
        data=Mysql_Stock(stock_code=i[0],stock_title=i[1],stock_Latestprice=i[2],stock_Quotechange=i[3],stock_Increaseamount=i[4],stock_Turnover=i[5],stock_highest=i[6],stock_lowest=i[7],stock_Opentoday=i[8],stock_Closedyesterday=i[9],stock_Turnoverrate=i[10],stock_PE_ratioP=i[11],stock_PB_ratioB=i[12])
        db.session.add(data)
        db.session.commit()
   



if __name__ == '__main__':
    t1 = threading.Thread(target=Mysql_hot_text(),args=('t1',))  
    t2 = threading.Thread(target=Mysql_Stock_StocksUpAndDown(),args=('t2',))
    t2.start()
    t1.start()
    # Mysql_hot_text()
