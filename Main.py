from Package import Package
from HashTable import HashTable
from reader import *
Inventory = HashTable()

p1 = Package(1, "195 W Oakland Ave", "Salt Lake City", 84115, "12/31/1899 10:30:00 AM", 21, "not delivered")
Inventory.insert(p1.packageId, p1)
print(Inventory.search(1).deliveryStatus)
importAllData()