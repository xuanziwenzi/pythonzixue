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
