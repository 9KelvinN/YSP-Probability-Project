'''
Created on Jul 17, 2019

@author: ajp47
'''
from _overlapped import NULL

class Dude:
    
    def __init__(self, name):
        self.name = name
        self.speed = 2
        self.bikespeed = 10
        self.loc = 0
        self.hasBike = 0
        self.bike = NULL
    
    def move(self):
        if self.hasBike:
            self.loc += self.bikespeed
            self.bike.move(self.loc)
        else:
            self.loc += self.speed
    
    def pickUp(self):
        self.bike = 1
    
    def drop(self):
        self.bike = 0

class Bike:
    
    def __init__(self, loc):
        self.loc = loc
        
    def move(self):
    
    
    
