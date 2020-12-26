# tesserocr 安装和使用



tesserocr是python的应该OCR的识别库，是对tesseract做了一层封装，它的核心就是tesseract。因此在安装tesserocr应先安装tesseract。

tesseract目前支持到的python版本是3.7,之前尝鲜用了3.9出了很多错，推荐选择**python3.7版本**。

我整理一下，亲身试过可以用的：

链接：https://pan.baidu.com/s/1n2QQ_45lC2fk9d3EBKTyLQ  提取码：f9hu 


![](C:\Users\ReddyFan\Desktop\study notes\03-spider\images\install-1.jpg)

## 安装步骤：



* 先安装tesseract
* pip install wheel pillow
* pip install tesserocr



### tesseract

下载对应的tesseract，推荐4.0或者4.1

[tesseract下载地址](https://digi.bib.uni-mannheim.de/tesseract/)

* 一路next，到这勾选后两项。
* 之后选择你要安装的路径后，安装即可。
* 如遇报错一直按enter即可

![](C:\Users\ReddyFan\Desktop\study notes\03-spider\images\choose_data.jpg)



安装完成，配置环境变量，直接把安装目录添加到环境变量中



![](C:\Users\ReddyFan\Desktop\study notes\03-spider\images\env.jpg)





测试安装是否成功，`win+r`输入cmd回车。

输入tesseract -v，显示如下即成功。

![](C:\Users\ReddyFan\Desktop\study notes\03-spider\images\version.jpg)



测试验证码

![](C:\Users\ReddyFan\Desktop\study notes\03-spider\images\verification_code.jpg)

![](C:\Users\ReddyFan\Desktop\study notes\03-spider\images\test_1.jpg)





### pip install wheel pillow



先安装wheel 和 pillow库

~~~bash
pip install wheel pillow
~~~



之后选择对应版本的whl包，下载即可。

我百度网盘也有，如需自行选择[tesserocr对应python版本whl](https://github.com/simonflueckiger/tesserocr-windows_build/releases)

![](C:\Users\ReddyFan\Desktop\study notes\03-spider\images\whl.jpg)





只有对应了python版本的whl文件才能pip install

~~~bash
pip install ./tesserocr-2.4.0-cp37-cp37m-win_amd64
~~~





### 安装tesserocr

上述步骤完成，之后即可直接pip按照

~~~bash
pip install tesserocr
~~~

测试代码

```python
import tesserocr
from PIL import Image

image = Image.open(f'i1.png')
res = tesserocr.image_to_text(image)
print(res)
```



输出

![](C:\Users\ReddyFan\Desktop\study notes\03-spider\images\res.jpg)

