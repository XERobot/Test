#coding= utf-8
#输出类型要统一，连接字符串+，要么就是，分隔，当变量输出
import math

a = float(input("请输入："))

if a==0 :
    print("00000")
elif a>0 :
    print("11111")
else :
    print("-11111")




b = int(input("Enter："))
if b == 0:
    print(str(b)+"0+"+str(b))
else:
    if b < 0:
        print("-1+",b)  
    else:
        print(" 1+",b)

