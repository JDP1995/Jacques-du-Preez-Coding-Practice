# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, a

class Aircraft:
    def __init__(self,make,model,length,width,transponder):
        self.make = make
        self.model= model
        self.length= length
        self.width = width
        self.transponder = transponder

    def transponder_check(self):
        if self.transponder == True:
            print("Cleared for takeoff")


aircraft1= Aircraft("Boeing",737,10,3,True)

print(aircraft1.transponder_check())








