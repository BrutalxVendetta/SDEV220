# Super class
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

# Sub class
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        Vehicle.__init__(self, vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof


# Program start
print("Enter the information for the vehicle below.")
vehicle_type = "car"   # as required

year = input("Enter the year: ")
make = input("Enter the make: ")
model = input("Enter the model: ")
doors = input("Enter number of doors (2 or 4): ")
roof = input("Enter type of roof (solid or sun roof): ")

# Create object
my_car = Automobile(vehicle_type, year, make, model, doors, roof)

# Display results
print("")
print("Vehicle type: " + my_car.vehicle_type)
print("Year: " + my_car.year)
print("Make: " + my_car.make)
print("Model: " + my_car.model)
print("Number of doors: " + my_car.doors)
print("Type of roof: " + my_car.roof)
