__author__ = 'asus'
#coding:utf-8



# 小驼峰法
#
# 变量一般用小驼峰法标识。驼峰法的意思是:除第一个单词之外，其他单词首字母大写。譬如
#
# int myStudentCount;
#
# 变量myStudentCount第一个单词是全部小写，后面的单词首字母大写。
#
# 大驼峰法
#
# 相比小驼峰法，大驼峰法(即帕斯卡命名法)把第一个单词的首字母也大写了。常用于类名，命名空间等。譬如
#
# public class DataBaseUser;

# what_he_dose = ' plays'
# his_instrument = ' guitar'
# his_name = 'Robert Johnson'
# artist_intro = his_name + what_he_dose + his_instrument
# print(artist_intro)

#
# num = 1
# # string = "2"
# # num2 = int(string ),这样被转换成同类型之后，就可以合并这两个变量了。
# # print(num + num2 )
# print(type(num)),这样可以看变量是什么类型

# words = "words" * 3
# print(words )

# word = "a loooooong word"
# num = 12
# string = "bang"
# total = string * (len(word) - num)
# print(total)

# #字符串的分片和索引
# name = 'My name is Mike'
#
# print(name[0])
# print(name[-4])
# print(name[11:14])
# print(name[5:])
# print(name[:5])

# word = 'friends'
# find_the_evil_in_your_friends = word[0] + word[2:4] + word[-3:-1]
# print(find_the_evil_in_your_friends )
#
# url = 'http://open.163.com/movie/2010/11/B/J/M6GOB7TT6_M6GOBOPBJ.html'
# file_name = url[-10:]
# print(file_name)


#字符串（相当于对象）的方法，例如car.drive(),ca.door.open(),car.light()

phone_number = '1386-666-0006'
hiding_number = phone_number.replace(phone_number[:9],'*' * 9)
print(hiding_number)
#模拟手机查找电话功能


#字符串格式化符
# print('{} a word she can get what she {} for.'.format('with','came'))
# print('{preposition} a word she can get what she {verb} for.'.format(preposition='with',verb='came'))
# print('{0} a word she can get what she {1} for.'.format('with','came'))

#查询城市天气
# city = input("write down the name of city:")
# url = "http://.......................".format(city)


