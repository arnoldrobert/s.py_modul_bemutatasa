# s.py_modul_bemutatása
Fontos tudnunk, ha az ESP-01 microvezérlőt használjuk, nem működik a soros kommunikáció, mivel a Tx lábát is kimenetnek használja. Csak a WebREPL-ben programozható. A többi nagyobb mikrovezérlőnél a soros kommunikációt is tudjuk használni. A s.py modul támogatja a több shift register sorbakötését is.

> 8 bit ki/be kapcsolása

```python
from s import*
kiir('10101010')  # '0'-kikapcsolt, '1'-bekapcsolt állapot
```
> A megjelenítés legegyszerűbb módja (a ctrl+E segitségével több parancssort tudunk egyszerre bemásolni a WebREPL-be)

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

> Bitek görgetése előre vagy hátra

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
A shift register amikor előre lépkedünk, 8. bit után túlcsordul (ha egy shift register-t használunk). Az s.py modult úgy írtam meg, hogy visszafelé is ezt imitálja, vagyis hátrafelé is túlcsordul. A következő példában illusztrálom ezt.

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
