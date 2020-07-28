"""
Írjon programot, amely tárolja az e havi bevételt és kiadást
(pl: Kiadás: 280315500; Bevétel: 125270000).

Írassa ki az egyenleget, 30 szélesen, 3 tizedesjegy pontossággal, „Ft” egységként.
"""
kiadas = 280315500
bevetel = 125270000
egyenleg = bevetel - kiadas
print( "%30.3d ft" % egyenleg )