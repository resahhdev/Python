"""
Írjon programot, amelyben adott egy név és egy fizetés.
Írja ki a nevet 30 szélesen jobbra igazítva,
azt következő sorban a fizetést szintén 30 szélesen Ft utótaggal.
"""
nev = "Nagy Béla"
fizetes = 450000

print( "%30s" % nev )
print( "%30d Ft" % fizetes )