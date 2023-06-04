# fonksiyonlar
## def fonksiyon_adi(parametre1,parametre2...): yapilacak_islemler . . . .
```sh
def matematikte_dort_islem():
    print("Toplama")
    print("Çıkarma")
    print("Bölme")
    print("Çarpma")
```
```sh
matematikte_dort_islem()
```
Toplama
Çıkarma
Bölme
Çarpma

```sh
matematikte_dort_islem    
```

<function __main__.matematikte_dort_islem()>
matematikte_dort_islem:
  File "C:\Users\onurk\AppData\Local\Temp\ipykernel_11676\2971681725.py", line 1

 matematikte_dort_islem:    
                           ^

SyntaxError: invalid syntax
```sh
matematikte_dort_islem()
```
Toplama
Çıkarma
Bölme
Çarpma
```sh
def toplama(sayi1,sayi2,sayi3):
    print("Bu Üç Sayının Toplama İşlemi Sonucu: ", sayi1+sayi2+sayi3)

def çıkarma(sayi1,sayi2,sayi3):
    print("Bu Üç Sayının Çıkarma İşlemi Sonucu: ", sayi1-sayi2-sayi3)
    
def bölme(sayi1,sayi2,sayi3):
    print("Bu Üç Sayının Bölme İşlemi Sonucu: ", sayi1/sayi2/sayi3)
    
def çarpma(sayi1,sayi2,sayi3):
    print("Bu Üç Sayının Çarpma İşlemi Sonucu: ", sayi1*sayi2*sayi3)

toplama(5,6,7)

çıkarma(5,6,7)

bölme(5,6,7)

çarpma(5,6,7)
```
Bu Üç Sayının Toplama İşlemi Sonucu:  18

Bu Üç Sayının Çıkarma İşlemi Sonucu:  -8

Bu Üç Sayının Bölme İşlemi Sonucu:  0.11904761904761905

Bu Üç Sayının Çarpma İşlemi Sonucu:  210
```sh
def alan(kisa,uzun):
    print("Dikdörtgenin Alanı: ", kisa*uzun)
alan(5,30)
```
Dikdörtgenin Alanı:  150
```sh
def faktoriyel(sayi):
    sonuc = 1
    for i in range(1, sayi + 1):
        sonuc *= i
    return sonuc
faktoriyel(7)
```
5040
```sh
def topla(s1,s2,s3):
    return s1+s2+s3
topla(12,23,65)
```
100
```sh
def kare(s1):
    print("İşleminin Sonucu: ")
    return (s1)**2
kare(6)
```
İşleminin Sonucu: 
36
```sh
def tek_cift(sayi):
    if sayi % 2 == 0:
        return "Çift"
    else:
        return "Tek"
tek_cift(36)
```
'Çift'
```sh
def asal(sayi):
    if sayi < 2:
        return False
    for i in range(2, int(sayi ** 0.5)+1):
        if sayi % i == 0:
            return False
    return True
asal(23)
```
True
```sh
def ters(yazi):
    return yazi[::-1]
ters("onur")
```
'runo'
```sh
def toplama_islemi(s1,s2):
    return print(s1+s2)
toplama_islemi(5,6)
```
11
 
