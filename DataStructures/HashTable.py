

# this class has a table of bucket lists
# each bucket list has a chain of buckets with key, value pairs
# using a hash function it can search for a value with a key provided
class HashTable:
    def __init__(self, startingCapacity=40):
        # initializes a list
        self._table = []
        # initializes an integer to track size of occupied buckets
        self._size = 0
        # sets each element of the list to an empty list or "bucket"
        for i in range(startingCapacity):
            self._table.append([])

    # returns the hashedKey value for the given key
    def hashFunction(self, key):
        # hashes the key and then returns the remainder after dividing by the table size
        hashedKey = hash(key) % len(self._table)
        return hashedKey

    # receives a key and a value and inserts into table
    def insert(self, key, value):
        # creates a hashed key
        bucket = self.hashFunction(key)
        # sets bucket list
        bucketList = self._table[bucket]
        # the bucket list is appended with new item
        bucketList.append([key, value])
        # increment size
        self._size += 1

    # returns a value for the given key
    # time - O(1) - O(N)
    def getValue(self, key):
        # creates a hashed key
        bucket = self.hashFunction(key)
        # sets bucket list
        bucketList = self._table[bucket]
        # loop through bucket list
        for i in range(len(bucketList)):
            # if key is found
            if bucketList[i][0] == key:
                # return value
                return bucketList[i][1]

    # returns the size of the table that is not set to None
    def getSize(self):
        return self._size

    # deletes a bucket by setting it to None
    def delete(self, item):
        # creates a hashed key using this hash function
        bucket = self.hashFunction(item)
        bucketList = self._table[bucket]
        # removes item from bucket list
        if item in bucketList:
            bucketList.remove(item)
            # decrement size
            self._size -= 1
