# normál kiíratás
print( "{} {}".format( 23, 32 ))

# 10 szélesen jobbra
print( "{:>10}{:>10}".format( 23, 32 ))

# 10 szélesen balra jobbra 2 tizedes
print( "{:<10.2f}{:>10.2f}".format( 23.23456, 32.7654332 ))

# középre igazítás
print('{:^15}'.format( 123456 ))

# kitöltés alulvonással
print('{:_<10}'.format( 8400000 ))

# vezető 0
print( "Ár: {:010d} Ft".format( 840 ))

# ezredes tagolás
print('{:,d}'.format( 840000000 ))

# előjel
print('{:+d}'.format( 8400000 ))

szoveg = "Az ő neve {1}. {1} életkora: {0}"
print( szoveg.format( 34, "Mari" ))