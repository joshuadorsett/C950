class Package:
    def __init__(self, packageId, address, city, zipCode, deadline, weight, specialNote):
        self._packageId = packageId
        self._address = address
        self._city = city
        self._zipCode = zipCode
        self._deadline = deadline
        self._weight = weight
        self._specialNote = specialNote
        self._deliveryStatus = None

    def setDeliveryStatus(self, status):
        self._deliveryStatus = status

    def getId(self):
        return self._packageId



