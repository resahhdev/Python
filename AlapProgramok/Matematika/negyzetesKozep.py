import math

"""
Vegye fel a következő változókat a következő értékekkel:

a = 15;
b = 21;
c = 13;
d = 27;
e = 33;
Számítsd ki a számok négyzetes közepét.

Négyzetes közép képlete
"""
# Q = sqrt(( x^ + y^ + z^ ... ) / n )

a = 15
b = 21
c = 13
d = 27
e = 33

aPow = math.pow( a, 2 )
bPow = math.pow( b, 2 )
cPow = math.pow( c, 2 )
dPow = math.pow( d, 2 )
ePow = math.pow( e, 2 )

powSum = aPow + bPow + cPow + dPow + ePow
divPow = powSum / 5
median = math.sqrt( divPow )

print( median )