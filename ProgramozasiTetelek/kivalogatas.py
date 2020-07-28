
print( "Kiválogatás tétel." )

numbersOrig = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
numbersEven = []

print( "Eredeti lista:")
for num in numbersOrig:
    print( num, end = " ")

for num in numbersOrig:
    if( num % 2 == 0 ):
        numbersEven.append( num )

print( "\nPáros lista:")
for num in numbersEven:
    print( num, end = " ")
