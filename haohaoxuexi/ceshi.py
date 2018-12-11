##print('hello,',end = ' ')
##print('world.')

#5.4.2
##name = input('what is your name? ')
##if name.endswith(name):
##    print("hello,Mr.{}".format(name))
##    

#5.4.5
name = input('what is your name?')
if name.endswith('gumby'):
    if name.startswith("mr."):
        print('hello,mr.gumby')
    elif name.startswith('mrs.'):
        print('hello,mrs.gumby')
    else :
        print('hello,gumby')
else :
    print('hello,stringer')
              
              
