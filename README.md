# s.py_modul_bemutatása
Fontos tudnunk, ha az ESP-01 microvezérlőt használjuk, nem működik a soros kommunikáció, mivel a Tx lábát is kimenetnek használja. Csak a WebREPL-ben programozható. A többi nagyobb mikrovezérlőnél a soros kommunikációt is tudjuk használni.

> 8 bit ki/be kapcsolása

from s import*
kiir('10101010')  # '0'-kikapcsolt állapot, '1'-bekapcsolt állapot
gorget('E',8,350) # 'E'-előre, 'H'-hátra, 8-léptetés, 350 ms késleltetéssel
