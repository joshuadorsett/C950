class Package:
    def __init__(self, packageId, address, city, zipCode, deadline, weight, specialNote):
        self._packageId = packageId
        self._address = address
        self._city = city
        self._zipCode = zipCode
        self._deadline = deadline
        self._weight = weight
        self._specialNote = specialNote
        self._deliveryStatus = "not delivered\n"
        self._validInfo = True
        self._truck = None

    def setDeliveryStatus(self, status):
        self._deliveryStatus = status

    def setTruck(self, truck):
        self._truck = truck

    def setAddress(self, address):
        self._address = address

    def getAddress(self):
        return self._address

    def getId(self):
        return self._packageId

    def getDeadline(self):
        return self._deadline

    def getCity(self):
        return self._city

    def getZipCode(self):
        return self._zipCode

    def getWeight(self):
        return self._weight

    def getDeliveryStatus(self):
        return self._deliveryStatus

    # this will be set to true unless a package has a note about wrong address information like package 8
    def valid(self):
        return self._validInfo

    def setValidity(self, value):
        self._validInfo = value

    # print method that prints out all information for a specific package object
    def print(self):
        printStream = "ID: " + str(self._packageId) + \
            "\nAddress: " + self._address + \
            "\nCity: " + self._city + \
            "\nZipCode: " + str(self._zipCode) + \
            "\nDeadline: " + self._deadline + \
            "\nWeight: " + str(self._weight) + \
            "\nSpecial Note: " + self._specialNote + \
            "Assigned to Truck: " + str(self._truck.getId()) +\
            "\nDelivery Status: " + self._deliveryStatus + \
            "\n--------------------------------------------\n"
        print(printStream)






