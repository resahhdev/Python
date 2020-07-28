
print( "Eldöntés tétel." )

numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

searching = 11
i = 0

while( i < len( numbers ) and numbers[ i ] != searching ):
    i += 1

if( i == len( numbers ) ):
    print( "Nincs meg a keresett érték." )
else:
    print( "A keresett értéket tartalmazza a lista." )