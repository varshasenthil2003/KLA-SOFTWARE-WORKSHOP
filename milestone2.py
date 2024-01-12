import math
import numpy as np
import ast 

with open("C:/Users/91948/Desktop/Kla hackathon/Milestone2/Input/Testcase1.txt", "r") as file1:
        read_content = file1.readlines()
        print(read_content)
        
data={}

for line in read_content:
        key, value = line.strip().split(':')
        data[key] = (value)

print(data)

data['WaferDiameter']=int(data['WaferDiameter'])

print(data)

diameter=data['WaferDiameter']
height, width = data['DieSize'].strip().split('x')

height=int(height)
width=int(width)

print(height)
print(width)

dsv=ast.literal_eval(data['DieShiftVector'])
print(dsv)
dsv=list(dsv)

rd=ast.literal_eval(data['ReferenceDie'])
print(rd)
rd=list(rd)

print(dsv)
print(rd)


def coord(diameter,height, width, dsv, rd):
    print(type(height))
    print(type(width))
    x=dsv[0]
    y=dsv[1]
    print(x,y)
    llcx=rd[0]
    print(type(llcx))
    llcy=rd[1]
    print(llcx, llcy)
    x_, y_=0,0
    while(x_ < llcx and llcx > width):
        x_=width
        print('in loop' , x)

    
res=[]
res=coord(diameter,height, width, dsv, rd )
