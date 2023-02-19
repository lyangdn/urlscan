import argparse
import re
import requests
from bs4 import BeautifulSoup
import urllib3
import time

urllib3.disable_warnings()

def hander():
    print(" _                            ") 
    print("| |   _   _  __ _ _ __   __ _ ") 
    print("| |  | | | |/ _` | '_ \ / _` |") 
    print("| |__| |_| | (_| | | | | (_| |") 
    print("|_____\__, |\__,_|_| |_|\__, |") 
    print("      |___/             |___/ ")
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--search", help="设置URL。示例:inurl:asp?id=30", required=True)
parser.add_argument("-s", "--site", help="设置顶级域名。示例：.cn", required=True)
parser.add_argument("-f", "--file", help="设置输出名。默认为urls.txt", default="urls.txt")
args = parser.parse_args()

# 设置UA
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'

query = f"{args.search} and site:{args.site}"
num = 300
query = query.replace(' ', '+')
URL = f"https://google.com/search?q={query}&num={num}"

headers = {"user-agent": USER_AGENT}
hander()
print("开始谷歌扫描\n")
results = []
proxies = {
  "http": "http://127.0.0.1:7890",
  "https": "http://127.0.0.1:7890",
}

for i in range(num//100):
    URL = f"https://google.com/search?q={query}&num={num}&start={i*100}"
    resp = requests.get(URL, headers=headers, proxies=proxies, verify=False)

    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")
        # url is in the href attribute of the <a> tag under the <div> tag
        for g in soup.find_all('div'):
            anchors = g.find_all('a')
            if anchors:
                for i in range(len(anchors)):
                    try:
                        link = anchors[i].attrs['href']
                        # filter URL with regex and remove some garbage
                        if re.match('/', link) is None and re.match('(.*)google.com',link) is None and link != '#' and link.find('search?q') == -1:
                            # filter duplicate URL
                            if any(i.split(".site")[0] == link.split(".site")[0] for i in results):
                                link = ""
                            results.append(link)
                    except:
                        pass
    time.sleep(5)
print(results)

with open(args.file, "a") as f:
    for i in results:
        if i != "":
            f.write(i + "\n")
