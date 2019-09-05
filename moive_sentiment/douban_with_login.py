import urllib.request
import urllib.parse
from lxml import etree
import time
import  numpy as np
import pymysql
import requests
from login.log import DouBanLogin


def handle_content(content):
    print("开始解析")
    tree = etree.HTML(content)
    div_list = tree.xpath('//div[@class="mod-bd"]//div[@class="comment-item"]')
    next_url = tree.xpath('//div[@class="mod-bd"]/div[@id="paginator"]/a[@class="next"]/@href')
   
    for odiv in div_list:
        # print("******"*5,odiv)

        user_name = odiv.xpath('./div[@class="comment"]/h3/span[@class="comment-info"]/a/text()')
        pscore = odiv.xpath('./div[@class="comment"]/h3/span[@class="comment-info"]/span[contains(@class,"allstar")]/@class')
        pcomment=odiv.xpath('./div[@class="comment"]//span[@class="short"]/text()')
        ptime = odiv.xpath('./div[@class="comment"]/h3/span[@class="comment-info"]/span[contains(@class,"comment-time")]/@title')
        pvote = odiv.xpath('./div[@class="comment"]/h3//span[@class="votes"]/text()')
        if not pscore:
            pscore="allstar"
        if not pvote:
            pvote=0
        save_data(user_name,pcomment,ptime,pvote,pscore)
    return next_url

def save_data(username,pcomment,pdate,pvote,pscore):
    conn = pymysql.connect(host='localhost', user='root', password='', database='douban',port=3306)
    cursor = conn.cursor()  # 创建游标

    sql = """insert into parasite(id,user_name,pcomment,pdate,pvote,pscore) values(Null,%s,%s,%s,%s,%s)"""

    cursor.execute(sql,(username,pcomment,pdate,pvote,pscore))
    # cursor.execute(sql,(username,age,salary,job_time))
    # 执行sql语句
    conn.commit()  # 提交执行操作

    # conn.close()  # 关闭连接


def main():

    url= 'https://movie.douban.com/subject/26796665/comments?status=P'

    content = login.get_data(url)
    nexturl=handle_content(content)
    time.sleep(2)
    while nexturl:

            newurl='https://movie.douban.com/subject/26796665/comments' + nexturl[0]
            cont = login.get_data(newurl)

            nexturl = handle_content(cont)

            time.sleep(2)

if __name__=='__main__':
    account = input("请输入你的账号:")
    password = input("请输入你的密码:")
    login = DouBanLogin(account, password)
    login.run()
    main()