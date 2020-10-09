class HashTable:
    def __init__(self, startingCapacity=40):
        self._table = []
        for i in range(startingCapacity):
            self._table.append([None])

    def insert(self, key, value):
        hashedKey = hash(key) % len(self._table)
        # if index is found in table
        if self._table[hashedKey] is not None:
            self._table[hashedKey] = [key, value]
        # if index is not found in table
        else:
            self._table[hashedKey].append([key, value])

    def getValue(self, key):
        hashedKey = int(key) % len(self._table)
        if self._table[hashedKey] is not None:
            return self._table[hashedKey][1]
        else:
            print("key not found")

    def getSize(self):
        size = 0
        for i in range(len(self._table)):
            if self._table[i] is not None:
                size += 1
        return size

    def delete(self, key):
        hashedKey = hash(key) % len(self._table)
        self._table[hashedKey] = [None]
