

print( "Szétválogatás tétel." )

numbersOrig = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
numbersEven = []
numbersOdd = []

print( "Eredeti lista:" )
for num in numbersOrig:
    print( num, end = " " )

for num in numbersOrig:
    if( num % 2 == 0 ):
        numbersEven.append( num )
    else:
        numbersOdd.append( num )

print( "\nPáratlan lista: " )
for num in numbersOdd:
    print( num, end = " " )

print( "\nPáros lista: ")
for num in numbersEven:
    print( num, end = " " )
