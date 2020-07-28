

print( "Másolás tétel.")

numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
numbersCopy = []

print( "Eredeti lista: ")
for num in numbers:
    print( num, end = " ")
    numbersCopy.append( num * 2 )

print( "\nMásolt lista: ")
for num in numbersCopy:
    print( num, end = ' ' )