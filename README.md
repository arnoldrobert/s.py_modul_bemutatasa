# s.py_modul_bemutatása
Fontos tudnunk, ha az ESP-01 microvezérlőt használjuk, nem működik a soros kommunikáció, mivel a Tx lábát is kimenetnek használja. Csak a WebREPL-ben programozható. A többi nagyobb mikrovezérlőnél a soros kommunikációt is tudjuk használni. A s.py modul támogatja a több shift register sorbakötését is. A WebREPL nem támogatja az ékezetes betűket, a megjegyzéseimet ne használjuk a kódokban.

> 8 bit ki/be kapcsolása

```python
from s import*
kiir('10101010')  # '0'-kikapcsolt, '1'-bekapcsolt állapot
```
> A megjelenítés legegyszerűbb módja (a ctrl+E segitségével 10 parancssort tudunk egyszerre bemásolni a WebREPL-be)

```python
from s import*
from time import*
kiir('00011000');sleep_ms(250)
kiir('00100100');sleep_ms(250)
kiir('01000010');sleep_ms(250)
kiir('10000001');sleep_ms(250)
kiir('01000010');sleep_ms(250)
kiir('00100100');sleep_ms(250)
kiir('00011000');sleep_ms(250)
kiir('00000000')
```
> Egymást lögdöső bitek
```python
from s import*
from time import*
x=0
bit=['00000000','00000001','00000010','00000100','00000101','00000110'\
     ,'00001010','00010010','00010100','00011000','00101000','01001000'\
     ,'01010000','01100000','10100000','00100000','01000000','10000000']
while True:
    for i in bit:
        if x<3 or x>=5 and x<7 or x>=9 and x<11 or x==13:
            t=300
        elif x>=3 and x<5 or x>=7 and x<9 or x>=11 and x<13 or x>13:
            t=100
        kiir(i);sleep_ms(t)
        x+=1
        if x>19:
            x=0
```
> Bitek be- és kicsorgása

```python
from s import*
from time import*
for i in range(1,9):
    z=(8-i)*'0'+i*'1'
    kiir(z);sleep_ms(150)
for i in range(1,9):
    z=(8-i)*'1'+i*'0'
    kiir(z);sleep_ms(150)
```
> Bitek görgetését a "gorget()" fügvénnyel végezhetjük. Az argumentumában beállíthatjuk, hogy "E" - előre, "H" - hátra, a léptetés számát és a késleltetés idejét ms-ban.

```python
gorget('E',8,350) # 'E'-előre, 'H'-hátra, 8-léptetés széma, 350 ms késleltetés
```
> 1 bit előre görgetése

```python
from s import*
kiir('10000000')
gorget('E',8,350) # 'E'-előre, 8-léptetés, 350 ms késleltetéssel
```
> 1 bit hátra görgetése

```python
from s import*
kiir('00000001')
gorget('H',8,350) # 'H'-előre, 8-léptetés, 350 ms késleltetéssel
```
A shift register amikor előre lépkedünk, 8. bit után túlcsordul (ha 1 shift register-t használunk). Az s.py modult úgy írtam meg, hogy visszafelé is ezt imitálja, vagyis hátrafelé is túlcsordul. A következő példában illusztrálom ezt.

> Lögdössük ki a biteket

```python
from s import*
kiir('11111111')    # '1'-bekapcsolt állapot
for i in range(9):  # felváltva lépked előre hátra és lögdösi ki a bit-ket
  if i % 2 == 0:
    x = 'E'
  elif i % 2 != 0:
    x = 'H'
  gorget(x,i,250)
```
