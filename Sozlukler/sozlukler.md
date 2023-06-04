# Sözlük - Dictionary
```sh
abc = {"elma":"apple", "pencere":"window", "kapı":"door"} # Metin ifadeler sözlükte bu şekilde işlenmektedir.
abc
```
{'elma': 'apple', 'pencere': 'window', 'kapı': 'door'}
```sh
xyz = {"istanbul":34, "adana":1, "ankara":6, "tekirdağ":59} # sayılar sözlükte bu şekilde işlenmektedir.
xyz
```
{'istanbul': 34, 'adana': 1, 'ankara': 6, 'tekirdağ': 59}
```sh
sozluk = dict() # boş sözlük bu şekilde oluşturulmaktadır.
sozluk
```
{}
## Sözlüğe Yeni Değer Ekleme ve Değerleri Çekme
```sh
plaka = {"istanbul":34, "adana":1, "ankara":6, "tekirdağ":59}
#Sözlüklerde Keys ve Value adında yapılar bulunmaktadır. Bu sözlük örneğimizde "istanbul" : Keys - 34 : Value değerini alır.
```
```sh
plaka["istanbul"]
```
34
```sh
plaka["adana"]
```
1
```sh
plaka["tekirdag"]
```
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
~\AppData\Local\Temp\ipykernel_21196\597699468.py in <module>
----> 1 plaka["tekirdag"]

KeyError: 'tekirdag'
```sh
  plaka["tekirdağ"]
```sh
  59
```sh
  yeni = {"solzuk1":[1,2,3,4,5,6,7,8,9,0], "sozluk2":[[1,3,5,7,9], [2,4,6,8]], "sozluk3":30}
yeni["sozluk2"]
```
[[1, 3, 5, 7, 9], [2, 4, 6, 8]]
```sh
  yeni["sozluk2"][1][1]
```
  4
```sh
  yeni["sozluk3"] 
```
30
```sh
  yeni["sozluk3"] += 10 # Sözlük içerisinde toplama işlemi
yeni["sozluk3"]
```
  40
```sh
  yeni
```
{'solzuk1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
 'sozluk2': [[1, 3, 5, 7, 9], [2, 4, 6, 8]],
 'sozluk3': 40}
## İç İçe Sözlük Yapıları
```sh
  bolgeler={"Marmara":{"istanbul":34, "tekirdağ":59, "kırklareli":39, "edirne":22}, "karadeniz":{"trabzon":61, "sakarya":54,"Amasya":5}, "Doğu":{"kars":36, "ardahan":75}}
bolgeler
  ```
{'Marmara': {'istanbul': 34, 'tekirdağ': 59, 'kırklareli': 39, 'edirne': 22},
 
  'karadeniz': {'trabzon': 61, 'sakarya': 54, 'Amasya': 5},
 
  'Doğu': {'kars': 36, 'ardahan': 75}}
```sh
  bolgeler["Marmara"]["istanbul"]
```
  34
