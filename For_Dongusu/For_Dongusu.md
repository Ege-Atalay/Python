# For Döngüsü
```sh
rakam = [0,1,2,3,4,5,6,7,8,9]
for sayi in rakam:
    print("Rakamlar: ", sayi)
```
Rakamlar:  0

Rakamlar:  1

Rakamlar:  2

Rakamlar:  3

Rakamlar:  4

Rakamlar:  5

Rakamlar:  6

Rakamlar:  7

Rakamlar:  8

Rakamlar:  9
```sh
"t" in "türkiye"
```
True
```sh
"z" in "türkiye"
```
False
```sh
liste = [0,1,2,3,4,5,6,7,8,9]
genel_toplam = 0
for sayi in liste:
    genel_toplam += sayi
print("Listedeki rakamların genel toplamı: ", genel_toplam)
```
Listedeki rakamların genel toplamı:  45
```sh
liste = [0,1,2,3,4,5,6,7,8,9]
for sayi in liste:
    if sayi % 5 == 0:
        print(sayi)
```
0
5
```sh
ad = "Ege"
soyad = "Atalay"
for harf in ad:
    print(harf*5)
```
EEEEE
ggggg
eeeee
 
