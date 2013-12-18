__author__ = 'Benqing'

from filteringdata import computeNearestNeighbor
from filteringdata import recommend
from filteringdata import users

print computeNearestNeighbor('Hailey', users)
print recommend('Hailey', users)
print recommend('Chan', users)