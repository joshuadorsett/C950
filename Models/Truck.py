from DataStructures.HashTable import *

class Truck:
    def __init__(self, truckId):
        self._truckId = truckId
        self._maxCargo = 16
        self._speed = 18
        self._cargoSize = 0
        self._packages = HashTable(16)

    def getId(self):
        return self._truckId

    def getPackages(self):
        return self._packages

    def addCargo(self, package):
        if self._cargoSize < self._maxCargo:
            self._packages.insert(package.getId(), package)
            self._cargoSize += 1
        else:
            print("cargo is full.")

    def removeCargo(self, packageId):
        self._packages.delete(packageId)
        if self._cargoSize > 0:
            self._cargoSize -= 1
        else:
            print("cargo is empty.")



