# linux



[TOC]







## 常用命令

| linux常用命令           | 查看版本                    |
| ----------------------- | --------------------------- |
| cat /etc/redhat-release | 查看版本                    |
| lastb                   | 显示最近登录用户的列表      |
| rmdir                   | 删除口文件夹                |
| touch                   | 创建文件/修改访问的最后时间 |
| !!                      | 执行刚刚执行的命令          |
| history -c              | 清除历史记录                |
|                         |                             |
|                         |                             |
|                         |                             |



### 查看文档

| 查看文档  |                                           |
| --------- | ----------------------------------------- |
| cat       | 查看看文件内容                            |
| head/tail | head/tail -10  ./index.html   (前/后10行) |
| more/less | 逐行查看文件内容                          |

### wget

* -o 重命令下载资源名

  ```
  wget https://www.baidu.com/ -o index.html
  ```

  

### 帮助文档

* --help
* man
* tldr：使用nodejs安装

### wc —统计行数、单词数

统计行数、字节数



| wc   |          |
| ---- | -------- |
| -w   | 单词数   |
| -l   | 统计行数 |
| -c   |          |



### lastb—统计登录失败次数

```
lastb | wc -l
```



### iconv—转编码

* -f ：当前编码
* -t：目标编码

~~~
inonv -f gb2312 -t utf-8 ./index.html
~~~



### cp—拷贝

* 递归式拷贝（拷贝文件夹）

~~~
cp -r test ../
~~~



### od—查看文件二进制

~~~
od time.jpg
~~~



### file—查看文件属性

```
file web/index.html 
"""
web/index.html: HTML document, UTF-8 Unicode text, with very long lines
"""
```



###  scp—安全拷贝

scp	发送主机用户@ip:文件路径	接收用户@ip：文件路径

~~~shell
scp html.tar root@39.105.2.205:/home/reddy/
~~~





### uniq—去重

```
uniq  fruits.txt
```



### sorted—排序

```
uniq  fruits.txt
```

去重排序

-计数 重复的次数

~~~
sorted fruits.txt | uniq -c
~~~







## 常用参数

|      |                                  |
| ---- | -------------------------------- |
| -v   | 打印执行过程中的操作打印一条信息 |
|      |                                  |
|      |                                  |
|      |                                  |



## 管道 重定向

### |—管道

*  操作系统提供的进程间通信的I/O通道

**将前一个命令的输出，作为后一个命令的输入**



### 重定向

| 重定向 |                |
| ------ | -------------- |
| >      | 重定向         |
| >>     | 追加重定向     |
| 2>     | 错误输出重定向 |
| <      | 输入重定向     |



## 压缩 归档

### 压缩/解压缩

* WinRAR	->	归档/解归档
* WinZip    ->     压缩/解压缩

| 压缩  | 解压缩 |
| ----- | ------ |
| gzip  | gunzip |
| xz -z | xz -d  |
|       |        |



### 归档和解归档



| 归档                                 | 解归档           |
| ------------------------------------ | ---------------- |
| tar -cf  test.tar  index.html  *.txt | tar -xf test.tar |
|                                      |                  |

```bash
tar -zcvf 12.tar.gz 1.txt 2.txt # 将1.txt和2.txt压缩并打包成12.tar.gz文件

tar -zxvf 12.tar.gz   # 解压并解包12.tar.gz文件
```

## CentOS如何安装软件和服务



### 包管理工具

#### yum

yum（全称为 Yellow dog Updater, Modified）是一个在Fedora和RedHat以及CentOS中的Shell前端软件包管理器。基于RPM包管理，能够从指定的服务器自动下载RPM包并且安装，可以自动处理依赖性关系，并且一次安装所有依赖的软件包，无须繁琐地一次次下载、安装。

|          命令行           |         作用         |        示例        |
| :-----------------------: | :------------------: | :----------------: |
| yum search <packagename>  |      搜索软件包      | yum search python  |
|    yum list installed     | 列出已经安装的软件包 | yum list installed |
| yum install <packagename> | 用来安装指定的软件包 |  yum install vim   |
|        yum remove         |    用来移除软件包    |   yum remove vim   |
| yum update <packagename>  |      更新软件包      |   yum updat tar    |
|     yum check-update      |       检查更新       |  yum check-update  |
|  yum info <packagename>   |  列出指定软件包详情  |  yum info python   |



#### rpm

rpm是“Red-Hat Package Manager”的简写，为 Red Hat专门开发的套件管理系统，方便软件的安装、更新及移除。所有源自Red Hat的“Linux ”发行版都可以使用 rpm.

|          命令行           |                 作用                 |                       示例                       |
| :-----------------------: | :----------------------------------: | :----------------------------------------------: |
| rpm -ivh <.rpm file name> | 安装.rpm后缀名的软件，并显示安装详情 | rpm -ivh google-chrome-stable_current_x86_64.rpm |
|   rpm -e <packagename>    |            删除指定的软件            |           rpm -r google-chrome-stable            |
|          rpm -qa          |        列出电脑上安装的所有包        |                     rpm -qa                      |

### 源代码构建安装

#### 源代码构建安装Git
下载源代码

```
wget https://mirrors.edge.kernel.org/pub/software/scm/git/git-2.27.0.tar.xz
```

解压缩和解归档

```
xz -d git-2.27.0.tar.xz ---> git-2.27.0.tar
tar -xf git-2.27.0.tar --->  git-2.27.0（文件夹）
```

安装前的准备工作

```
cd git-2.27.0
yum install -y libcurl libcurl-devel zlib zlib-devel
yum install -y gcc
./configure --prefix=/usr/local
```

编译源代码生成可执行程序

```
make && make install
```

通过下面的命令检查是否安装成功

```
git --version
whereis git
```



#### 源代码构建安装Python 3

补充安装Python 3需要用到的依赖项

```
yum install -y zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel libdb4-devel libpcap-devel xz-devel libffi-devel
```

下载和检查Python3的源代码

```
wget https://www.python.org/ftp/python/3.7.8/Python-3.7.8.tar.xz
md5sum Python-3.7.8.tar.xz
```

解压缩和解归档

```
xz -d Python-3.7.8.tar.xz
tar -xf Python-3.7.8.tar
```

安装前的准备工作

```
cd Python-3.7.8
./configure --prefix=/usr/local/python37 --enable-optimizations
```

构建和安装

```
make && make install
```

配置PATH环境变量

```
vim /etc/bashrc ---> 系统环境变量
vim ~/.bash_profile ---> 用户环境变量
---> Go
export PATH=$PATH:/usr/local/python37/bin
---> Esc ZZ
```

检查是否安装成功
    退出登录，重新登录，激活PATH环境变量

```
python3 --version
pip3 --version
```



### 二进制程序



## systemctl—服务启动



| systemctl |                  |
| --------- | ---------------- |
| start     |                  |
| stop      |                  |
| status    | 查看启动服务状态 |
| enable    | 开机自启         |
| disable   | 禁止自启         |

## 服务监听

### netstat

用来监听网络连接状态

| netstat |                                |
| ------- | ------------------------------ |
| -n      | 地址和端口的数值               |
| -t      | tcp                            |
| -l      | 正在监听                       |
| -p      | 显示进程信息                   |
| -a      | 显示所有socket，包括正在监听的 |
| -o      | 显示与与网络计时器相关的信息   |
| -u      | 显示UDP协议的连接情况          |

### ps

- 查看进程信息
- 使用:
  - ps -ef
  - ps aux



### kill

- 作用：杀死进程
- 示例：kill -9 PID
- 说明：强制杀死指定进程



## vim

### 工作模式

#### 命令模式

按Esc键切换到命令模式

| 命令/操作        | 说明                           |
| ---------------- | ------------------------------ |
| ZZ（shift + zz） | 保存退出                       |
| 光标定位         |                                |
| vim filename +n  | 打开文件，将光标定位到第n行    |
| vim filename +   | 打开文件，将光标定位到最后一行 |
| gg               | 定位到首行                     |
| G                | 定位到尾行                     |
| ngg              | 定位到第n行                    |
| ^/0              | 定位到行首                     |
| $                | 定位到行尾                     |
| k                | ↑                              |
| j                | ↓                              |
| h                | ←                              |
| l                | →                              |
| ctrl + f         | 下翻一页                       |
| ctrl + b         | 上翻一页                       |
| ctrl + d         | 下翻半页                       |
| ctrl + u         | 上翻半页                       |
| 内容处理         |                                |
| x                | 向右删除一个字符               |
| nx               | 向右删除n个字符，n表示个数     |
| X                | 向左删除一个字符               |
| nX               | 向左删除n个字符，n表示个数     |
| dd               | 删除光标所在行                 |
| ndd              | 删除光标开始的n行              |
| p                | 粘贴剪切板中的内容             |
| yy               | 复制光标所在行                 |
| nyy              | 复制光标开始的n行              |
| u                | 撤销                           |
| ctrl + r         | 反撤销                         |
| d0               | 删除到行首                     |
| d$               | 删除到行尾                     |
| dw               | 删除一个单词                   |



#### 编辑模式/末行模式

在命令模式下，按 : 键进入到编辑模式。

| 命令                    | 说明                                                |
| ----------------------- | --------------------------------------------------- |
| :w                      | 保存                                                |
| :q                      | 退出                                                |
| :wq                     | 保存退出                                            |
| :x                      | 保存退出                                            |
| :w!                     | 强制保存                                            |
| :q!                     | 强制退出，不保存修改                                |
| :e!                     | 放弃修改，恢复到修改之前的状态                      |
| :w newfile              | 文件另存为                                          |
| :set nu[mber]           | 显示行号                                            |
| :set nonu[mber]         | 隐藏行号                                            |
| :set tabstop=4          | 设置一个tab缩进4个字符                              |
| :set mouse=a            | 启用鼠标的点击功能                                  |
| [:]/内容                | 查找指定内容，n下翻，N上翻                          |
| [:]?内容                | 查找指定内容，N下翻，n上翻                          |
| :%s/原内容/新内容/[g]   | 所有行内容替换，g表示全局(默认只能替换一行中第一处) |
| :m,ns/原内容/新内容/[g] | m到n行内容替换，g用法同上                           |
| 光标定位                |                                                     |
| :n                      | 将光标定位到第n行，n表示行号                        |



#### 输入模式

| 命令 | 说明                             |
| ---- | -------------------------------- |
| i    | 在光标位置插入                   |
| I    | 在第一个非空字符插入             |
| a    | 在光标的下一个字符输入           |
| A    | 在行尾插入                       |
| o    | 在光标所在的行下面插入空行       |
| O    | 在光标所在的行上面插入空行       |
| s    | 删除光标所在字符，并进入输入模式 |
| S    | 删除光标所在行，并进入输入模式   |



### 配置.vimrc

进入用户目录下，创建.vimrc

配置参数

~~~bash
set nu
set ts=4
set expandtab
set autoindent
set ruler
syntax on
~~~



### vim高级操作

编辑模式执行

```bash
!ls 

!mkdir
...
```



#### vim多窗口操作

| 多窗口操作 |                    |
| ---------- | ------------------ |
| sp         | 水平拆分           |
| vs         | 垂直拆分           |
| ctrl + w   | 切换窗口（按两下） |
| :b 编号    | 切换文件           |
| ls         | 展示编辑的所有文件 |

#### vim -d 比较文件



## python脚本



### python可执行脚本

`encoding: utf-8` python2需加

```python
#!/usr/bin/python3
# encoding: utf-8
```

### sys.argv—命令行参数

`sys.argv：`  是一个元组，元组中第一个是文件名，之后是命令后面自己加的参数

```python
import sys

sys.argv
```

```bash
[reddy@reddy ~]$ mycal param1 param2
['/home/reddy/code/mycal', 'param1', 'param2']
       Dec 2020      
Su Mo Tu We Th Fr Sa
```



### 设置全局变量

* 临时修改全局变量：export PATH=$PATH:/home/reddy/code

* 永久修改全局变量：vim /etc/bashrc 
  * 加入`export PATH=$PATH:/home/reddy/code`



## ln -s —软链接

创建python快捷方式

```bash
ln -s /usr/local/python37/bin/python3  /usr/bin/python3
```



## alias—起别名

* 临时别名：alias 'll=ls -l'
* 取消别名：unalias ll
* 设置永久别名：`vim /root/.bashrc`  or `vim /用户目录/.bashrc`  or `.bash_profile`
  * alias ll='ls -l'



## 权限管理

### chmod—更改权限

- 说明：在linux下，所有的文件都涉及权限，分为三组：所有者、所属组、其他
- 权限：所有文件的权限可以分为：可读(r)、可写(w)、可执行(x)，'-'表示没有改权限
- 原理：ls -l的结果，三位一组，分为三组，刚好对应：所有者、所属组、其他
- 修改权限：chmod，格式：`chmod [身份] [操作] [权限] 文件`

| 选项 | 说明          |
| ---- | ------------- |
| 身份 |               |
| u    | 所有者(user)  |
| g    | 所属组(group) |
| o    | 其他(other)   |
| a    | 所有（all）   |
| 操作 |               |
| +    | 添加          |
| -    | 去掉          |
| =    | 设置          |
| 权限 |               |
| r    | 可读          |
| w    | 可写          |
| x    | 可执行        |



给其他用户添加可写的权限

```bash
sudo chmod o+w 1.py，
```



若要进行递归操作，则需要添加'-R'操作

```bash
sudo chmod -R  755 ../code/
```



### chown—更改所有者

~~~bash
sudo chown -R reddy:reddy /home/reddy/
~~~



## 批量操作



|       |                             |
| ----- | --------------------------- |
| mkdir | mkdir -p {a1,a2,a3}/{c1,c2} |
| yum   | yum install -y  gcc nodejs  |
|       |                             |
|       |                             |
|       |                             |



