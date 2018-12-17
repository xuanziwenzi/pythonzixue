#python学习
#第一次修改

pycharm单行和多行注释快捷键

单多行注释就一个组合键：选中+Ctrl+/

按a或者i
进入编辑模式
按esc
退出编辑模式
按：wq
保存并退出

zz


有时候想知道import的模块的文件路径，看看脚本，可以通过以下方式来查看：

Python 2.6.6 (r266:84292, Jul 23 2015, 15:22:56) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-11)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import identmodule
>>> print identmodule.__file__
/usr/lib/python2.6/site-packages/identmodule/__init__.pyc

通过模块的__file__属性来确定，这时候进入
/usr/lib/python2.6/site-packages/identmodule/ 目录就可以查看脚本了
--------------------- 
作者：云中不知人 
来源：CSDN 
原文：https://blog.csdn.net/u011085172/article/details/71466182 
版权声明：本文为博主原创文章，转载请附上博文链接！


python模块路径
Python会在以下路径中搜索它想要寻找的模块：

1. 程序所在的文件夹

2. 标准库的安装路径

3. 操作系统环境变量PYTHONPATH所包含的路径

 

将自定义库的路径添加到Python的库路径中去，有如下两种方法：

1. 动态的添加库路径。在程序运行过程中修改sys.path的值，添加自己的库路径

import sys

sys.path.append(r'your_path') 

2. 在Python安装目录下的\Lib\site-packages文件夹中建立一个.pth文件，内容为自己写的库路径。示例如下

E:\\work\\Python\\http

E:\\work\\Python\\logging
