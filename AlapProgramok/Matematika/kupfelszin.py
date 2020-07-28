import math

sugar = 2
magassag = 27
felszin = 0
# A = (pi * r^) + (pi * r *( sqrt r^ + h^))

alapKorTerulet = math.pi * math.pow( sugar, 2 )
gyokSugarMagassag = math.sqrt( math.pow( sugar, 2 ) + math.pow( magassag, 2 ))
sugarPi = math.pi * sugar
felszin = alapKorTerulet + ( sugarPi * gyokSugarMagassag )
print( felszin )
