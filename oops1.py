#intiate a class 
class employee:
    #special method /magic method/dunder method -constructor
    def __init__(self):
        print("started the data attributes") #to check this function automatically run
        self.id=123
        self.salary='20000'
        self.designation='software developer'
        print("data have been initiated")

    def travel(self,destination):
        print("This travel method was called manually")
        print(f" employee travelling to {destination}")
        
#creating an obj/instance
sam=employee()
#print(f"salary {sam.salary}")
sam.travel('agra')
