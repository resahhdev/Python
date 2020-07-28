"""
A KSH adatai szerint a Magyarországon a baromfiállomány az elmúlt időszakban
a következő képen alakult:

név	2015 június 1.	2016 június 1.
tyúk	37 895,8	36 688,3
kacsa	5 213,7	    5 709,9
lúd	    3 030,2	    3 514,0
pulyka	3 053,2	    3 253,4
Tegye változóba az összes adatot a táblázatban, a fejléc kivételével.
Írassa ki a következő paraméterek szerint:

az egyes oszlopokat „|” karakter mutatja
legyen egy fejléc sor, amely megegyezik a táblázat fejlécsorával
a fejléc sor után „-” karakterek legyenek elválasztónak
az állat neve 10 szélesen jelenjen meg
2015 és 2016-os értékek 20 szélesen jelenjenek meg
az értékek ezer darabban értendők,
minden érték teljes számmal jelenjen meg, tehát nem ezer darabban
a változókban viszont ezer darab legyen eltárolva
az értékek 1 tizedesjegy pontossággal jelenjenek meg
az utolsó sor, első oszlopában jelenítse meg az „Összeg: ” szöveget.
az értékek az „Összeg:” szöveggel egy sorban jelenjenek meg összegezve
az összegző sor elé tegyen egy elválasztó sort „-” karakterekből
az összeg is teljes számmal jelenjen meg, ne ezer darabban
az összeg is legyen 1 tizedesjegy pontos
ha az adott nyelv megengedi, állítson be minden értéknél ezredes tagolást
Kimeneti minta:

|        név |       2015 június 1. |       2016 június 2. |
------------------------------------------------------------
| tyúk       |         37 895 800,0 |         36 688 300,0 |
| kacsa      |          5 213 700,0 |          5 709 900,0 |
| lúd        |          3 030 200,0 |          3 514 000,0 |
| pulyka     |          3 053 200,0 |          3 253 400,0 |
------------------------------------------------------------
|    Összeg: |         49 192 900,0 |         49 165 600,0 |
"""

tyuk15 = 37895.8
tyuk16 = 36688.3
kacsa15 = 5213.7
kacsa16 = 5709.9
lud15 = 3030.2
lud16 = 3514.0
pulyka15 = 3053.2
pulyka16 = 3253.4
osszeg15 = 49192.9
osszeg16 = 49165.6


print( "|{:>10}|{:>20}|{:>20}|".format( "Név", "2015 junius 1.", "2016 junius 2." ))
for i in range( 54 ):
    print( "-", end = "")
print()
print( "|{:<10}|{:20,.1f}|{:20,.1f}|".format( "tyúk", tyuk15 * 1000, tyuk16 * 1000 ))
print( "|{:<10}|{:20,.1f}|{:20,.1f}|".format( "kacsa", kacsa15 * 1000, kacsa16 * 1000 ))
print( "|{:<10}|{:20,.1f}|{:20,.1f}|".format( "lúd", lud15 * 1000, lud16 * 1000 ))
print( "|{:<10}|{:20,.1f}|{:20,.1f}|".format( "pulyka", pulyka15 * 1000, pulyka16 * 1000 ))
for i in range( 54 ):
    print( "-", end = "")
print()
print( "|{:>10}|{:>20,.1f}|{:>20,.1f}|".format( "Összeg:", osszeg15 * 1000, osszeg16 * 1000 ))
