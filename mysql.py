#数据库mysql学习
#公众号有相关学习资料，这是娜娜

用inner join链接三个表

select * from (表A inner join 表B on A.字段名 = B.字段名)
inner join 表C on A.字段名 = C.字段名;

INNER JOIN 关联两张数据表的写法：
SELECT * FROM 表1 INNER JOIN 表2 ON 表1.字段号=表2.字段号

INNER JOIN 关联三张数据表的写法：
SELECT * FROM (表1 INNER JOIN 表2 ON 表1.字段号=表2.字段号) INNER JOIN 表3 ON 表1.字段号=表3.字段号

INNER JOIN 关联四张数据表的写法：
SELECT * FROM ((表1 INNER JOIN 表2 ON 表1.字段号=表2.字段号) INNER JOIN 表3 ON 表1.字段号=表3.字段号) INNER JOIN 表4 ON Member.字段号=表4.字段号

INNER JOIN 关联五张数据表的写法：
SELECT * FROM (((表1 INNER JOIN 表2 ON 表1.字段号=表2.字段号) INNER JOIN 表3 ON 表1.字段号=表3.字段号) INNER JOIN 表4 ON Member.字段号=表4.字段号) INNER JOIN 表5 ON Member.字段号=表5.字段号

day1

在命令行下输入 mysql -h localhost -u root -p回车,然后输入密码即可;或直接运行mysql自带的连接工具,然后输入密码即可.

1.编写sql脚本,假设内容如下:

  create database dearabao;
  use dearabao;
  create table niuzi (name varchar(20));

  保存脚本文件,假设我把它保存在F盘的hello world目录下,于是该文件的路径为:F:\hello world\niuzi.sql


2.执行sql脚本,可以有2种方法:
  第一种方法:
 在命令行下(未连接数据库),输入 mysql -h localhost -u root -p123456 < F:\hello world\niuzi.sql (注意路径不用加引号的!!) 回车即可.
  第二种方法:
 在命令行下(已连接数据库,此时的提示符为 mysql> ),输入 source F:\hello world\niuzi.sql (注意路径不用加引号的) 或者 \. F:\hello world\niuzi.sql (注意路径不用加引号的) 回车即可

 

上边为转载内容。我自己尝试如下：

我mysql没有设置密码。直接打开CMD，输入mysql，进入mysql命令行状态。输入source E:\123.sql


mysql> SELECT VERSION(), CURRENT_DATE;
mysql> SELECT SIN(PI()/4), (4+1)*5;
mysql> SELECT VERSION(); SELECT NOW();
mysql> SELECT
    -> USER()
    -> ,
    -> CURRENT_DATE;

mysql> SELECT * FROM my_table WHERE name = 'Smith AND age < 30;
    '> '\c
mysql>


如果你的机器上也有test数据库，通过下面的命令使用它
mysql> USE test
USE和QUIT一样，不需要分号，当然，如果你有强迫症，为了你的性命着想就加上分号吧，反正加上也没有害处。

USE特殊的另一点是，它不能跨行。


创建
mysql> CREATE DATABASE menagerie;


选择它
mysql> USE menagerie

直接选择它：
shell> mysql -h host -u user -p menagerie
Enter password: ********

查看当前被选择的数据库：
SELECT DATABASE();

创建这张表的样式
mysql> CREATE TABLE pet (name VARCHAR(20), owner VARCHAR(20),
    -> species VARCHAR(20), sex CHAR(1), birth DATE, death DATE);

mysql> SHOW TABLES;

mysql> DESCRIBE pet;

如果你的编辑器中用的是\r\n来换行，那你应该用下面这条命令：
mysql> LOAD DATA LOCAL INFILE '/path/pet.txt' INTO TABLE pet
    -> LINES TERMINATED BY '\r\n';

在苹果上，你应该换成：TERMINATED BY '\r'

如果命令失败了，应该是你mysql安装时没有选择默认本地文件处理功能。

当你想一条一条输入时，Insert 命令就有用武之地了。
mysql> INSERT INTO pet
    -> VALUES ('Puffball','Diane','hamster','f','1999-03-30',NULL);

字符串，日期，要用引号，空白用NULL


如果你能使用test数据库，那就用吧，但是test数据库上的数据可能被任何其他有权限使用test数据的人删除掉，所以最好建立自己的数据库。

假设你需要使用你的数据库（上面建立的动物园），管理员需要执行下面的命令：
mysql> GRANT ALL ON menagerie.* TO 'your_mysql_name'@'your_client_host';

your_mysql_name 就是你的账户名，your_client_host是你用来登陆服务器的机器地址


day2
查找所有资料：
mysql> SELECT * FROM pet;

    a.修改pet.txt，然后删除pet 表，再load data

　　mysql> DELETE FROM pet; 
　　mysql> LOAD DATA LOCAL INFILE 'pet.txt' INTO TABLE pet;

　　b.Update 只修改错误的信息

　　mysql> UPDATE pet SET birth = '1989-08-31' WHERE name = 'Bowser';

　　update只修改不符合要求的数据，不用重新加载源数据


选择指定的行
mysql> SELECT * FROM pet WHERE name = 'Bowser';
mysql> SELECT * FROM pet WHERE birth >= '1998-1-1';
mysql> SELECT * FROM pet WHERE species = 'dog' AND sex = 'f';

选择特定的列
mysql> SELECT name, birth FROM pet;

查看宠物的主人
mysql> SELECT owner FROM pet;
mysql> SELECT DISTINCT owner FROM pet;

对出生日期的排序
mysql> SELECT name, birth FROM pet ORDER BY birth;

默认排序是升序，如果你需要降序，需要加上DESC
mysql> SELECT name, species, birth FROM pet
    -> ORDER BY species, birth DESC;


日期计算
mysql提供了一些函数，方便你计算日期，

计算宠物的寿命，使用TimeStampdiff（）函数，参数是你想得到结果的单位，这里是年

mysql> SELECT name, birth, CURDATE(),
    -> TIMESTAMPDIFF(YEAR,birth,CURDATE()) AS age
    -> FROM pet;


需要按年龄排序，只需要简单修改下：
mysql> SELECT name, birth, CURDATE(),
    -> TIMESTAMPDIFF(YEAR,birth,CURDATE()) AS age
    -> FROM pet ORDER BY age;


如果你想知道哪个动物下个月过生日怎么办？要做这种计算，年和日都是相关的，你只想提取月份数据，mysql提供了几个函数去提取日期中的一部分，比如year(),month(),dayofmonth()

这里要用到的是month函数
mysql> SELECT name, birth, MONTH(birth) FROM pet;

现在要找出下个月过生的宠物也是很简单的，比如 ，现在 4月，那么下个月就是五月
mysql> SELECT name, birth FROM pet WHERE MONTH(birth) = 5;

注意，如果现在是12月，要记住你该查找的是1月而不是13月

你可以通过下面的语句来查询结果，而不用在意现在是哪个月，所以你不要使用特定的月份。Date add()函数能加一定的时间到给定的时间，如果你身Curdate（）加一定时间

然后就可以通过month()函数提取你想找的下个月过后日的宠物了。

mysql> SELECT name, birth FROM pet
    -> WHERE MONTH(birth) = MONTH(DATE_ADD(CURDATE(),INTERVAL 1 MONTH));
另一种方法是对当前月份取余，对12的余数如果是0,那么加1
mysql> SELECT name, birth FROM pet

Month（）返回1~12的数，Mod（）返回0~11的数，所以1应该放在mod()后面，否则，就会从11月直接跳到了1月。


以fy结尾的名字
mysql> SELECT * FROM pet WHERE name LIKE '%fy';

查找以b开头的名字：
mysql> SELECT * FROM pet WHERE name LIKE 'b%';

包含字母w的名字
mysql> SELECT * FROM pet WHERE name LIKE '%w%';

包含5个字母 的名字，用5个 _
mysql> SELECT * FROM pet WHERE name LIKE '_____';



Regexp　　 只要是这种模式就会匹配成功，而Like则必须匹配完整的值。


mysql> SELECT * FROM pet WHERE name REGEXP '^b';
mysql> SELECT * FROM pet WHERE name REGEXP BINARY '^b';
mysql> SELECT * FROM pet WHERE name REGEXP 'fy$';
mysql> SELECT * FROM pet WHERE name REGEXP 'w';
mysql> SELECT * FROM pet WHERE name REGEXP '^.....$';
mysql> SELECT * FROM pet WHERE name REGEXP '^.{5}$';











































