#coding= utf-8
#Authon：张三
#Version：0.0.2

a = 6
b = 3

#求模，余数
#整除，结果整数
#求幂
#格式化 %.1f  %d  %s
print(a%b)  
print(a//b)
print(a**b)


k=float(input('Please input 开尔文:'))
c= (k-32)/1.8
print(c)

format1 = 1.000000
format2 = 4
format3 = 'abcdefg'

print('float类型：%2.2f' % (format1))
print('int类型：%d' % (format2))
print('str类型：%5.1s' % (format3))
