"""adding small numbers to a large one"""
import math

bignum = 1#math.pow(10, 9)

for i in xrange(1000000):
    bignum += math.pow(10,-6)
print bignum - 1 #math.pow(10, 9)
