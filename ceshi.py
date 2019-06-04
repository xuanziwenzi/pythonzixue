##print('hello,',end = ' ')
##print('world.')

##5.4.2
##name = input('what is your name? ')
##if name.endswith(name):
##    print("hello,Mr.{}".format(name))
##    

# #5.4.5
# name = input('what is your name?')
# if name.endswith('gumby'):
#     if name.startswith("mr."):
#         print('hello,mr.gumby')
#     elif name.startswith('mrs.'):
#         print('hello,mrs.gumby')
#     else :
#         print('hello,gumby')
# else :
#     print('hello,stringer')
# print()
 #5.5.1
# name = ''
# while not name.strip():
#     name = input('please enter your name: ')
# print('Hello,{}'.format(name))

#5.5.2
# words = list("this is an pan".split())
# for word in words:
#     print(word)
# num = [1,2,3,4,5,6,7,8,9,10]
# for number in num:
#     print(number)
# for num in range(1,11):
#     print (num)

#5.5.3
#d = {'x':1,'y':2, 'z':3}
# for key in d:
#     print(key, 'correspons to',d[key])

# for key, value in d.items():
#     print (key, 'cc to', value)

# strings = list("this is an pan and pan".split())
# for string in strings:
#     if 'an' in string:
#         index = strings.index(string)#在字符串列表中查找字符串
#         strings[index] = '[censored]'
# print(strings)

# strings = list("this is an pan and pan".split())
# index = 0
# for string in strings:
#     if 'an' in string:
#         strings[index] = '[censored] '
#     index += 1
# print(strings)

#5.5.5 跳出循环
# from math import sqrt
# for n in range(200,0,-1):
#     root = sqrt(n)
#     if root ==int(root):
#         print(n)
#         break
# word='cnady'
# while word:
#     word = input('please enter a word: ')
# #    print('this is',word)
#     print('this is {}'.format(word))
#
#消除哑值
# word = input('please enter a word: ')
# while word:
#     print('this is',word)
#     word = input('please enter a word: ')
# while True:
#     word = input('please enter a word: ')
#     if not word: break
#     print('this is {}'.format(word))

#5.6简单推到
# girls = ['alice', 'bernice', 'clarice']
# boys = ['chris', 'aenold', 'bob']
# let = {}
# for girl in girls:
#     let.setdefault(girl[0],[]).append(girl)#####有说法
#     print(girl)
#     print (let)
# print([b+'+'+g for b in boys for g in let[b[0]]])


a = [1,2,3,4,5,6,7,8]
b = [2,3,4,5,6,7,8,9]
c = [3,4,5,6,7,8,9,10]
d = [5,6,7,8,9,10,11,12]
#result = []
#while True:
# for  i in range(len(a)):
#     result = []
#     result.extend([a[i],b[i],d[i],c[i]])
# #    sort(result)#####有说法
# #    result.sort()
#     y = sorted(result)
#     print(y)
# #    sorted(result)
# #print(y)

# def init(data):
#     data['first'] = {}
#     data['middle'] = {}
#     data['last'] = {}
# def lookup(data, label, name):
#     return data[label].get(name)
# def stroe(data, full_name):
#     names = full_name.split()
#     if len(names) == 2: names.insert(1, '')
#     labels = "first","middle","last"
#
#     for label, name in zip(labels, names):
#         people = lookup(data,label,name)
#         if people:
#             people.append(full_name)
#         else:
#             data[label][name] = [full_name]
# me = {}
# init(me)
# stroe(me, 'Ma Lie Het')
# lookup(me,'middle', 'Lie')

#class Bird:
#    song = 'aaa'
#    def


#coding:utf-8

def conflict(state, nextX):
        nextY = len(state)
        for i in range(nextY):
                if abs(state[i] - nextX) in (0, nextY - i):
                        return True
        return False

def queens(num = 8, state = ()):
        for pos in range(num):
                if not conflict(state, pos):
                        if len(state) == num - 1:
                                yield (pos,)
                        else:
                                for result in queens(num, state + (pos,)):
                                        yield (pos,) + result
c = 0
for res in queens(8):
        c += 1
        print ('Solution %d: ' % c)
        chest = [[0]*len(res) for i in range(len(res))]
        for i in range(len(res)):
                chest[i][res[i]] = 1
                print (chest[i])
        print ()