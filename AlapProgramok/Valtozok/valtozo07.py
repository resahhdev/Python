"""
Írjon programot, amelynek első sora saját nevét és az aktuális dátumot írja a képernyőre.
A következő sorok egy „a” változóban 35-öt, majd egy „b” változóban 27-et tárolnak.
A program következői sorai cseréljék meg a két változó tartalmát.
Tehát az „a” változóban vegye fel „b” változó tartalmát, a „b” változó az „a” változó tartalmát.
Akkor is működjön a csere, ha az „a” és „b” változó más értékeket tartalmaz.
"""
a = 35
b = 27
c = 0
print( "Csere előtt" )
print( "Az a változó értéke: ", a )
print( "A b változó értéke: ", b )
print( "Csere..." )
c = a
a = b
b = c
print( "Csere után" )
print( "Az a változó értéke: ", a )
print( "A b változó értéke: ", b )