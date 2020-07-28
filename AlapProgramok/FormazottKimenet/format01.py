"""
Írjon programot, amely a következő hőmérséklet adatokat, valós számok alakjában tárolja:

15,82
18,27
22,40
23,19
24,57
22,02
20,28
Az adatok hétfőtől vasárnapig egy hét adatait tartalmazzák.
A program írja ki egymás alá az adatokat.

A sorok a hőmérséklet adat értéket mutassák először, 1 tizedesjegy pontossággal,
15 szélesen, jobbra igazítva, előjellel,
a következő oszlop 10 szélességben, balra igazítva mutassa milyen napra esett.

Példa:

        15.8   hétfő
        18.2   kedd
        22.4   szerda
        23.1   csütörtök
        24.5   péntek
        22.0   szombat
        20.2   vasárnap
"""
a = 15.82
b = 18.27
c = 22.40
d = 23.19
e = 24.57
f = 22.02
g = 20.28
print( "{:>15.1f}\t\t{:<10}".format( a, "hétfő" ))
print( "{:>15.1f}\t\t{:<10}".format( b, "kedd" ))
print( "{:>15.1f}\t\t{:<10}".format( c, "szerda" ))
print( "{:>15.1f}\t\t{:<10}".format( d, "csütörtök" ))
print( "{:>15.1f}\t\t{:<10}".format( e, "péntek" ))
print( "{:>15.1f}\t\t{:<10}".format( f, "szombat" ))
print( "{:>15.1f}\t\t{:<10}".format( g, "vasárnap" ))