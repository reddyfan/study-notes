# git
[TOC]



## 配置



### 查看配置信息

```
git config --list
```



### 配置用户个人信息
```shell
git config --global user.name "reddy"
git config --global user.email "1312805094@qq.com"
```




## 创建仓库


**前提：**在`github`创建新仓库

~~~shell 
# 在github创建新仓库
git init
git add .
git commit -m "first commit" 
git remote add origin git@github.com:reddyfan/hi.git
git push -u origin master / git push --set-upstream origin master
~~~

