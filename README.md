# urlscan
自用使用谷歌搜索或必应搜索引擎爬取url工具

因现在搜索引擎的反爬机制，很多不带代理的url扫描程序已经不好用了，故修改二次开发。  
自用谷歌搜索或必应搜索引擎爬取url工具  
请使用python3以上环境，建议python3.8  
使用方法：  
1.git clone https://github.com/PrettyABC/urlscan.git  
2.cd urlscan  
3.pip install -r requirements.txt  
4.修改代码中以下字段：  
proxies = {  
  "http": "http://127.0.0.1:7890",  
  "https": "http://127.0.0.1:7890",  
}  
将127.0.0.1:7890修改为你的代理端口  
5.即可食用！！！  
6.食用-h命令可以查看食用方法！！！  
7.输出结果自动保存至url.txt中（注意：输出结果会自动追加至url.txt文件中，请运行代码前查看目录中是否有url.txt文件）  
8.如果想替换为覆盖url.txt文件的话修改以下代码：  
with open("urls.txt", "a") as f:  
替换为  
with open("urls.txt", "w") as f:  
