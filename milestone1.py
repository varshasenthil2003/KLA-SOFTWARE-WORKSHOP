#milestone1

#from cmath import cos, sin
import math
import numpy as np


with open("C:/Users/91948/Desktop/Kla hackathon/Milestone1/Input/Testcase3.txt", "r") as file1:
        read_content = file1.readlines()
        print(read_content)
data={}
for line in read_content:
        key, value = line.strip().split(':')
        data[key] = int(value)

print(data)
    
radius=data['WaferDiameter']/2
angle=data['Angle']
points=data['NumberOfPoints']

print(radius, angle, points )


'''print('ALL VALUES : ', diameter, n, angle)
radius=diameter/2


#from itertools import product

def points_in_circle(radius):
    for x, y in product(range(int(radius) + 1), repeat=2):
        if x**2 + y**2 <= radius**2:
            yield from set(((x, y), (x, -y), (-x, y), (-x, -y),))'''

           
'''l=list(points_in_circle(radius))
print(l)

#print(len(l))
'''
l=[]
r1=math.radians(angle)
r2=math.radians(angle+180)

x1= radius * math.cos(r1)
y1= radius * math.sin(r1)

print(x1,y1)

x2= radius * math.cos(r2)
y2= radius * math.sin(r2)

print(x2,y2)

x=np.linspace(x1,x2,points)
y=np.linspace(y1,y2,points)

answer=""
for i in range(0,points):
        p1=str(round(x[i],4))
        p2=str(round(y[i],4))
        coordinates='('+p1+','+p2+')'
        print(coordinates,end='\n')
        answer=answer+coordinates+'\n'

print(answer)


'''def points_in_cordinates(diameter,radius, n, angle):
    print("points: ", radius , n, angle)
    for i in range(0, n):
        #print(angle/n)
        tp = [i* (diameter/n) + angle + i * (angle/ n)]
        #print(tp)
        for j in tp:
            x=radius * math.cos(math.radians(j))
            y=radius * math.sin(math.radians(j))
            points=[x,y]
            l.append(points)
           

    return l

'''

with open ('C:/Users/91948/Desktop/Kla hackathon/Milestone1/outputof3.txt', 'w') as file:  
    file.write(answer)  
