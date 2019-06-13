#coding=utf-8

#version:0.01
#author:xyz
#date:2019-06-12

str = 'hello WORLD！'

print('字符串长度：',len(str))
print('字符串首字大写：',str.title())
print('全大写：',str.upper())
print('全小写：',str.lower())
print('大写？：',str.isupper())
print('小写？：',str.islower())
print('hello开头：',str.startswith('hello'))
print('HELLO开头：',str.startswith('HELLO'))
print('D!结束：',str.endswith('D!'))
print('D！结束：',str.endswith('D！'))


a = 2
b = 10
print(a**b)
print(a//b)
print(a%b)