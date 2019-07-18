'''
Created on Jul 17, 2019

@author: Kel N
'''
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
spd1=2
bspd1=10
spd2=2
bspd2=10      
stPnt=200
Joe=Dude(spd1,bspd1,stPnt)
Jim=Dude(spd2,bspd2,stPnt)
Joe.pickUp()
times=[]
for bikePoint in range(0,210,10):
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
            times.append([bikePoint,time])
            break
    Joe.reset()
    Jim.reset()
    Joe.pickUp()
print(times)