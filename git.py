#git学习
#ssh -T git@github.com
#git config --global user.name "your name"
#git config --global user.email "your_email@youremail.com"
#提交上传
# 1）接下来在本地仓库里添加一些文件，比如README
#
# 在本地新建一个README文件
#
# 然后在命令行输入一下命令
#
# $ git add README
#
# $ git commit -m "first commit"
# 我的执行界面如下
#
# 2）上传到github
#
# $ git push origin master
# git push命令会将本地仓库推送到远程服务器。
#
# git pull命令则相反。
#
# 注：首次提交，先git pull下，修改完代码后，使用git status可以查看文件的差别，使用git add 添加要commit的文件。
#
# 大功告成，现在你知道如何将本地的项目提交到github上了。



fatal: pathspec 'readme.txt' did not match any files 解决办法

Git中用，git init 创建好仓库后，目录就会多了 .git 的目录，它里面放了 Git 所需要的一些文件，先忽略。


如果要将某文件比如readme.txt放进仓库中可以输入：


git add readme.txt


但可能会出现这样的提示：

fatal: pathspec 'readme.txt' did not match any files


这说明在文件夹里并没有readme.txt这个文件
。
去库的文件夹下创建好readme.txt后，再次输入：


git add readme.txt


成功





git删除远程仓库的文件或目录

git rm -r --cached a/2.txt //删除a目录下的2.txt文件 

git commit -m "删除a目录下的2.txt文件" 

git push

Note:

用-r参数删除目录, git rm --cached a.txt 删除的是本地仓库中的文件，且本地工作区的文件会保留且不再与远程仓库发生跟踪关系，如果本地仓库中的文件也要删除则用git rm a.txt


在git bush中如何退出vim编辑器
2016-11-14 18:37 by 盛世游侠, 26397 阅读, 0 评论, 收藏, 编辑
写npm的pakege.json文件的files配置时，如果有不想包含的文件，那就要创建.npmignore文件排除，但windows系统又不允许创建以点开头命名的文件，咋办？

这时候就要用到linux命令行工具创建如git bash。

git bash创建文件和文件夹的命令如下：

复制代码
#创建文件
vi

#创建文件    
touch

#拷贝文件
cp

#移动文件
mv

#创建文件夹
mkdir

#另外还有好多命令能够创建文件，之要该命令能够重定向输出到一个不存在的#文件，就会创建文件。例如
tail -f -n 200 /usr/local/tomcat/logs/catalina.out > /tmp/tomcatlog.log 
复制代码
 

 但是git bush使用vi命令创建文件时进入到vim编辑器后，我不知道怎么退出，查了下发现一个方法：

  

  方法：一直按住esc ，再连续按大写的z两次就退出来了。

  但实际上，我发现，只要你按住shift键盘，下面的这些命令都可以用：

  1
  2
  3
  4
  5
  6
  7
  8
  9
  10
  如果你想编辑某个文档 可以直接编辑的如你有文档AA 可以用vi AA 【注意：必须在AA所在的目录下】
  如果没有文档而且你又想编辑就可以直接编辑vi aa【名字你可以随便命名】
  也可以先建立一个文档touch aa 然后再编辑vi aa
  编辑器有三种模式 1 命令行模式 2 末行模式 3 输入模式
  按Esc 就可以进入命令行模式也是系统默认模式
  输入模式可以按 o i a 都可以进入 退出可以进入末行和命令行模式
  末行模式可以按ctrl+；它的主要功能是退出编辑器 也可以保存退出文档
  q! 【强制退出不保存】 q【退出不保存】 wq【退出并保存后面也可以加个！】
  在输入模式和命令行模式命令很多 如果你想具体知道哪些你可以在和我说
  如复制（yy）粘贴（p) 删除（d）等等
  只是，用wq的时候，要先esc，然后按住shift键，出现下面这个界面时才可以输入命令：

How to resolve git's “not something we can merge” error



'''如何正确使用git提交命令

对于这个问题，最好的解决方法就是按如下步骤：
1.到根目录下：git add .；("."是必须要的)
2.git commit -m "some word"
3.git push -u origin master如果你只修改了一个文件，也可以在第一步中进入你修改了的目录下，然后将这个文件进行git add 文件名，接着进行下边的2，3步骤。。。
参考链接：http://www.mamicode.com/info-detail-262143.html

作者：山的那边是什么_
链接：https://www.jianshu.com/p/fb9f130906a4
來源：简书'''

简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。

