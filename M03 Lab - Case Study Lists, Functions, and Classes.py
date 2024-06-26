#M03 Lab - Case Study: Lists, Functions, and Classes
#C.J. Becker
#6/25/2024
#make vehicle superclass with subclass with extra details and allow user input

#class to define what type of vehicle
class Vehicle:
    def __init__(self, v_type):
        self.v_type = v_type

#class to determine other details of vehicle
class Automobile(Vehicle):
    def __init__(self, v_type, year, make, model, doors, roof):
        super().__init__(v_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
    
    #print info
    def print_info(self):
        print("Vehicle type: " + self.v_type)
        print("Year: " + self.year)
        print("Make: " + self.make)
        print("Model: " + self.model)
        print("Number of doors: " + self.doors)
        print("Type of roof: " + self.roof)

vehinput = str(input("Enter type of vehicle: "))
myyear = str(input("Enter year of vehicle: "))
mymake = str(input("Enter make of vehicle: "))
mymodel = str(input("Enter model of vehicle: "))
mydoors = str(input("Does it have 2 or 4 doors?: "))
myroof = str(input("Does it have a solid or sun roof?: "))
myveh = Automobile(vehinput, myyear, mymake, mymodel, mydoors, myroof)
myveh.print_info()