'''
Created on Jul 17, 2019

@author: Kel N
'''
import matplotlib.pyplot as pyplt
from functools import reduce

class Dude:
    
    def __init__(self,spd, bspd,stPnt):
        self.speed = spd
        self.bikespeed = bspd
        self.loc = 0
        self.hasBike = True
        self.stopPoint=stPnt
        self.reached=False    
    def move(self):
        if self.reached:
            return
        if self.hasBike:
            self.loc += self.bikespeed
        else:
            self.loc += self.speed
        if self.loc>=stPnt:
            self.reached=True
    def pickUp(self):
        self.hasBike = True
    
    def drop(self):
        self.hasBike = False
    def reset(self):
        self.loc=0
        self.hasBike=False
        self.reached=False
#https://gist.github.com/endolith/114336/eff2dc13535f139d0d6a2db68597fad2826b53c3
def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a
def lcm(a, b):
    return a * b / gcd(a, b)
def LCM(*nums):
    return reduce(lcm,nums)

spd1=1
bspd1=3
spd2=2
bspd2=4
stPnt=20
step=(int)(LCM(spd1,bspd1,spd2,bspd2))
stPnt=stPnt*step**2 + step
Joe=Dude(spd1,bspd1,stPnt)
Jim=Dude(spd2,bspd2,stPnt)
Joe.pickUp()
times=[]
bikePoints=[]
for bikePoint in range(0,stPnt, step):
    time=0
    while 1:
        time+=1
        if Joe.loc==bikePoint:
            Joe.drop()
        Joe.move()
        if Jim.loc==bikePoint:
            Jim.pickUp() 
        Jim.move()
        if Joe.reached and Jim.reached:
            time/=1.0*step**2
            bikePoint/=1.0*step**2
            bikePoints.append(bikePoint)
            times.append(time)
            if bikePoint==0:
                low=(bikePoint,time)
            elif time<low[1]:
                low=(bikePoint,time)
            break
    Joe.reset()
    Jim.reset()
    Joe.pickUp()
print(low)
pyplt.plot(bikePoints,times,'bo')
pyplt.xlabel('Bikepoints')
pyplt.ylabel('Time Taken')
pyplt.title('The Relationship between the Point the Bike was Dropped and the Time Taken')
dimensionx,dimensiony=max(bikePoints),max(times)
pyplt.text(dimensionx/4, dimensiony*9/10, 'R1W=' +str(Joe.speed) + ', R1B=' +str(Joe.bikespeed) + ', R2W=' +str(Jim.speed)+', R2B=' +str(Jim.bikespeed))
pyplt.axis([0,dimensionx,0,dimensiony])
pyplt.grid(True)
pyplt.show()
