class Package:
    def __init__(self, packageId, address, city, zipCode, deadline, weight, specialNote):
        self._packageId = packageId
        self._address = address
        self._city = city
        self._zipCode = zipCode
        self._deadline = deadline
        self._weight = weight
        self._specialNote = specialNote
        self._graphIndex = None
        self._deliveryStatus = None

    def setDeliveryStatus(self, status):
        self._deliveryStatus = status

    def setGraphDestinationIndex(self, locations):
        for i in range(40):
            if locations.getValue(i).getAddress() == self._address:
                self._graphIndex = locations.getValue(i).getIndex()
            else:
                print("address not found in locations")

    def getId(self):
        return self._packageId



