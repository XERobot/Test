#coding:utf-8

#version：0.01
#author：xyz
#date：2019-06-12

import math

r=float(input('请输入圆半径：'))
l=2*math.pi*r
s=math.pi*r*r
print('周长：%.2f' % l+'\n'+'面积: %.2f' % s)

