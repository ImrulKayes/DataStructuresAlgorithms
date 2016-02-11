'''Design a parking lotThink simpleParking lot has 5 levels, each level has 30 partkingSpots, 10 parking spots per rowMotorcycles, cars and buses can park, the lot has motorcyle spot, compact and large spotsMotorcycles can park anywhere, car can park in single compact or large spot, bus needs five large spots, consequtive, in a row'''from abc import ABCMeta, abstractmethod # used for the abstract base classclass VehicleSize:    Motorcycle="Motorcycle"    Compact="Compact"    Large="Large"    class Vehicle:    # this tells us that this is an abstract class    __metaclass__=ABCMeta        def getSpotsNeeded(self):   return self.spotsNeeded    def getSize(self):  return self.size    "Park vehicle in this spot (among others, potentially)"    def parkInSpot(spot):        self.parkingSpots.append(spot)            "Remove car from spot, and notify spot that it's gone"    def clearSpots(self):        for parkingSpot in parkingSpots:            parkingSpot.removeVehicle()        self.parkingSpots=[]    @abstractmethod      def canFitInSpot(spot): pass    class Car(Vehicle):    def __init__(self):        self.spotsNeeded = 1        self.size = VehicleSize.Compact    def canFitInSpot(spot):        return spot.getSize()==VehicleSize.Large or spot.getSize() == VehicleSize.Compactclass Bus(Vehicle):    def __init__(self):        self.spotsNeeded = 5        self.size = VehicleSize.Large    def canFitInSpot(spot):        return spot.getSize()==VehicleSize.Large class Motorcycle(Vehicle):    def __init__(self):        self.spotsNeeded = 1        self.size = VehicleSize.Motorcycle    def canFitInSpot(spot):        return Trueclass ParkingLot:    NUM_LEVELS=5        def __init__(self):        self.levels=[Level(i,30) for i in range(self.NUM_LEVELS)]    def parkVehicle(vehicle):        for level in self.levels:            if level.parkVehicle(vehicle):                return True        return False    def print(self):        for level in self.levels:            leve.print()class Level:    SPOTS_PER_ROW = 10    def __init__(self,flr,numberSpots):        self.floor=flr        self.spots=[]        self.availableSpots = 0        largeSpots=numberSpots/4        bikeSpots=numberSpots/4        compactSpots= numberSpots - largeSpots - bikeSpots        for i in range(numberSpots):	    sz = VehicleSize.Motorcycle	    if i < largeSpots:                sz = VehicleSize.Large	    elif i < largeSpots + compactSpots:		sz = VehicleSize.Compact            row = i / SPOTS_PER_ROW	    self.spots.append(ParkingSpot(row, i, sz))	availableSpots = numberSpots        def availableSpots():   return availableSpots    "Try to find a place to park this vehicle. Return false if failed. "    def parkVehicle(vehicle):    "Park a vehicle starting at the spot spotNumber, and continuing until vehicle.spotsNeeded."    def parkStartingAtSpot(spotNumber, vehicle):    "find a spot to park this vehicle. Return index of spot, or -1 on failure. "    def findAvailableSpots(vehicle):    "When a car was removed from the spot, increment availableSpots"    def spotFreed():        class ParkingSpot:            def __init__(self,lvl,r,n,sz):        self.level=lvl        self.row=r        self.soptNumber=n        self.spotSize=sz    def isAvailable(self):        return self.vehicle==None    "Checks if the spot is big enough for the vehicle (and is available). This compares the SIZE only. It does not check if it has enough spots"    def canFitVehicle(self,vehicle):        return self.isAvailable() and vehicle.canFitInSpot()    def park(self,v):        if not self.canFitVehicle(v):            return False        self.vehicle=v        self.vehicle.parkInSpot()        return True        "Remove vehicle from spot, and notify level that a new spot is available"    def removeVehicle(self):        level.spotFreed()        self.vehicle=None        def getRow(self): return self.row    def getSpotNumber(self): return self.soptNumber    def getSize(self): return spotSize