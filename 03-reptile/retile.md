# reptile

## 1、开发环境配置

###  请求库

#### requests

####  Selenium

Selenium自动化测试工具：可驱动浏览器执行特定的动作。

#### ChromeDriver

Selenium是一个自动测试化工具，需要ChromeDriver配合使用

* 选择对应浏览器版本的驱动
* 下载地址：
  * [ChromeDriver](https://chromedriver.storage.googleapis.com/index.html)
* 下载后直接将chromediver.exe拖进Python的Scripts目录下

#### GeckoDriver

[GeckoDriver](https://github.com/mozilla/geckodriver/releases)

#### PhantomJS

#### aiohttp



### 解析库

#### lxml

支持HTML和XML的解析，支持XPath解析方式，解析效率高

#### BeautifulSoup4

HTML或XML的解析库，方便网页中提取数据。有强大的API和多样的解析方式

依赖于lxml库，在此之前确保安装lxml

#### pyquery

网页解析工具，提供和JQuery类似的语法来解析HTML文档，支持CSS选择器

#### tesserocr

解决验证码的

tesserocr：是python的一个OCR识别库，其实是对tesseract做的一层Python API分装，核心是tesseract。

先安装tesseract，再安装tessrocr

[tessract](https://digi.bib.uni-mannheim.de/tesseract/)

pip3 install tesserocr pillow





### 存储库



### Web库



### APP爬取相关库



### 爬虫框架



### 部署相关库



## 2、爬虫基础



### URI和URL

* URI(Uniform Resource Identifiter)：统一资源标志符
* URL(Universal Resource Locator)：统一资源定位符



URL是URI的子集，每个URL都是URI，但不是每个URI都是URL。

一般的链接可以称为URL，也可以叫URI。



### HTTP和HTTPS

* HTTP（Hyper Text Transfer Protocol）：超文本传输协议。从网络传输超文本数据到本地浏览器的传输协议。
* HTTPS（Hyper Text Transfer Protocol over Secure Socket Layer）：HTTP的安全版，在HTTP下加了SSL层。



### 爬虫

爬虫：爬虫就是获取网页并提取和保存信息的自动化程序

* 获取网页：通过reques、urllib等来实现HTTP请求操作，获得响应内容。
* 提取信息：通过BeautifulSoup、pyquery、lxml等提取需要的信息。
* 保存数据：将提取的信息保存到某处以便后续使用。
* 自动化程序：快速获取大量数据，借助程序，自动化爬虫。在抓取过程中进行各种异常处理，错误重试等操作，确保爬虫持续高效的运行。
* 

### 数据的呈现形式

* HTML源码
* JSON字符串
* 二进制数据（图片、音视频等）
* 各种扩展名的文件



### JS渲染页面

使用selenium、Splash爬取



### 会话和Cookies



### 代理的基本原理

网站采取了反爬措施，服务器会检测某个ip在单位时间内的请求次数，超过了规定的阈值，则会放回错误信息，称为封IP。

代理：通过代理网络用户取得网络信息。（本机通过向代理服务器发出请求，让Web服务器取获取响应，再放回给本机）这个过程Web服务识别的IP不再是本机IP。

爬取过快、同一IP频繁访问，网站可能要求输入验证码登录或封禁IP



#### 代理分类

* FTP
* HTTP
* RTSP
* Telnet
* P0P3/SMTP
* SOCKS





## 基本库的使用

请求库，让你只需要关心请求是什么，需要的参数是什么，以及何如设置可选的请求头即可。不需深入了解底层是怎么用传输和通信的。

### urlib

内置的http请求库

包含4个模块：

* request：模拟发送请求
  * openurl()
  * Request()
* error：异常处理模块
* parse：工具模块（提供URL处理方法，如拆分、解析、合并）
  * urlencode()
  * 
* rebotparser：是要用来识别网站的robots.txt文件，判断那些网站可以爬。



### requests



#### cookie

```python
import requests

headers = {
    'Cookie': '_zap=16d60559-3e1b-4baf-899a-641d2301c315; d_c0="AECRGEpQyhGPTjse0SgtZtNTlKQj_uFjLFI=|1598414814"; _ga=GA1.2.1041407150.1598414816; _xsrf=AlYQtcPjKrUE696XMzI0v9GodhoGUCTL; q_c1=0a0b665d4460456c9b5666571091d346|1606708875000|1600141412000; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1608168233,1608168330,1608182427,1608207041; SESSIONID=EkdbY5ygBEdLormeTcH3qQMCcxYI39Jga6wFDUrW5Qx; JOID=Vl4RA00W0x95cY-lExKzTiX07U0CUbp_HSq43nBWlHkxGP_KdNSfxiJxj6MRI02gS5ok3SH6uN4ZzzoepsKDcbg=; osd=V18VAEsX0ht6d46kFxG1TyTw7ksDUL58Gyu52nNQlXg1G_nLddCcwCNwi6AXIkykSJwl3CX5vt8YyzkYp8OHcr4=; capsion_ticket="2|1:0|10:1608209630|14:capsion_ticket|44:ZjVkNmIxN2IzZGRjNGU0MmIxMDA2N2YwY2E3NzFiOWY=|25c209f9195ad78d6aa712a86af54fa7eb60b99d31eec2d3476f8afe8e63fc4a"; z_c0="2|1:0|10:1608209631|4:z_c0|92:Mi4xMjB4SUdRQUFBQUFBUUpFWVNsREtFU1lBQUFCZ0FsVk4zNkxJWUFBMlUzM1p4OHZMSmUxSkxMeDNhbG9FX3FmSTln|552c7ff97d4dbfe25e03f37efc4faa9dbcfe24559f00906e2dded9e85c09ee93"; unlock_ticket="ACDZbYK81xAmAAAAYAJVTedb219Dk8W31nxoY1mklGNHr67GG7arGA=="; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1608209633; KLBRSID=81978cf28cf03c58e07f705c156aa833|1608209633|1608207040',
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}

r = requests.get('https://www.zhihu.com', headers=headers)
print(r.text)
```



#### 会话维持

直接使用get()或post()等方法，虽然可以做到模拟登录，但是在是两个不同的会话。（相当于用两个浏览器打开了不同的页面）

requests.Session()

```python
import requests

set_url = 'http://httpbin.org/cookies/set/number/123456789'
cookies_url = 'http://httpbin.org/cookies'

# 获取一个session对象
s = requests.session()
print(type(s))
s.get(set_url)
r = s.get(cookies_url)
print(r.text)


"""
<class 'requests.sessions.Session'>
{
  "cookies": {
    "number": "123456789"
  }
}
"""
```

用于模拟在一个浏览器中打开同一站点的不同页面



#### SSL证书验证

* 设置忽略警告的方式屏蔽警告

  ~~~python
  import requests
  from request.packages import urllib3
  
  urllib3.disable_warnings()
  resp = requests.get('https://www.12306.com', verify=False)
  ~~~

* 通过捕获警告到日志的方式忽略警告

  ~~~python
  import requests
  from logging
  
  logging.captureWarnings(True)
  resp = requests.get('https://www.12306.com', verify=False)
  ~~~

* 指定一个本地证书用作客户端证书，可以是单个文件（包含密钥和证书）或一个包含两个文件路径的元组

  * 需要crt和key文件，并指定路径



#### 代理设置

大规模且频繁的请求，可能会弹出验证码或登录认证，严重的封禁ip，再或者`隐匿身份`，此时需要设置代理来解决

##### HTTP代理

```python
def agent(url):
    pool = ['http://182.84.133.61:48021', 'http://119.116.79.150:38070']
    proxies = {
        'http': random.choice(pool)
    }
    print(proxies)
    resp = requests.get(url, proxies=proxies)
    print(resp.status_code)
    # print(resp.text[:100])
    print(resp.headers)


def main():
    agent('https://www.taobao.com')


if __name__ == '__main__':
    main()
```

#####  SOCKS代理



##### 蘑菇代理池

```python
# 代理url
mogu_url = 'http://piping.mogumiao.com/proxy/api/get_ip_al?appKey=b3e67385fc9449aea21aac7c02c1fe73&expiryDate=0&format=1&newLine=2'

def mogu_proxies_pool(url, count=5):
    """
    获取蘑菇代理
    :param count: 获取的条数
    :param url: 蘑菇代理url
    :return: 代理池
    """
    url = url + f'&count={count}'
    resp = requests.get(url)
    proxies_pool = []
    if resp.status_code == 200:
        json = resp.json()
        if json['code'] == '0':
            for item in json['msg']:
                proxies_pool.append(f"http://{item['ip']}:{item['port']}")
            print('已获取代理池')
        elif json['code'] == '3001':
            print('appkey提取频繁，请按照所购买订单规定的频率进行合理提取。如仍未解决，建议检查相关后台进程！')
        elif json['code'] == '3002' or json['code'] == '3005':
            print('请检查订单的有效时间！')
        elif json['code'] == '3006':
            print('请检查订单的剩余数量！')
        elif json['code'] == '3004':
            print('appkey有误！')
        else:
            print('代理有误！')

    else:
        print('代理有误！')

    return proxies_pool
```



#### 身份认证

在访问网站时，可能会遇见认证问题，requests自带了身份认证功能。

* reuqests.auth.HTTPBasicAucth对象传入auth

* 给参数auth中传一个元组

* requests_oauthlib





~~~python
import requests
from requests.auth import HTTPBasicAuth

url='http://localhost:5000'

# 方法一
r = request.get(url, auth=HTTPBasicAuth('username', 'passwd'))

# 方法二
r = request.get(url, auth=('username', 'passwd'))

# 方法三
# pip install requests_oauthlib
from request_oauthlib import OAuth1

auth = OAuth1('APP_KEY', 'APP_SECRET', 'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRT')
requests.get(url, auth=auth)
~~~





#### Prepared Request

将请求表示为数据结构，其中的参数通过Request对象来表示，这种数据结构叫Prepared Request。

* 用method、url、data、headers来构造Request对象

* 调用Session的prepare_request()方法转换为Prepared Request对象

* 调用send()方法请求即可



```python
from requests import Request, Session

url = 'http://httpbin.org/post'

data = {'name': 'reddy'}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}

s = Session()
req = Request('POST', url, headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)
```



#### 正则表达式

处理字符串的强大工具，实现字符串的检索、替换、匹配验证等。

对提取HTML中的信息



|   方法   |                             描述                             |
| :------: | :----------------------------------------------------------: |
|   math   | 匹配字符串开头，如果匹配不到结果是None，如果匹配成功了结果是匹配对象。 |
|  group   |                匹配成功，正则所匹配的内容范围                |
|   span   |                    匹配的范围,是一个元组                     |
|  string  |                         获取原字符串                         |
|  search  | 在字符串中查找第一个能和正则表达式匹配的子串，找到返回对象，未找到返回None。 |
| findall  | 获取字符串中所有满足正则表达式的子串，返回一个列表，列表中的元素是字符串 |
| finditer | 获取字符串中所有满足正则表达式的子串。返回一个迭代器，迭代器中的元素是匹配对象 |
|          |                                                              |

##### 通用匹配

`.`可以匹配任意字符，`*`代表匹配前的字符0获取n次，他们组合匹配任意字符。

##### 贪婪和非贪婪

正常情况都是贪婪，非贪婪用`?`表示。

`.*?`在字符串末尾，就可能匹配不到任何内容，尽可能少的匹配字符。



##### 修饰符

| 修饰符 | **描述**                                                     |
| ------ | ------------------------------------------------------------ |
| re.I   | 使匹配对大小写不敏感                                         |
| re.L   | 做本地化识别（locale-aware）匹配                             |
| re.M   | 多行匹配，影响 ^ 和 $                                        |
| re.S   | 使 . 匹配包括换行在内的所有字符                              |
| re.U   | 根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.      |
| re.X   | 该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。 |



##### 转义匹配  /

