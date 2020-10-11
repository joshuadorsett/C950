

# this class has a table of Key, Value buckets
# using a hash function it can search for a value with a key provided
class HashTable:
    def __init__(self, startingCapacity=40):
        # initializes a list
        self._table = []
        # sets each element of the list to an empty list or "bucket"
        for i in range(startingCapacity):
            self._table.append([None])

    # returns the hashedKey value for the given key
    def hashFunction(self, key):
        # hashes the key and then returns the remainder after dividing by the table size
        hashedKey = hash(key) % len(self._table)
        return hashedKey

    # receives a key and a value and inserts into table
    def insert(self, key, value):
        # creates a hashed key using this hash function
        hashedKey = self.hashFunction(key)
        # if index is found in table, this branch is selected
        if self._table[hashedKey] is not None:
            # the bucket is modified
            self._table[hashedKey] = [key, value]
        # if index is not found in table, this branch is selected
        else:
            # the bucket set to None is modified
            self._table[hashedKey].append([key, value])

    # returns a value for the given key
    # time - O(1)
    def getValue(self, key):
        # creates a hashed key using this hash function
        hashedKey = self.hashFunction(key)
        # if the bucket is not set to None
        if self._table[hashedKey] is not None:
            # returns the value of the bucket
            return self._table[hashedKey][1]
        else:
            # prints message if bucket is set to None
            print("bucket is empty")
            return None

    # returns the size of the table that is not set to None
    # time - O(N)
    def getSize(self):
        size = 0
        # loops through table
        for i in range(len(self._table)):
            # if the tables is not set to None
            if self._table[i] is not None:
                # increments size
                size += 1
        return size

    # deletes a bucket by setting it to None
    def delete(self, key):
        # creates a hashed key using this hash function
        hashedKey = self.hashFunction(key)
        # sets bucket with hashed key to None
        self._table[hashedKey] = [None]
