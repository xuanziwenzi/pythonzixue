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

