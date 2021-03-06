# Spider
- [Spider](#spider)
  - [1、开发环境配置](#1开发环境配置)
    - [请求库](#请求库)
      - [requests](#requests)
      - [Selenium](#selenium)
      - [ChromeDriver](#chromedriver)
      - [GeckoDriver](#geckodriver)
      - [PhantomJS](#phantomjs)
      - [aiohttp](#aiohttp)
    - [解析库](#解析库)
      - [lxml](#lxml)
      - [BeautifulSoup4](#beautifulsoup4)
      - [pyquery](#pyquery)
      - [tesserocr](#tesserocr)
    - [存储库](#存储库)
    - [Web库](#web库)
    - [APP爬取相关库](#app爬取相关库)
    - [爬虫框架](#爬虫框架)
    - [部署相关库](#部署相关库)
  - [2、爬虫基础](#2爬虫基础)
    - [URI和URL](#uri和url)
    - [HTTP和HTTPS](#http和https)
    - [爬虫](#爬虫)
    - [数据的呈现形式](#数据的呈现形式)
    - [JS渲染页面](#js渲染页面)
    - [会话和Cookies](#会话和cookies)
    - [代理的基本原理](#代理的基本原理)
      - [代理分类](#代理分类)
  - [3、基本库的使用](#3基本库的使用)
    - [urlib](#urlib)
    - [requests](#requests-1)
      - [cookie](#cookie)
      - [会话维持](#会话维持)
      - [SSL证书验证](#ssl证书验证)
      - [代理设置](#代理设置)
        - [HTTP代理](#http代理)
        - [SOCKS代理](#socks代理)
        - [蘑菇代理池](#蘑菇代理池)
      - [身份认证](#身份认证)
            - [Prepared Request](#prepared-request)
                - [正则表达式](#正则表达式)
              - [通用匹配](#通用匹配)
              - [贪婪和非贪婪](#贪婪和非贪婪)
              - [修饰符](#修饰符)
              - [转义匹配  /](#转义匹配--)

  - [4、解析库的使用](#4解析库的使用)
    - [XPath](#xpath)
      - [XPath常用规则](#xpath常用规则)
      - [初始化](#初始化)
      - [字符串初始化](#字符串初始化)
      - [文件初始化](#文件初始化)
      - [文本获取](#文本获取)
      - [属性多值匹配](#属性多值匹配)
      - [多属性匹配](#多属性匹配)
      - [按序选择](#按序选择)
      - [节点轴选择](#节点轴选择)
    - [Beautiful Soup](#beautiful-soup)
      - [解析器](#解析器)
      - [BS解析器](#bs解析器)
      - [节点选择器](#节点选择器)
      - [方法选择器](#方法选择器)
      - [CSS选择器](#css选择器)
    - [pyquery](#pyquery-1)
      - [初始化](#初始化-1)
      - [字符串初始化](#字符串初始化-1)
      -  [URL初始化](#url初始化)
      -  [文件初始化](#文件初始化-1)
      - [函数](#函数)
      - [属性](#属性)
      - [伪类选择器](#伪类选择器)
  - [5、数据存储](#5数据存储)
    - [文件存储](#文件存储)
      - [TXT](#txt)
      - [JSON](#json)
      - [CSV](#csv)
    - [关系型数据库存储](#关系型数据库存储)
      - [MySQL](#mysql)
        - [操作](#操作)
    - [非关系数据存储](#非关系数据存储)
      - [MongoDB](#mongodb)
        - [连接Mongo](#连接mongo)
      - [Redis](#redis)
  - [6、Ajax数据爬取](#6ajax数据爬取)
  - [7、动态渲染页面爬取](#7动态渲染页面爬取)
    - [为什么要动态获取](#为什么要动态获取)
    - [模拟浏览器运行的库](#模拟浏览器运行的库)
    - [Selenium](#selenium-1)
        - [声明浏览器对象](#声明浏览器对象)
        - [无头浏览器](#无头浏览器)
        - [规避被监测的风险](#规避被监测的风险)
        - [查找节点](#查找节点)
          - [单个节点](#单个节点)
          - [通用查找](#通用查找)
          - [多个节点](#多个节点)
        - [节点交互](#节点交互)
        - [动作链](#动作链)
        - [执行JS](#执行js)
        - [获取节点信息](#获取节点信息)
        - [切换Frame](#切换frame)
        - [延时等待](#延时等待)
          - [隐式等待](#隐式等待)
          - [显示等待](#显示等待)
          - [等待条件](#等待条件)
        - [前进和后退](#前进和后退)
        - [Cookies](#cookies)
        - [选项卡管理](#选项卡管理)
          - [异常处理](#异常处理)
    - [Splash](#splash)
  - [8、验证码的识别](#8验证码的识别)
    - [图形验证码](#图形验证码)
      - [工具](#工具)
      - [先转灰度](#先转灰度)
      - [设定阈值](#设定阈值)
      - [二值化](#二值化)
      - [获取验证码的字符串](#获取验证码的字符串)

    - [极验滑动验证码](#极验滑动验证码)
    - [步骤](#步骤)
    - [工具](#工具-1)
    - [特点](#特点)
  - [9、代理的使用](#9代理的使用)
    - [代理池的维护](#代理池的维护)
        - [准备工作](#准备工作)
        - [代理的目标](#代理的目标)
        - [基本模块](#基本模块)
    - [ADSL拨号代理](#adsl拨号代理)
  - [什么是ADSL](#什么是adsl)
        - [购买主句](#购买主句)
  - [10、模拟登录](#10模拟登录)
  - [案例](#案例)
    - [猫眼爬取](#猫眼爬取)
- [top正则表达式](#top正则表达式)
    - [京东商品爬取](#京东商品爬取)
    - [点触验证码登录boss直聘](#点触验证码登录boss直聘)




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

是一个无界面的、可脚本编程的WebKit浏览器引擎，支持多种Web标准：Dom操作、CSS选择器、JSON、Canvas以及SVG.

Selenium支持PhantomJS，在运行时不弹出浏览器。

[Phantomjs下载地址](https://phantomjs.org/download.html)

* 将文件所在路径里面bin文件夹下的phantomjs.exe配置到环境变量里面
* 也可以将phantomjs.exe复制到python的scirpts文件里



#### aiohttp

requests是一个阻塞的HTTP请求库，当发出一个请求后，程序会等待服务的响应，知道得到响应后才会经行下一步的处理。这是一个耗时操作。

在等待的过程中做一些其他事可以提高爬取效率，如请求的调度、响应的处理等。

aiohttp提供异步Web服务的库，从python3.5版本开始，python中加入了async/await关键字，使得回调的写法更加直观和人性化。

直接 pip install aiohttp

官方还推荐安装两个库：一个是字符编码检测库cchardet，还一个是加速DNS的解析库aiodns

pip install cchardet aiodns





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

####  pyspider的安装

pip install pyspider



安装完成之后，命令行启动pyspider

pyspider all



##### 常见错误

<font color="red">ERROR: Command errored out with exit status 10: python setup.py egg_info Check the logs for full command output.</font>

需要安装PyCul库，从<https://www.lfd.uci.edu/~gohlke/pythonlibs/#pycurl>找对应的Python版本，下载wheel文件即可。

![](./images/PyCurl.png)



<font color="red">SyntaxError: invalid syntax</font>

<https://blog.csdn.net/u012424313/article/details/89511520>



#### Scrapy

十分强大的爬虫框架、依赖的库比较多，至少需要依赖库由Twisted14.0、lxml3.4和pyOpenSSL0.14。

在不同的平台环境下，他所依赖的库也不一样，安装之前要确保安装了基本的库。

##### windows下安装

* pip install lxml

* 安装pyOpenSSL

  * [下载wheel文件](https://pypi.python.org/pypi/pyOpenSSL#downloads)

    ![](./images/pyOpenSSL-wheel.png)

  * pip install  pyOpenSSL-20.0.1-py2.py3-none-any.whl

* 安装Twisted

  * [下载wheel文件](https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted)

    ![](./images/twisted-wheel.png)

* 安装pyWin32

  * [链接](https://sourceforge.net/projects/pywin32/files/pywin32/Build%20221)
  * 双击.exe文件安装即可

* pip install Scrapy



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





## 3、基本库的使用

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

## 4、解析库的使用



### XPath

XPath，全称XML Path Language，即XML路径语言，是一门在XML文档中查找信息的语言。

提供了超过100个内建函数，用于字符串、数值、时间的匹配以及节点、序列的处理。几乎所有想要定位的节点，都可以用XPath来选择。

XPath于1999年11月16日成为W3C标准。

#### XPath常用规则

|     表达式      |                     描述                     |
| :-------------: | :------------------------------------------: |
|    nodename     |            选取从节点的所有子节点            |
|        /        |           从当前节点选择直接子节点           |
|       //        | 从当前节点选取子孙节点（一般也表示所有节点） |
|        .        |                 选取当前节点                 |
|       ..        |             选取当前节点的父节点             |
|        @        |                   选取属性                   |
| [@class="item"] |                   属性匹配                   |
|     text()      |               获取节点中的文本               |

#### 初始化

~~~python
from lxml import etree

# 字符串初始化
html = etree.HTML(text)
res = etree.tostring(html)
print(res.decode('utf-8'))

# 文件初始化
html = etree.parse('./index.html', etree.HTMLParser())
~~~





#### 文本获取

* //text()：节点下的所有内容（更为完整，但可能会夹杂一些特殊字符）

* /a/text()：准确



#### 属性多值匹配

 contains()函数

```
//li[contains(@class,”li”)]/a/text()
```



#### 多属性匹配

用and连接

~~~
//li[contains(@class,”li") and @name＝item]
~~~



#### 按序选择

在选择某些属性可能会匹配多个节点，可只想要其中的某个节点时，可以用last()，posttion()等函数，也可以用索引或者last()，posttion()的比较和加减运算。



~~~
result = html. xpath (’//li[l]/a/text()’) 
result = html.xpath (’ I / li[last() ] /a/text()’) 
result = html.xpath (’ I !li [position() <3 ] I a/text() ’ ) 
result = html. xpath ( ’ I /li [last ()-2] /a/text() ’ ) 
~~~



####  节点轴选择

中间要用`::`隔开

| 轴选择            | 释义                       | 示例                                                   |
| ----------------- | -------------------------- | ------------------------------------------------------ |
| ancestor          | 祖先                       | （//li[l]/ancestor:： ·*）、（//li[l]/ancestor: :div） |
| attribute         | 属性                       | //li [1] /attribute: : *                               |
| child             | 孩子                       | //li[1]/child: :a[@href=”linkl.html”]                  |
| descentant        | 子孙                       | //li[l]/descendant::span                               |
| following         | 当前节点之后的所有节点     | //li[1]/following : :*(2]                              |
| following-sibling | 当前节点之后的所有同级节点 | //li [1]/following-sibling: : *                        |



### Beautiful Soup

借助网页的结构和属性等特性来解析网页。

Python的一个HTML或XML的解析库。

#### 解析器

BS在解析时实际依赖解析器，处理支持Python标准库中的HTML解析器外，还支持一些三分解析器（如lxml)



#### BS解析器

|     解析器      |              使用方法               |                           优势                            |                       劣势                        |
| :-------------: | :---------------------------------: | :-------------------------------------------------------: | :-----------------------------------------------: |
|  Python标准库   | BeautifulSoup(markup,”html.parser") |     Python的内置标准库、执行 速度适中、文档容错能力强     | Python 2.7.3及Python3.2.2之前的版本文档容错能力差 |
| lxml HTML解析器 |    BeautifulSoup(markup,”lxml")     |                  速度快、文档容错能力强                   |               需要安装c语言库解析器               |
| lxml XML解析器  |     BeautifulSoup(markup,”xml")     |                   速度快、唯一支持的XML                   |               需要安装c语言库解析器               |
|    html5lib     |  BeautifulSoup(markup,”html5lib")   | 最好的容错性、以浏览器的方式解析文档、生成HTML5格式的文档 |              速度慢、不依赖外部扩展               |





~~~python
from bs4 import BeautifulSoup

soup = BeautifulSoup(text, 'lxml')
print(soup.p.string)

~~~



#### 节点选择器

| 属性              | 释义                                                         |
| ----------------- | ------------------------------------------------------------ |
| string            | 获取文本的值                                                 |
| name              | 获取节点的名称                                               |
| attrs             | 获取所有的属性，可用attrs['name']获取name的属性值            |
| contents          | 得到一个子节点列表                                           |
| children          | 得到所有的子节点，返回一个生成器类型                         |
| descendants       | 得到所有的子孙节点，返回一个生成器类型。递归查询所有节点，得到所有的子孙节点 |
| parent            | 获取某个节点元素的父节点                                     |
| parents           | 获取所有祖先节点，返回一个生成器类型                         |
| previous_sibling  | 上一个兄弟节点                                               |
| next_sibling      | 下一个兄弟节点                                               |
| previous_siblings | 所有前面的兄弟节点                                           |
| next_siblings     | 所有后面的兄弟节点                                           |



#### 方法选择器

进行比较复杂的选着

|                     查询方法                      |                             释义                             |
| :-----------------------------------------------: | :----------------------------------------------------------: |
| find_all(name, attrs , recursive, text, **kwargs) | 传入一些属性或文本，得到复合条件的元素<br />name：节点名<br />attrs：通过属性查询，用字典。<br />常用的属性可以用正常传值的方式<br /><br />text：匹配节点的文本<br /> |
|                      find()                       |                     得到第一个匹配的元素                     |
|                  find_parents()                   |                        所有的祖先节点                        |
|                   find_parent()                   |                          直接父节点                          |
|                previous_sibling()                 |                        上一个兄弟节点                        |
|                  next_sibling()                   |                        下一个兄弟节点                        |
|                previous_siblings()                |                      所有前面的兄弟节点                      |
|                  next_siblings()                  |                      所有后面的兄弟节点                      |
|                  find_all_next()                  |                 返回节点后所有复合条件的节点                 |
|                    find_next()                    |                     第一个符合条件的节点                     |
|                find_all_previous()                |                   节点前所有符合条件的节点                   |
|                  find_previous()                  |                  节点前第一个符合条件的节点                  |



#### CSS选择器

|                             方法                             |     释义      |
| :----------------------------------------------------------: | :-----------: |
|                           select()                           | 查询,支持嵌套 |
| soup.selelct('ul').**attrs['id']** / soup.**selelct('ul')['id']** |   获取属性    |
|                     get_text() / string                      |   获取文本    |



### pyquery



需要传入HTML文本来初始化PyQuery对象。初始化的的方式有传入字符串、URL、文件名。

#### 初始化

~~~python
from pyquery import PyQuery as pq

# 字符串初始化
html = ''' <html>....</html>'''
doc = pq(html)

# URL初始化
doc = pq(url='https://www.baidu.com')

# 文件初始化
doc = pd(filename='demo.html')
~~~



#### 函数

|     函数      |                             释义                             |
| :-----------: | :----------------------------------------------------------: |
|    find()     |                      符合条件的所有节点                      |
|  children()   | 所有符合条件的子孙节点，进行子节点筛选可以传入css选择器如'.active or #hi' |
|   parent()    |              获取某个节点的父节点，PyQuery类型               |
|   parents()   |           返回所有的祖先节点，也可以传入css选择器            |
|  siblings()   |                         获取兄弟节点                         |
|    items()    |  遍历返回的多个节点。放回的都是PyQuery类型，并没有返回列表   |
|    attr()     |              获取属性，只会得到第一个节点的属性              |
|    text()     |         获取文本，忽略所有的HTML，只返回文字（所有）         |
|    html()     |                   第一个节点内部的HTML内容                   |
|  addClass()   |                      添加class(第一个)                       |
| removeClass() |                      移除class(第一个)                       |
|   remove()    |                           移除节点                           |
|   append()    |                             添加                             |
|    empty()    |                                                              |
|   prepend()   |                                                              |



#### 属性

| 属性 |                                    |
| ---- | ---------------------------------- |
| attr | 获取属性，只会得到第一个节点的属性 |



#### 伪类选择器

* first-child
* last-child
* nth-child(n)
* gt(n)
* nth-child(2n)
* contains(second) 



## 5、数据存储

### 文件存储

#### TXT

操作简单、几乎兼容任何平台，但不利于检索。

对检索和数据结构要求不高，追求方便，可用txt。





#### JSON

全称JavaScript Object Notation，Javascript对象标记。



#### CSV





### 关系型数据库存储

#### MySQL

关系型数据库是基于关系模型的数据库，而关系模型是通过二维表来保存的。



PyMySQL是通过connect()方法获取连接对象，连接成功之后再调用cursor()方法获得操作游标，利用游标来执行SQL语句。



|                            方法                             |                 释义                 |
| :---------------------------------------------------------: | :----------------------------------: |
| connect(host=host, user=user, password=password, port=port) |             获取连接对象             |
|                          cursor()                           |               获取游标               |
|                          execute()                          |             执行SQL语句              |
|                         fetchone()                          | 获得结果第一条数据，放回结果元组形式 |
|                         fetchall()                          |          得到结果的所有数据          |
|                          commit()                           |                 提交                 |
|                         roolback()                          |                 回滚                 |
|                                                             |                                      |
|                                                             |                                      |



```python
host = 'ip'
user = 'username'
password = 'password'
port = 3306 # 端口


conn = pymysql.connect(host=host, user=user, password=password, port=port)
cursor = conn.cursor()
```



##### 操作

```python
import csv
import os

import pymysql



host = 'ip'
user = 'username'
password = 'password'
port = 3306 # 端口


create_table = '''
create table if not exists spiders.movies_top100
(
    id           int         not null auto_increment,
    rank         int unique,
    image_url    varchar(255),
    name         varchar(50) not null,
    star         varchar(50) not null,
    release_data datetime    not null,
    country      varchar(20),
    score        double      not null,
    primary key (id)
)
'''



insert_data = '''
insert into spiders.movies_top100 (`rank`, image_url, `name`, star, release_data, country, score) values 
'''



conn = pymysql.connect(host=host, user=user, password=password, port=port)
with conn.cursor() as cursor:
        try:
           cursor.execute('create database if not exists spiders default  character set utf8')
            cursor.execute(create_table)
            data = read_csv('top.csv')[1:]
            data = str(tuple(map(lambda ele: tuple([int(ele[0])] + ele[1:]), data)))[1:-1]
            insert_data += data
            print(insert_data)
            cursor.execute(insert_data)
            conn.commit()
            print('插入成功')
        except:
            conn.rollback()
            print('回滚')
```



所有数据一般用while循环加fetchone()来获取，而不是fetchall()，数据量很大，会占用很大的开销。一般逐行获取。

~~~python
row = cursor.fetchone()

while row:
    row = cursor.fetchone()
~~~





### 非关系数据存储

全称Not Only SQL ，意为不仅仅SQL，泛指非关系数据库。NoSQL是基于键值对的，而不需要进行SQL层的解析，数据之间没有耦合性，性能非常高。

####  MongoDB

由C++语言编写的非关系数据库，一个基于分布式文件存储的开源数据库系统，内容存储形式类似JSON对象。

#####  连接Mongo

调用MongoClient类型获取连接对象

#### Redis









## 6、Ajax数据爬取

原始的页面最初不会包含某些数据，原始页面加载完后，回再向服务器请求某个接口获取数据，然后数据才会被处理从而呈现到网页上。

Ajax，全称Asynchronous JavaScript and XML ，即异步的JavaScript和XML。它不是编程语言，而是利用js在整个网页不被刷新，页面链接不改变的情况下与服务器进行数据交换并更新部分网页的技术。





## 7、动态渲染页面爬取

### 为什么要动态获取

页面可能部分是JS生成的，并非原始的HTML代码。

亦有可能是ECharts经过JS计算之后生成的。

亦有即使是Ajax获取的数据，但其接口含有很多加密参数，很难直接找出规律。



### 模拟浏览器运行的库

模拟浏览器运行，看到的什么，爬到的就是什么，不需要管源码是什么样的。**可见即可爬**

* Selenium

* Splash

* PyV8

* Ghost



### Selenium

自动测试化工具，利用它可以驱动浏览器执行特定的动作，通过驱动获取页面源代码。

支持非常多的浏览器，还有Android、BlackBerry等手机浏览器，也支持无界面浏览器PhantomJS。



##### 声明浏览器对象

~~~python
from selenium import webdriver

browser = webdriver.Chrome()
browser = webdriver.FireFox()
browser = webdriver.Edge()
browser = webdriver.Safari()
~~~



|               方法               |         释义         |
| :------------------------------: | :------------------: |
|             get(url)             |       请求页面       |
|          page_source()           |    获取页面源代码    |
|             close()              |      关闭浏览器      |



##### 无头浏览器


~~~python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_option = Options()
chrome_option.add_argument('--headless')
chrome_option.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_option)

~~~



##### 规避被监测的风险

~~~python
from selenium.webdriver import ChromeOptions
options = ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(options=options)
~~~








##### 查找节点

除了自带的方法、还可以根据XPath、CSS选择器等方式获取

|               方法               |         释义         |
| :------------------------------: | :------------------: |
|      find_element_by_name()      |    根据name值获取    |
|       ind_element_by_id()        |     根据id值获取     |
|  find_element_by_css_selector()  |  根据css选择器获取   |
|     find_element_by_xpath()      |    根据xpath获取     |
|  find_element(By.ID,'id value')  | 通用查找元素（单个） |
| find_elements(Bys.ID,'id value') | 通用查找元素（多个） |

###### 单个节点

* find_element_by_id
* find_element_by_name
* find_element_by_xpath
* find_element_by_link_text
* find_element_by_parial_text
* find_element_by_tag_name
* find_element_by_classname
* find_element_by_css_selector



###### 通用查找

~~~python
from selenium.webdriver.common.by import By

browser.find_element(By.ID,'q')
~~~



###### 多个节点

在获取单个的element加上s既可

* find_elements_by_id
* find_elements_by_name
* find_elements_by_xpath
* find_elements_by_link_text
* find_elements_by_parial_text
* find_elements_by_tag_name
* find_elements_by_classname
* find_elements_by_css_selector





##### 节点交互



驱动执行一些操作，让浏览器模拟一些动作。

|    方法     |   释义   |
| :---------: | :------: |
| send_keys() | 输入文字 |
|   clear()   | 清空文字 |
|  clikck()   | 点击按钮 |
|             |          |



##### 动作链

没有特定的执行对象，如鼠标拖拽，键盘按键等，就是动作链

```python
from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()

url = 'https://www.runoob.com/try/try.php?filename=jqueryui-example-draggable'
browser.get(url)
browser.switch_to.frame('iframeResult')
source = browser.find_element_by_css_selector('#draggable')
target = browser.find_element_by_css_selector('#draggable')
actions = ActionChains(browser)
actions.drag_and_drop(source,target)
actions.perform()
```



##### 执行JS

execute_script()

```python
from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://www.zhihu.com/explore')
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)') # 到最底部
browser.execute_script('alert("to Bottom")')
```



##### 获取节点信息

selenium提供了选择节点的方法，放回类型是WebElement类型，也有相关的方和属性来直接获取节点信息。

|  方法 or 属性   |          释义          |
| :-------------: | :--------------------: |
| get_attribute() |        获取属性        |
|      text       |       获取文本值       |
|       id        |         获取id         |
|    location     | 节点在页面中的相对位置 |
|    tag_name     |      获取标签名称      |
|      size       |   节点的大小（宽高）   |
|                 |                        |



##### 切换Frame

网页中有一种节点叫iframe，也就是子Frame，相当于子页面，他在结构和外部网页的结构完全一致。

默认是在父级Frame操作（正常页面）,切换到子Frame。**switch_to.frame()**方法。



##### 延时等待

get()方法会在网页框架加载结束后结束执行，此时获取的page_source()，可能不是浏览器完全加载的页面，可能由额外的Ajax请求，此时就需延时等待。

###### 隐式等待

 **browser.implicitly_wait(10)**

selenium没有在dom中找到节点，将会继续等待到设定时间（默认为0）后，如果最后没有找到就抛节点找不到异常。

当查找节点时，没有立即出现的时候，等待一段时间再去找dom，默认时间为0.

```python
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Chrome()
# 隐式等待
try:
    browser.implicitly_wait(10)
    browser.get('https://www.zhihu.com/explore')
    it = browser.find_element_by_id('root')
    print(it.text)
except NoSuchElementException:
    print('没有该节点')
```



###### 显示等待

隐式等待，只规定了时间，页面的加载时间会受到网络条件的影响

显示等待，指定要查找的节点，然后指定一个最长等待时间。如果在规定时间内加载处理啊，就放回查找的节点；如果在规定时间未加载出来则抛超时异常。

```python
browser.get('https://www.taobao.com')
try:
    wait = WebDriverWait(browser, 3)
    it = wait.until(EC.presence_of_element_located((By.ID, 'q')))
    btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btn-serach')))
    print(it, btn)
except TimeoutException:
    print('没有该节点')
```





###### 等待条件

| 方法                          |                释义                |
| :---------------------------- | :--------------------------------: |
| presence_of_element_located() | 节点加载出来，参数时节点的定位元组 |
| element_to_be_clickable()     |             节点可点击             |
| titile_is                     |              标题内容              |
| title_contains                |           标题包含某内容           |



```python
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as  EC
from selenium.webdriver.support.wait import WebDriverWait

# 显示等待
browser.get('https://www.taobao.com')
try:
    wait = WebDriverWait(browser, 3)
    it = wait.until(EC.presence_of_element_located((By.ID, 'q')))
    btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btn-serach')))
    print(it, btn)
except TimeoutException:
    print('没有该节点')
```



##### 前进和后退

forward()、back()

```python
import time

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.get('https://www.taobao.com')
browser.get('https://www.jd.com')
browser.back()
time.sleep(1)
browser.forward()
browser.close()
```





##### Cookies

对cookies进行获取、添加、删除等操作。

* get_cookies()

* get_cookie()

* add_cookie()

* delete_cookie()

* delete_cookies()

  

##### 选项卡管理

**browser.window_handles[1]**

```python
import time

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
# 打开新窗口
browser.execute_script('window.open()')
print(browser.window_handles)
# 切换窗口
browser.switch_to.window(browser.window_handles[1])
browser.get('https://www.jd.com')
time.sleep(1)
browser.switch_to.window(browser.window_handles[0])
browser.get('https://www.taobao.com')
```



###### 异常处理

* NoSuchElementException：没有找到节点
* TimeoutException：超时



### Splash

是一个JS渲染服务，还是应该带有HTTP API 的轻量级浏览器，同时对接了Python中的Twisted和QT库。同样可以用它实现动态渲染页面的抓取。

功能：

* 异步处理多个网页渲染过程
* 获取渲染后的页面的源代码或截图
* 通过关闭图片渲染或者使用Adblock规则来加快页面渲染速度
* 可执行特定的js脚本
* 可通过Lua脚本来控制页面的渲染过程
* 获取渲染的详细过程并通过HAR(HTTP Archive)格式呈现









## 8、验证码的识别



验证 码的种类：

* 普通图形
* 极验滑动
* 点触
* 微博宫格

### 图形验证码

#### 工具

* tesserocr

* PIL

~~~python
import tesserocr
from PIL import Image

image = Image.open('i1.jpg')
res = tesserocr.image_to_text(image)
print(res)
~~~



识别和实际结果有偏差，是因为验证码在内的多余线条干扰了图片的识别。可以额为的处理，如转灰度、二值化等操作。

利用image对象的`convert()`方法参数传入`L`，即为**转灰度**，传入`1`进行**二值化**。默认二值化阈值为127。

不能转换原图，应先转为灰度图像，然后在指定二值化的阈值。

~~~python
import tesserocr
from PIL import Image

image = Iamge.open('i2.png')
# 先转灰度
image = image.covert('L')
# 设定阈值
threshold = 80
table = []

for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
# 二值化
image = image.point(table, '1')
image.show()
# 获取验证码的字符串
res = tesserocr.image_to_text(image)
print(res)
~~~



### 极验滑动验证码

#### 步骤

* 分析识别思路
* 识别缺口位置
* 生成滑块拖动路径
* 模拟实现滑块拼合

  

#### 工具

* selenium
* chrome浏览器
* ChromeDriver



极验验证码，专注于提供验证安全的系统。



#### 特点

三角防护：

* 防模拟：模仿人类行为轨迹进行识别
* 防伪造：伪造设备浏览器环境进行识别
* 防暴力：短时间内进行密集攻击

通过selenium模拟人的行为进行验证。





## 9、代理的使用

解决封禁ip、隐匿ip等问题



### 代理池的维护



##### 准备工作

*  aiohttp
* requests
* redis-py
* pyquery
* Flask

##### 代理的目标
实现高效易用的代理池。

##### 基本模块

* 存储模块：存储抓取下来的代理，保证代理不重复，识别代理的可用情况，动态实时处理每个代理。

  * 高效和方便的存储方式：redis的sorted Set ，即有序集合。

* 获取模块：需要定时在各大代理网站抓取代理。代理可以是免费的也可以是付费的。

  * 代理的形式：ip+port
  * 尽量从不同来源获取，尽量抓高匿代理，抓取成功保存到数据库中。

* 检测模块：需要定时检测数据中的代理。需要设置一个检测代理，最好爬取哪个网站就检测那给网站，要有针对性。

  * 标识每个代理的状态：设置分数标识，100分表示可用，分数越少代表越不可用，当分数减到一定阈值后，就直接从数据库中移除。

* 接口模块：

  * 需要用API来提供对外的服务接口 。通过访问接口拿到可用的代理。

  

### ADSL拨号代理

  代理池可以挑选出许多的代理，但是常常稳定性不高，响应速度慢，通常为公共代理，不止一个人使用。所以封禁的概率很大。

  要追求稳定的代理，需要购买专有代理或搭建代理服务器，但是服务器一般都是固定IP，不可能100个代理就搭建100个服务器。



## 什么是ADSL

ADSL 非对称数字用户环路。

通过拨号的方式上网，需要输入ADSL账号和密码，每次拨号就换一个IP，每隔一段时间主机拨号就换一个IP，可以有效的防止IP封禁。

优点：稳定性很好，代理反应速度很快。

准备工作：

* requests
* redis-py
* tornado

##### 购买主句

先购买一台动态拨号VPS主机，如[云立方](http://www.yunlifang.cn/dynamicvps.asp)



## 10、模拟登录





## pyspider框架

爬虫框架，让我们可以不必关系爬虫的全部流程，异常处理、任务调度等，只需要关注爬虫核心业务逻辑即可。

爬虫框架提高开发效率和爬虫的健壮性。

pyspider是由国人binux编写的网络爬虫系统，GitHub地址为：<https://github.com/binux/pyspider>

优点：pyspider带有强大的WebUI、脚本编辑器、任务监控器、项目管理器以及结果处理器，它支持多种数据库、多种消息队列、JavaScript渲染页面等待爬取，使用方便。



##### pyspider 与 scrapy 的区别

1. pyspider提供了WebUI，Scrapy原始不提供，可通过Portia对接实现可视化配置；
2. pyspdier调试方便、WebUI操作便捷直观，Scrapy使用parse命令进行调试，方便程度不及pyspider；
3. pyspider内置pyquery作为选择器，Scrapy对接了XPath、CSS选择器和正则匹配；
4. pysider的可扩展程度不及Scrapy，可配置程度不高。Scrapy可以对接Middleware、Pipeline、Extension等组件实现非常强大的功能、模块之间的耦合程度低、可扩张程度高。



要快速实现一个页面的抓取，推荐pyspider,开发便捷。

应对反扒程度强、大规模的爬取 、推荐Scrapy，如抓取封IP、分帐号、高频验证的网站的大规模采集数据。

##### pyspider的架构

主要分为Scheduler(调度器)、Fetcher(抓取器)、Proccesser(处理器)三个部分，整个爬取过程受到了Monitor(监控器)，抓取的结构被Result Worker(结果处理器)处理。

![](./images/pyspider架gou.png)



Scheduler发起任务调度，Fetcher负责抓取页面，Processer负责解析网页内容，然后将新生成的Request发给Scheduler进行调度，将生成的提取结果输出保存。



##### 基本使用

Handler是pyspider爬虫的主类，可以在此定义爬取、解析、存储的逻辑。整个爬虫的功能只需要一个Handler即可。

* carwl_config：将项目的所有爬取配置统一定义到这，如定义Headers、设置代理等，配置之后全局全局生效。
* on_start()：爬取入口，初始的爬取请求会在这里产生，该方法通过调用crawl()方法既可以创建一个新的爬取请求，第一个参数是爬取的URL，另一个参数callback指定这个页面爬取成功后用哪个方法进行解析，代码中指定为index_page()方法。





### Scrapy框架

基于Twisted的异步处理框架，是纯Python实现的爬虫框架，架构清晰，模块之间的耦合度低，可扩展性强，可以灵活完成各种需求。

#### 架构



![](./images/Scrap架构.png)





|          模块          |                             作用                             |
| :--------------------: | :----------------------------------------------------------: |
|         Engine         | 引擎，处理整个系统的数据流处理、触发事务，是整个框架的核心。 |
|          Item          | 项目，定义了爬取结果的数据结构，爬出的数据结构会被赋值成该Item对象。 |
|       Scheduler        | 调度器，接受引擎发过来的请求并将其加入到队列中，在引擎再次请求的时候提供给引擎。 |
|       Downloader       |        下载器，下载网页内容，并将网页内容返回给蜘蛛。        |
|        Spiders         | 蜘蛛，其定义了爬取的逻辑和网页的解析规则，它主要负责解析响应并生成提取结果和新的请求。 |
|     Item Pipeline      | 项目管道，负责处理由蜘蛛到网页中抽取的项目，他的主要任务是清洗、验证和存储数据。 |
| Downloader MIddlewares | 下载器中间件，位于引擎和下载器之间的钩子框架，主要处理引擎与下载器之间的请求及响应。 |
|   Spider MiddlewARES   | 蜘蛛中间件，位于引擎和蜘蛛之间的钩子框架，主要处理蜘蛛输入的响应和输出的结果及新的请求。 |



#### 目录介绍

![](./images/scrapy目录介绍.jpg)







## 案例

### 猫眼爬取

~~~python
"""
@Time ： 2020/12/18 10:54
@Auth ： 侬&码
@File ：maoyantop100.py
@Description : 爬取猫眼top100
"""
import csv
import json
import os
import random
import re
import time

import requests

# top正则表达式
TOP_RE_STR = r'<dd>[\s\S]*?board-index-\d+">(\d+)</i>[\s\S]*?' \
             r'data-src="([\s\S]*?)"[\s\S]*?' \
             r'movieId:\d+}">(.+?)</a>[\s\S]*?' \
             r'主演：([\s\S]*?)\n[\s\S]*?' \
             r'上映时间：([\s\S]*?)</p>[\s\S]*?' \
             r'integer">(\d\.)[\s\S]*?' \
             r'fraction">(\d)'

movie_cols = (
    'rank', 'image_url', 'name',
    'star', 'release_data', 'country', 'score'
)


def get_page(url, proxies, offset=10):
    """
    获取页面
    :param url: 网址
    :param proxies: 代理
    :param offset: 偏移量
    :return: html页面
    """
    url += f'?offset={offset}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/87.0.4280.88 Safari/537.36'
    }
    resp = requests.get(url, proxies=proxies, headers=headers)
    page = resp.text
    if resp.status_code == 200 and page:
        return page

    return None


def get_data_re(page):
    """
    用正则获取数据
    :param page: 页面内容
    :return: 已处理的数据（列表）
    """
    top_re = re.compile(TOP_RE_STR)
    top_list = top_re.findall(page)
    if top_list:
        top = []
        for i in top_list:
            i = list(i)
            if '(' in i[-3]:
                i[-3], country = i[-3].split('(')
                i.insert(-2, country[:-1])
            else:
                i.insert(-2, '')

            # 评分设置
            score = i[-2] + i[-1]
            i.insert(-2, score)
            i = i[:-2]
            top.append(i)

    else:
        print('请检查正则或页面是否正确')
        print(page)
    return top


def to_dict(columns, data):
    """
    将字段和数据组成字典
    :param columns: 字段
    :param data: 序列数据
    :return: 字典
    """
    return [dict(zip(columns, item)) for item in data]


def to_csv(filename, data, columns=None, encoding='utf-8'):
    """
    将数据存储为csv文件，如有同名文件即是追加
    :param filename: 文件名
    :param data: 数据集
    :param columns: 字段
    :param encoding: 编码
    :return:
    """
    flag = os.path.exists(filename)
    with open(filename, 'a', encoding=encoding, newline='') as file:
        csv_file = csv.writer(file)
        if (not flag) and columns:
            csv_file.writerow(columns)

        for item in data:
            csv_file.writerow(item)


def to_txt_json(filename, data, columns=None, encoding='utf-8'):
    """
    将数据存储为txt文件，如有同名文件即是追加
    :param filename: 文件名
    :param data: 数据集
    :param columns: 字段
    :param encoding: 编码
    :return:
    """
    flag = os.path.exists(filename)
    print(flag)
    with open(filename, 'a', encoding=encoding) as file:
        if (not flag) and columns:
            print(columns)
            file.write(json.dumps(columns, ensure_ascii=False) + '\n')
        for item in data:
            file.write(json.dumps(item, ensure_ascii=False) + '\n')

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


def main():
    """ 主方法 """
    url = 'https://maoyan.com/board/4'
    # 代理url
    mogu_url = 'http://piping.mogumiao.com/proxy/api/get_ip_al' \
               '?appKey=b3e67385fc9449aea21aac7c02c1fe73&expiryDate=0' \
               '&format=1&newLine=2'
    pool = mogu_proxies_pool(mogu_url, 5)
    num = 0
    while True:
        for num in range(10):
            print(f'第{num + 1}页开始')
            proxies = {
                'https': random.choice(pool)
            }
            print(proxies['https'])
            page = get_page(url, proxies, num * 10)
            data = get_data_re(page)
            if data:
                for item in data:
                    print(item)
                to_csv('top.csv', data, movie_cols)
                print(f'第{num + 1}页保存成功')
                time.sleep(random.randint(6, 8))
            else:
                print('================爬取失败！未为获取页面===================')
                time.sleep(3)
                break
        else:
            print('================爬取完成！===================')
            break

        print('================爬取结束！===================')


if __name__ == '__main__':
    main()

~~~





### 京东商品爬取

```python
"""
@Time ： 2020/12/22 20:27
@Auth ： 侬&码
@File ：jdgoods.py
@Description :
"""
import os
import time

import pymongo
import ujson
from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def load_json_config(filename):
    """
    读取配置json文件
    :param filename: 文件名
    :return:
    """
    with open(filename, 'r', encoding='utf-8') as file:
        loads = ujson.loads(file.read())
    return loads


cfg = load_json_config('config.json')


def wait_located(wait, by: By, locator):
    return wait.until(expected_conditions.presence_of_element_located((by, locator)))


class Mongo():
    def __init__(self):
        global cfg

        if cfg:
            print(cfg)
            self.conn = pymongo.MongoClient(host=cfg['ip'], port=cfg['mongo']['port'])
            print(type(self.conn))
            self.db = self.conn[cfg['mongo']['db']]
            self.db = self.db.authenticate(cfg['mongo']['auth']['name'], cfg['mongo']['auth']['passwd'])

    def use_db(self, db):
        self.db = self.conn[db]
        return self.db

    def insert(self, table, data):
        if type(data) == list:
            self.db[table].insert_many(data)
        elif type(data) == dict:
            self.db[table].insert_one(data)
        data.clear()
        print("插入完成")


KEYWORD_PAGE_FILE_NAME = 'keyword_page.json'


class JDGoods:
    """ 提取京东商品 """

    def __init__(self, keyword):
        self.keyword = keyword
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.url = f'https://search.jd.com/Search?keyword={keyword}'
        self.driver.get(self.url)
        self.target = 0
        self.page = 1
        self.flag = True
        self.html = None
        self.data = []

    def redirect(self, page, target=0):
        if self.flag:
            if os.path.exists(KEYWORD_PAGE_FILE_NAME):
                with open(KEYWORD_PAGE_FILE_NAME, 'r', encoding='utf-8') as file:
                    data = ujson.loads(file.read())
                    if self.keyword in data.keys():
                        print(f'上次爬到{data[self.keyword]}页')
                        self.page = data[self.keyword] + 1
                    else:
                        self.page = page
            time.sleep(3)
            if target:
                self.target = target
            else:
                self.target = self.driver.find_element_by_xpath('//*[@id="J_topPage"]/span/i').text
                print(f'将爬取{self.target}')
            self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            wait_located(self.wait, By.XPATH, '//*[@id="J_goodsList"]/ul/li[60]')
            self.flag = False
        it = self.driver.find_element_by_xpath('//*[@id="J_bottomPage"]/span[2]/input')
        it.clear()
        it.send_keys(self.page)
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="J_bottomPage"]/span[2]/a').click()

    def access_good(self):
        print(f'正在爬取第{self.page}页')
        time.sleep(2)
        # self.driver.get_screenshot_as_file(f'./images/x-{self.page}.png')
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(3)
        wait_located(self.wait, By.XPATH, '//*[@id="J_goodsList"]/ul/li[60]/div/div[4]/strong/a')
        self.html = self.driver.page_source

    def extraction_data(self):
        if self.html:
            doc = pq(self.html)
            items = doc('#J_goodsList > ul > li ').items()
            img = 'div > div.p-img > a > img'
            for item in items:
                image = item.find(img).attr('src') if item.find(img) \
                    .attr('src') else item.find(img).attr('data-lazy-img')
                goods = {
                    'title': item.find('div > div.p-name.p-name-type-2 > a > em').text(),
                    'image': 'https:' + image,
                    'price': item.find('div > div.p-price > strong > i').text(),
                    'evaluate': item.find('div > div.p-commit > strong > a ').html(),
                    'shop_name': item.find('div > div.p-shop > span > a').text(),
                }
                self.data.append(goods)

    def close(self):
        if os.path.exists(KEYWORD_PAGE_FILE_NAME):
            with open(KEYWORD_PAGE_FILE_NAME, 'r', encoding='utf-8') as file:
                data = ujson.loads(file.read())
        with open(KEYWORD_PAGE_FILE_NAME, 'w', encoding='utf-8') as file:
            data[self.keyword] = self.page
            file.write(ujson.dumps(data))


if __name__ == '__main__':
    jd = JDGoods('ipad')
    mongo = Mongo()
    db = mongo.use_db('spider')
    lis = []
    while True:
        jd.redirect(1)
        lis.append(jd.access_good())
        jd.extraction_data()
        mongo.insert('goods', jd.data)
        if jd.page == jd.target:
            break
        jd.page += 1
    print(f'爬了{len(jd.data)}条数据')
    jd.close()
```



### 点触验证码登录boss直聘

```python
"""
@Time ： 2020/12/25 9:34
@Auth ： 侬&码
@File ：verify_login.py
@Description :
"""
import time
from hashlib import md5
from io import BytesIO

import requests
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

CJY_USERNAME = 'xxxx'
CJY_PASSWORD = 'xxxx'
CJY_SOFT_ID = 911112
CJY_KIND = 9005


class CJY(object):
    def __init__(self, username, password, soft_id):
        self.username = username
        password = password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files,
                          headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()


class BaseSn:
    """ selenium 登录类 """

    def __init__(self, url: str):
        """
        初始化
        :param url: 登录url
        """
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.wait = WebDriverWait(self.chrome, 15)
        self.chrome.get(url)

    def wait_key(self, action, by: By, locator: str):
        """
        延迟WebElement对象
        :param action: 具体行为
        :param by: 选择器类型
        :param locator: 选择器字符串
        :return:
        """
        if action == 'pl' or action == 0:
            return self.wait.until(EC.presence_of_element_located((by, locator)))
        elif action == 'ec' or action == 1:
            return self.wait.until(EC.element_to_be_clickable((by, locator)))


class VerifyLogin:
    """ 登录验证类 """

    def __init__(self, cjy: CJY, obj: BaseSn, image_obj):
        """

        :param cjy: 超级鹰对象
        :param obj: 登录对象
        :param image_obj: 验证码图片对象
        """
        self.cjy = cjy
        self.obj = obj
        self.image_obj = image_obj

    def get_position(self):
        """
        获取验证码图片位置
        :return: 位置
        """
        location = self.image_obj.location
        size = self.image_obj.size
        top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size[
            'width']

        return left, top, right, bottom

    def get_verify_image(self):
        """
        获取验证图片对象
        :return:
        """
        self.obj.chrome.get_screenshot_as_file('c.png')
        png = Image.open(BytesIO(self.obj.chrome.get_screenshot_as_png()))
        return png.crop(self.get_position())

    def get_captcha_json(self):
        """
        获取超级鹰验证json
        :return:
        """
        img = self.get_verify_image()
        bytes_array = BytesIO()
        img.save(bytes_array, format='PNG')
        captcha_json = self.cjy.PostPic(bytes_array.getvalue(), CJY_KIND)
        print(captcha_json)
        return captcha_json

    def get_offset(self):
        """
        获取验证字符的偏移量
        :return:
        """
        groups = self.get_captcha_json().get('pic_str').split('|')
        locations = [[int(number) for number in group.split(',')] for group in groups]
        print(locations)
        return locations

    def click_words(self):
        """
        动作链验证验证码
        :return:
        """
        for location in self.get_offset():
            ActionChains(self.obj.chrome) \
                .move_to_element_with_offset(
                self.image_obj, location[0], location[1]).click().perform()


if __name__ == '__main__':
    boos = BaseSn('https://login.zhipin.com/')
    cjy = CJY(CJY_USERNAME, CJY_PASSWORD, CJY_SOFT_ID)
    chrome = boos.chrome
    sms = boos.wait_key(1, By.CLASS_NAME, 'link-sms')
    sms.click()
    phone_input = boos.wait_key(0, By.NAME, 'phone')
    phone_input.send_keys('13895415358')
    # print(chrome.page_source)
    btn = boos.wait_key(0, By.XPATH, '//*[@id="wrap"]/div[2]/div[2]/div[2]/div[1]/form/div[4]/div[1]')
    btn.click()
    time.sleep(1)
    box = boos.wait_key(0, By.XPATH, '/html/body/div[5]')
    for i in range(3):
        img_obj = boos.wait_key(0, By.CLASS_NAME, 'geetest_widget')
        vl = VerifyLogin(cjy, boos, img_obj)
        vl.click_words()
        time.sleep(2)
        btn = boos.wait_key(1, By.CLASS_NAME, 'geetest_commit_tip')
        btn.click()
        time.sleep(2)
        if not box.is_displayed():
            print('验证成功')
            break
        print('验证失败，重试！')

    print('-----')
    time.sleep(2)
    sms_btn = boos.wait_key(1, By.XPATH, '//*[@id="wrap"]/div[2]/div[2]/div[2]/div[1]/form/div[5]/span/button')
    sms_btn.click()
    tel = boos.wait_key(0, By.NAME, 'phoneCode')
    tel.clear()
    code = input('输入手机验证码：')
    tel.send_keys(code)
    chrome.find_element_by_xpath('//*[@id="wrap"]/div[2]/div[2]/div[2]/div[1]/form/div[6]/button').click()

    time.sleep(3)
    boos.chrome.close()
```



### 微信公众号的爬取