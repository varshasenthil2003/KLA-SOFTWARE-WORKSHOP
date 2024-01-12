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

print('whole data', data)

diameter=data['WaferDiameter']
radius= diameter/2

height, width = data['DieSize'].strip().split('x')

height=int(height)
width=int(width)

print('height ', height)
print('Width', width)

dsv=ast.literal_eval(data['DieShiftVector'])
print('die shift vector', dsv)
dsv=list(dsv)

rd=ast.literal_eval(data['ReferenceDie'])
print('reference die', rd)
rd=list(rd)


print('die shift vector',dsv)
print('reference die',rd)


def is_point_inside_circle(x, y, diameter):

    radius = diameter / 2
    distance = math.sqrt(x**2 + y**2)

    print('Distance : ', distance)
    if (distance <= radius):
         return True
    else:
         return False


def coord(diameter,height, width, dsv, rd):
    print(type(height))
    print(type(width))
    x=dsv[0]
    y=dsv[1]
    print('dsv points ', x,y)
    llcx=rd[0]
    print(type(llcx))
    llcy=rd[1]
    print('rd points : ', llcx, llcy)
    x_, y_=0,0
    while(x_ < llcx and llcx > width):
        x_=x_ + width
        print('in loop' , x_)
    while(y_ < llcy and llcy > height):
        y_= y_ + height
        print("in loop ", y_)
    x_llcx=x_
    y_llcx=y_
    
    print(x_llcx)
    print(y_llcx)

    return y_llcx


res=[]
res=coord(diameter,height, width, dsv, rd )
print(res)


ans=is_point_inside_circle(height, width, diameter)
print(ans)


