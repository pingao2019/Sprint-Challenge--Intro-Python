# Write classes for the following class hierarchy:

#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# class Vehicle is the base class for all other classes
class Vehicle():  
    pass

# FlightVehicle class is base class for class Airplane and Starship and child class of Vehicle
class FlightVehicle(Vehicle):   
    pass

#Starship class is child class of FlightVehicle
class Starship(FlightVehicle):   
    pass

class GroundVehicle(Vehicle):   # base class for class Car and Motorcycle and child of Vehicle
    pass

class Car(GroundVehicle):  # child class of GroundVehicle
    pass

class Motorcycle(GroundVehicle):# child class of GroundVehicle
    pass   

class Airplane(FlightVehicle):# child class of FlightVehicle
    pass



































