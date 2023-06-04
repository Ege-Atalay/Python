# Stringler
## String Oluşturma
**Stringler oluşturulurken tek tırnak - çift tırnak ve üç tırnak kullanabiliriz.**
```sh
'Onur KIZILARSLAN'
```
'Onur KIZILARSLAN'
```sh
" Ege ATALAY"
```
' Ege ATALAY'
```sh
"""Ege ATALAY"""
```
'Ege ATALAY'
**Not : Hangi tırnak ile başladıysan o tırnak ile bitirmelisin..!**
```sh
"Onur KIZILARSLAN'
```
File "C:\Users\onurk\AppData\Local\Temp\ipykernel_9060\682226933.py", line 1
    "Onur KIZILARSLAN'
                      ^
SyntaxError: EOL while scanning string literal

**Not 2 : Tırnak ile başlayan Stringler tırnak ile bitmelidir..!**
```sh
"Ege ATALAY
```
File "C:\Users\onurk\AppData\Local\Temp\ipykernel_9060\1920440395.py", line 1
    "Ege ATALAY
               ^
SyntaxError: EOL while scanning string literal
```sh
plaka = "İstanbul'un Plaka Kodu 34"
plaka
```
"İstanbul'un Plaka Kodu 34"

## Index ve Parçalama
```sh
soyad = "KIZILARSLAN"
soyad[0]
```
'K'
```sh
soyad[3]
```
'I'
```sh
soyad[-1]
```
'N'
```sh
soyad[3:5]
```
'IL'
```sh
soyad[2:8]
```
'ZILARS'
```sh
len(soyad)
```
11
```sh
isim = "EGE"
len(isim)
```
3
```sh
soyisim = "ATALAY"
personel = isim + soyisim
personel
```
'EGEATALAY'
```sh
personel = isim + " " + soyisim
personel
```
'EGE ATALAY'
```sh
soyisim*5
```
'ATALAYATALAYATALAYATALAYATALAY'
