
print( "Metszet tétel." )

numbersOne = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
numbersTwo = [ 11, 2, 13, 14, 5, 16, 17, 8, 19, 20 ]
numbersSection = []

print( "Első lista:")
for num01 in numbersOne:
    print( num01, end = " " )

print( "\nMásodik lista:")
for num02 in numbersTwo:
    print( num02, end = " " )

for num01 in numbersOne:
    for num02 in numbersTwo:
        if( num02 == num01 ):
            numbersSection.append( num02 )#i += 1

print( "\nMetszet lista:")
for num in numbersSection:
    print( num, end = " " )
