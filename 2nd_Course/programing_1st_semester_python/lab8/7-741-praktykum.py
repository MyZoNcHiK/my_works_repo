from operator import itemgetter as ig
import operator
from operator import *
import operator as op
buildings = {
    "Shanghai Tower": 632,
    "Burj Khalifa": 828,
    "Abraj Al Bait": 601
}

print(sorted(buildings.items(), key=ig(1), reverse=True))
print(sorted(buildings.items(), key=operator.itemgetter(1)))
print(sorted(buildings.items(), key=itemgetter(0)))
print(sorted(buildings.items(), key=op.itemgetter(0), reverse=True))
