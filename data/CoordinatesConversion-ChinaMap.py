# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 17:30:15 2017

@author: 张朴平
"""

'''经纬度坐标转换'''
import re
import data_location
import data_name

''' 将坐标转换成path的形式'''
def trans_path(load_dict):
	load_dict = str(load_dict)
	repla = re.compile("\].*?\[")
	result = re.sub(repla,' L ',load_dict)
	a = re.compile("\[\[")
	result = re.sub(a,'M ',result)
	b = re.compile("\]\]")
	result = re.sub(b,' ',result)
	return (result)

''' 获取所有坐标的y轴坐标'''
def get_Y (result):
	mine = re.compile(", \d+.\d+")
	middle = []
	location_y = []
	middle = re.findall(mine,result)
	sub = re.compile(', ')
	middle = re.sub(sub,'',str(middle))
	middle = middle.split('\'')
	location_y = middle[1::2]
	return (location_y)

''' 获取所有坐标的x轴坐标'''
def get_X (result):
	minex = re.compile("L \d+.\d+|M \d+.\d+")
	middlex = []
	location_x = []
	middlex = re.findall(minex,result)
	sub = re.compile('L |M ')
	middlex = re.sub(sub,'',str(middlex))
	middlex = middlex.split('\'')
	location_x = middlex[1::2]
	return (location_x)

''' 对所有坐标的y轴坐标进行变换'''
def trans_y(location_y):
	i = 0
	for elem in location_y:#反转并平移y
	    location_y[i] = 1.35*(70 - eval(location_y[i]))#y轴拉伸1.35倍
	    location_y[i] = str(location_y[i])
	    i += 1
	return (location_y)

''' 对所有坐标的x轴坐标进行变换'''
def trans_x(location_x):
	i = 0
	for elem in location_x:
	    location_x[i] = eval(location_x[i]) - 50 #反转并平移x
	    location_x[i] = str(location_x[i])+','
	    i += 1
	return (location_x)

''' 形成新的变换后的地址坐标'''
def get_newlocation(trans_x,trans_y):
	new_location = []
	i = 0
	for elem in trans_x:
	    new_location.append(trans_x[i]+trans_y[i])
	    i += 1
	new_location = 'M'+' L '.join(new_location)
	return (new_location)

'''主函数'''
#zuobiao = [[121.354795,31.13872]]
path = trans_path(data_location.o1)
#path = trans_path(zuobiao)
location_y = get_Y(path)#获取x与y的原始经纬度坐标
location_x = get_X(path)
trans_y = trans_y(location_y)#对x与y分别进行坐标变换
trans_x = trans_x(location_x)
newlocation = get_newlocation(trans_x,trans_y)#形成新的path路径
print ("<path id=\""+data_name.o+"\" d=\""+newlocation+'\"/>')
#print (newlocation)


#print (data_location.o)