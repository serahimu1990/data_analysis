import requests

"""
模拟登陆豆瓣
"""

class DouBanLogin(object):
    def __init__(self, account, password):

        # https://accounts.douban.com/j/mobile/login/basic
        self.url = "https://accounts.douban.com/j/mobile/login/basic"
        # self.newurl = 'https://movie.douban.com/subject/27010768/comments?status=P'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
            "Host": "accounts.douban.com",
            "Referer": "https://accounts.douban.com/passport/login",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Cookie":"gr_user_id=6f78fe5a-ad6f-4c08-bcc6-b6f909cc11fc; _vwo_uuid_v2=D0944F87E843D5EEA1727502266864489|183df8c0610dfabc71481c9d81fbcad0; douban-fav-remind=1; "
            "__gads=ID=07b72da585d57676:T=1558148812:S=ALNI_MZkKWk8EvAl9cu_1lyKClGgyfD-Qw; "
            "bid=Az0fIWc0BiM; trc_cookie_storage=taboola%2520global%253Auser-id%3Decd5c4bb-1d82-4bd9-a05b-66bdd6d97398-tuct176e3ca; "
            "ll='108296'; viewed='34441323_30419577_30350007_30247776_5336893_33421284_30285146_30243136_26762081_30270959';"
            " __utmz=30149280.1566225557.154.60.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; "
            "_pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1566650009%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DSBqmxyZm5ZZXJw-hKfOJgFIEMjJhdBXQAkom7k5T9Vqr0FeiBTgEy58lDlu2Ga34G41A8atLTJ-Q60h3Or29ru3ycW5GPNwMG2dC347ylUi%26wd%3D%26eqid%3Dbb84e1a100007286000000035d3c5413%22%5D; "
            "_pk_ses.100001.8cb4=*; __utma=30149280.1373248791.1529204655.1566391626.1566650010.159; __utmc=30149280; dbcl2='202644733:kx4yxxvnNq4'; " \
             "ck=0S93; ps=y; ap_v=0,6.0; __yadk_uid=aLVzE0fPi9OnuI2ZjysqYmFSesaGkLQ4; push_doumail_num=0; " \
             "__utmv=30149280.20264; douban-profile-remind=1; ct=y; push_noty_num=0; __utmt=1; " \
             "__utmb=30149280.21.10.1566650010; _pk_id.100001.8cb4=fcedf087839e753c.1533431297.92.1566652519.1566392650."
        }
        """初始化数据"""
        self.data = {
            "ck": "0S93",
            "name": account,
            "password": password,
            "remember": "true",
            "ticket": "",
            "remember": "false",
        }
        self.session = requests.Session()

    def get_cookie(self):
        """模拟登陆获取cookie"""
        html = self.session.post(
            url=self.url,
            headers=self.headers,
            data=self.data,
            verify=True,
        )
        # print(html.status_code)
        # print(html.url)

        if html.status_code == 200:
            print("恭喜你，登陆成功") #16621387734

    def get_data(self,b):
        """获取用户数据表明登陆成功"""
        url = b
        # 获取页面信息
        html = self.session.get(url).text
        # print("*"*100)
        # print(html)
        return html

    def run(self):
        """运行程序"""
        self.get_cookie()
        # self.get_data()

#
# __name__ == '__main__':
# account = input("请输入你的账号:")
# password = input("请输入你的密码:")
# login = DouBanLogin(account, password)
# login.run()
# if