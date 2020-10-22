#  encoding=utf-8


import re
import requests
import json
from lxml import etree
import pprint
import time

 


class Get_html(object):
    def __init__(self):
        self.url='http://finance.eastmoney.com/company.html'
        self.headers={
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4209.400'
        }
        #请求字节格式
    def get_response_hetm(self,url):
        response=requests.get(url,headers=self.headers).text
        return response
        #请求TEXT格式
    def get_response_hetm_content(self,url):
        response=requests.get(url,headers=self.headers).content
        return response

        #解析
    def get_response_xpath(self,response):   
        response_html=etree.HTML(response)
        return response_html
        #需要JSON格式
    def get_response_josn(self):
        response_josn=requests.get(self.url,headers=self.headers)
        response_josn_data=response_josn.json()
        pprint.pprint(response_josn_data)
        #获取热门标题和链接
    def get_hot_title(self):
        rso=self.get_response_hetm(self.url)
        rsos=self.get_response_xpath(rso)
        hot_title_url=rsos.xpath('/html/body/div[1]/div[2]/div[1]/div/div[1]/ul/li/a[1]')
        return hot_title_url
        #下载
    def Download(self):
        url=self.get_hot_title()
        for url_html in url:
            url_html=url_html.xpath('./@href')[0]
            url_html=self.get_response_hetm_content(url_html)
            url_html=self.get_response_xpath(url_html)
            hot_text=url_html.xpath('''/html/body/div[1]/div[@class='page']/div[@class='mainFrame'][2]/div[@class='main_left']/div[@class='left-content']/div[@class='newsContent']/div[@id='ContentBody']//p/text()''')
            hot_time=url_html.xpath('/html/body/div[1]/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/text()')
            hot_source=url_html.xpath('/html/body/div[1]/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/text()')
            hot_Summary=url_html.xpath('//*[@id="ContentBody"]/div[2]/text()')
            hot_Editor=url_html.xpath('//*[@id="ContentBody"]//*[@class="res-edit"]/text()')
            hot_title=url_html.xpath('/html/body/div[1]/div/div[3]/div[1]/div[2]/div[1]/h1/text()')
            output=''
            for i in hot_text:
                output+=(i+'\n')

            print('热门头条已存入mysql')

            yield hot_title,hot_time,hot_source,hot_Summary,hot_Editor,output
            
                   
    def loads_jsonp(self,_jsonp):
            try:
                return json.loads(re.match(".*?({.*}).*",_jsonp,re.S).group(1))
            except:
                raise ValueError('Invalid Input')  
    
    
class Get_Individualstocks(Get_html):
    
    def __init__(self):
        self.url='http://43.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112408845062582052305_1602745508297&pn=1&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:13,m:0+t:80,m:1+t:2,m:1+t:23&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1602745508298'
        self.headers = {
           
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
            
            }
    def get_dfcj_Stockrise_json(self):
        response=self.get_response_hetm(self.url)
        response_dick=json.loads(re.match(".*?({.*}).*",response,re.S).group(1))
        
        return response_dick
    def for_url(self,i):
        url='http://48.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124029972769688072587_1603175637567&pn={}&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:13,m:0+t:80,m:1+t:2,m:1+t:23&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152'.format(i)
        return url
#    拿到股票数据
    def gei_dfcj_Stockrise_json_data(self):
        for i in range(0,210):
            print('正在存入第{}页数据'.format(i+1))
            url_dfcj=self.for_url(i+1)
            response=self.get_response_hetm(url_dfcj)
            json_data=response_dick=json.loads(re.match(".*?({.*}).*",response,re.S).group(1))
            json_list=json_data['data']['diff']
            # time.sleep(0.5)
            for i in json_list:
                #股票代号
                Stock_code=i['f12']
                #股票名称
                stock_title=i['f14']
                #股票最新价
                stock_Latestprice=i['f2']
                #涨跌幅  %
                stock_Quotechange=i['f24']
                #涨幅额度
                stock_Increaseamount=i['f4']
                #成交额
                stock_Turnover=i['f18']
                #最高
                stock_highest=i['f15']
                #最低
                stock_lowest=i['f16']
                #今开
                stock_Opentoday=i['f17']
                #昨收
                stock_Closedyesterday=i['f18']
                #换手率
                stock_Turnoverrate=i['f8']
                #市盈率
                stock_PE_ratioP=i['f9']
                #市净率
                stock_PB_ratioB=i['f23']
            
                yield Stock_code,stock_title,stock_Latestprice,stock_Quotechange,stock_Increaseamount,stock_Turnover,stock_highest,stock_lowest,stock_Opentoday,stock_Closedyesterday,stock_Turnoverrate,stock_PE_ratioP,stock_PB_ratioB
    def run(self):
         self.gei_dfcj_Stockrise_json_data()
    
if __name__ == '__main__':
    spider = Get_Individualstocks()
    spider.Download()    