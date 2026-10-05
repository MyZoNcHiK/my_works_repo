from operator import itemgetter as ig
#from operator import *
buildings = {
    "Shanghai Tower": 632,
    "Burj Khalifa": 828,
    "Abraj Al Bait": 601
}

print(sorted(buildings.items(), key=ig(1), reverse=True))
print(sorted(buildings.items(), key=ig(1)))
print(sorted(buildings.items(), key=ig(0)))
print(sorted(buildings.items(), key=ig(0), reverse=True))
