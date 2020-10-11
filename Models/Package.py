# holds all package information and methods to access and manipulate package information
class Package:
    # constructor initializes attributes with given arguments
    def __init__(self, packageId, address, city, zipCode, deadline, weight, specialNote):
        self._packageId = packageId
        self._address = address
        self._city = city
        self._zipCode = zipCode
        self._deadline = deadline
        self._weight = weight
        self._specialNote = specialNote
        self._deliveryStatus = "not delivered\n"
        # this bool is used for when a package address turns out to be the wrong address
        self._validInfo = True
        self._truck = None

    # setters
    def setDeliveryStatus(self, status):
        self._deliveryStatus = status

    def setTruck(self, truck):
        self._truck = truck

    def setAddress(self, address):
        self._address = address

    def setValidity(self, value):
        self._validInfo = value

    # getters
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

    def getValidity(self):
        return self._validInfo

    # print method that prints out all information for a specific package
    def print(self):
        printStream = "    ID: " + str(self._packageId) + \
            "\n    Address: " + self._address + \
            "\n    City: " + self._city + \
            "\n    ZipCode: " + str(self._zipCode) + \
            "\n    Deadline: " + self._deadline + \
            "\n    Weight: " + str(self._weight) + \
            "\n    Special Note: " + self._specialNote + \
            "    Assigned to Truck: " + str(self._truck.getId()) +\
            "\n    Delivery Status: " + self._deliveryStatus + \
            "\n\n"
        print(printStream)






