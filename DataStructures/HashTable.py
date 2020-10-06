class HashTable:
    def __init__(self, startingCapacity=40):
        self.table = []
        for i in range(startingCapacity):
            self.table.append([])

    def insert(self, key, value):
        hashedKey = hash(key) % len(self.table)
        # if index is found in table
        if self.table[hashedKey] is not None:
            self.table[hashedKey] = [key, value]
        # if index is not found in table
        else:
            self.table[hashedKey].append([key, value])

    def search(self, key):
        hashedKey = hash(key) % len(self.table)
        if self.table[hashedKey] is not None:
            return self.table[hashedKey][1]
        else:
            print("key not found")

    def delete(self, key):
        hashedKey = hash(key) % len(self.table)
        self.table[hashedKey] = [None]
