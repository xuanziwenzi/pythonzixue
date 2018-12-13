win10终端退出jupyter notebook重新进入命令输入行呢？

同时按下ctrl和C键，然后按照下面终端界面提示操作就可以了。

conda env list
cnnda info -e
都可列出环境
* 表示当前所处的环境
base 表示默认的环境

conda env remove -n env_name
删除指定环境
conda env remove -n env_name --all
删除指定环境（如果不添--all参数，而是指明某个库名，则是删除该库）。



因为我现在安装的是最新版Anaconda3，其自带的Python版本为3.6，如果我们需要添加2.7版本的Python，
可以进行如下操作。（同理，如果有人安装的是Anaconda2需要添加Python 3.x，之后操作里的2.7改为3.6或3.5即可）

conda create -n py27 python=2.7

其中py27是新添加环境的名字，可以自定义修改。

之后通过activate py27和deactivate py27命令激活、退出该环境。
（Linux和OS系统的命令似乎是source activate和source deactivate）
activate py27


彩蛋1

由于我们现在安装的是Anaconda3，之后又新添加了Python 2.7环境，
但是Python 3.6环境中安装了Anaconda自带的科学计算环境，Python 2.7中却没有，
那么如何为新添加的环境也装上Anaconda的科学计算包呢，没必要一个一个来，
更没有必要再去安装Anaconda2了，只需：

conda install -n py27 anaconda

但是这会安装非常多，非常多，非常多的包，慎用。


彩蛋2

我们已经说完了Anaconda中的包管理，那么既然Anaconda中可以使Python 2.x和3.x共存，
Jupyter Notebook是否可以呢？


当然可以。

在这里我们不展开来介绍Jupyter Notebook，因为后面还会专门再写一篇，大家可以先初步了解。
多版本的Python或者R等语言，在Jupyter中被称作kernel。

如果想要给Jupyter添加多个Python版本的kernel，有两种做法。

如果这个Python版本已经存在（比如我们刚才添加的py27环境），
那么你可以直接为这个环境安装ipykernel包。即：

conda install -n py27 ipykernel

然后激活这个环境，输入

python -m ipykernel install --user


如果所需版本并不是已有的环境，可以直接在创建环境时便为其预装ipykernel。如：

conda create -n py27 python=2.7 ipykernel

#PS 如果想要在创建新版本环境时直接装上其他库，像这里的ipykernel一样直接附在后面就可以了。
#之后同样是激活环境并添加kernel。

#PPS 这个命令生成的其实是一个JSON文件，可以直接查看并修改。



希望大家从此不再因为选择版本、安装Python、管理环境、添加第三方库（能用conda用conda，不能用conda用pip）、
选择IDE（单文件Jupyter，项目组织开Pycharm）等等杂事所困扰，专心于代码。

（当然了，有一些库不论conda和pip都无法直接安装，只能下载.whl，这里不再赘述了，
小白同学遇到这种问题的时候，应该也有能力自己解决这种问题了）


祝进步，祝愉快！迟到的新年快乐！

# 催更只接受打赏…（说的好像有人打赏似的…说的好像有人打赏就会更似的…）





1.Anaconda3-4.4.0-Windows-x86_64的下载及安装
下载地址链接：http://pan.baidu.com/s/1miJudBU 密码：lo04
下载后直接点击安装，无脑点击下一步，选择你的安装路径，
我的安装路径为D:\ProgramData\Anaconda3，然后耐心等待，等到安装完成。


2.环境变量的配置
需要设置的环境变量路径如下：
D:\ProgramData\Anaconda3;
D:\ProgramData\Anaconda3\Scripts;
D:\ProgramData\Anaconda3\Library\mingw-w64\bin;
D:\ProgramData\Anaconda3\Library\usr\bin;
D:\ProgramData\Anaconda3\Library\bin;


3.测试是否安装正确
在cmd命令下输入conda info 
看到如下的界面证明安装成功


4.设置Anaconda镜像，加速下载
使用conda install 包名 安装需要的Python非常方便，但是官方的服务器在国外，
因此下载速度很慢，国内清华大学提供了Anaconda的仓库镜像，
我们只需要配置Anaconda的配置文件，添加清华的镜像源，然后将其设置为第一搜索渠道即可

cmd命令行下分别执行以下命令：

conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --set show_channel_urls yes
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/


可以看到.condarc文件的改变如下


然后可以测试一下，安装第三方包明显神速了，哈哈哈


5.Anaconda管理多个版本的Python环境
 (1)添加python2.7
执行命令：conda create --name python27 python=2.7，命令中我制定了环境名称是python27，
指定了Python版本是2.7，执行命令后，Conda会自动下载最新版的Python2.7，并自动部署

（2）查看你的系统当前已有的Python环境
执行命令：conda info --envs，从图中我们看到，这里多了一个名字为python27的Python环境


（3）切换Python环境


切换Python环境到刚才新添加的Python2.7，执行命令：activate python27，
然后执行命令：python --version，查看是否切换成功

Python27环境下，完成工作后，切回原来的Python环境，执行命令：deactivate python27
--------------------- 
作者：liuyunshengsir 
来源：CSDN 
原文：https://blog.csdn.net/liuyunshengsir/article/details/77671767 
版权声明：本文为博主原创文章，转载请附上博文链接！




尽量按照Anaconda默认的行为安装——不使用root权限，仅为个人安装，
安装目录设置在个人主目录下（Windows就无所谓了）。这样的好处是，
同一台机器上的不同用户完全可以安装、配置自己的Anaconda，不会互相影响。


配置好PATH后，可以通过which conda或conda --version命令检查是否正确。
假如安装的是Python 2.7对应的版本，运行python --version或python -V
可以得到Python 2.7.12 :: Anaconda 4.1.1 (64-bit)，也说明该发行版默认的环境是Python 2.7。


Conda的环境管理


Conda的环境管理功能允许我们同时安装若干不同版本的Python，并能自由切换。对于上述安装过程，
假设我们采用的是Python 2.7对应的安装包，那么Python 2.7就是默认的环境
（默认名字是root，注意这个root不是超级管理员的意思）。


假设我们需要安装Python 3.4，此时，我们需要做的操作如下：

# 创建一个名为python34的环境，指定Python版本是3.4
#（不用管是3.4.x，conda会为我们自动寻找3.4.x中的最新版本） 
conda create --name python34 python=3.4  
# 安装好后，使用activate激活某个环境 
activate python34      # for Windows 
source activate python34 # for Linux & Mac
#激活后，会发现terminal输入的地方多了python34的字样，实际上，
#此时系统做的事情就是把默认2.7环境从PATH中去除，再把3.4对应的命令加入PATH 
# 此时，再次输入 
python --version 
# 可以得到`Python 3.4.5 :: Anaconda 4.1.1 (64-bit)`，即系统已经切换到了3.4的环境
# 如果想返回默认的python 2.7环境，运行 
deactivate python34  # for Windows 
source deactivate python34 # for Linux & Mac 
# 删除一个已有的环境 
conda remove --name python34 --all

用户安装的不同python环境都会被放在目录~/anaconda/envs下，
可以在命令中运行conda info -e查看已安装的环境，当前被激活的环境会显示有一个星号或者括号。


说明：有些用户可能经常使用python 3.4环境，
因此直接把~/anaconda/envs/python34下面的bin或者Scripts加入PATH，去除anaconda对应的那个bin目录。
这个办法，怎么说呢，也是可以的，但总觉得不是那么elegant……


如果直接按上面说的这么改PATH，你会发现conda命令又找不到了
（当然找不到啦，因为conda在~/anaconda/bin里呢），这时候怎么办呢？
方法有二：1. 显式地给出conda的绝对地址
          2. 在python34环境中也安装conda工具（推荐）。

