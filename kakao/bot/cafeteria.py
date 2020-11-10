class Cafeteria:
    def __init__(self, waiting, eating, finish):
        self.waiting = waiting
        self.eating = eating
        self.finish = finish

    def initialize(self):
        self.waiting = 0
        self.eating = 0
        self.finish = 0
    
    def addWaiting(self):
        self.waiting = self.waiting +1

    def addEating(self):
        self.eating = self.eating +1
    
    def addFinish(self):
        self.finish = self.finish +1
    
    def getValue(self):
        return self.waiting, self.eating