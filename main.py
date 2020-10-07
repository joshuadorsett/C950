from Models.Package import *
from DataStructures.HashTable import *
from Data.reader import *

if __name__ == "__main__":

    processData()

    WGUPS = HashTable()
    p1 = Package(1, "195 W Oakland Ave", "Salt Lake City", 84115, "12/31/1899 10:30:00 AM", 21, None)
    WGUPS.insert(p1.getId(), p1)
    print(WGUPS.getValue(p1.getId())._city)
