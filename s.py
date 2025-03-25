# Autor: Arnold Róbert
# A modul szabadon használható alakítható
# Shift register 74hc595 vezérlése ESP-01 -el
# Jó szórakozást '_'

from machine import Pin
import time

a=''
p14 = Pin(0, Pin.OUT) # SER(adat) pin
p12 = Pin(2, Pin.OUT) # RCLK(zar) pin
p13 = Pin(1, Pin.OUT) # SRCLK(orajel) pin
p12.off()
p13.off()
p14.off()

def adat():
  p14.on()
  p13.on()
  p13.off()
  p14.off() 

def lep():
  p13.on()
  p13.off()

def kulcs():
  p12.on()
  p12.off()

def kiir(lista):
  global a
  a=lista
  lista=list(lista)
  lista=lista[::-1]
  for i in lista:
    if i==('0'):
      lep()
    else:
      adat()
  kulcs()

def tol(lepes,ido):
  for i in range(lepes):
    lep()
    kulcs()
    time.sleep_ms(ido)
  
def gorget(irany,lepes,ido):
  bemenet=a
  g=[]
  l=[]
  pinek=[]
  m=0
  for x in range(1,lepes+1,1):
    for i,j in enumerate(bemenet,1):
      if irany=='H':
        if j=='1':
          if i-x>0:
            l.append(i-x)
        if i==len(bemenet):
          g.append(l[m:])   
          m=len(l)     
      elif irany=='E':
        if j=='1':
          if i+x>0:
            l.append(i+x)
        if i==len(bemenet):
          g.append(l[m:])   
          m=len(l)
  for elem in g:
      r=''
      for i in range(len(bemenet)):
          if i+1 in elem:
              r+='1'
          else:
              r+='0'
      pinek.append(r)
  for j in pinek:
      kiir(j)
      time.sleep_ms(ido)

