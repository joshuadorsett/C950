class Package:
    def __init__(self, packageId, address, city, zipCode, deadline, weight, specialNote):
        self._packageId = packageId
        self._address = address
        self._city = city
        self._zipCode = zipCode
        self._deadline = deadline
        self._weight = weight
        self._specialNote = specialNote
        self._deliveryStatus = "not delivered"
        self._truck = None

    def setDeliveryStatus(self, status):
        self._deliveryStatus = status

    def setTruck(self, truck):
        self._truck = truck

    def getTruck(self):
        return self._truck

    def getAddress(self):
        return self._address

    def getId(self):
        return self._packageId

    # print method that prints out all information for a specific package object
    def print(self):
        printStream = "ID: " + str(self._packageId) + \
            "\nAddress: " + self._address + \
            "\nCity: " + self._city + \
            "\nZipCode: " + str(self._zipCode) + \
            "\nDeadline: " + self._deadline + \
            "\nWeight: " + str(self._weight) + \
            "\nSpecial Note: " + self._specialNote + \
            "\nAssigned to Truck: " + str(self._truck.getId()) +\
            "\nDelivery Status: " + self._deliveryStatus
        print(printStream)






