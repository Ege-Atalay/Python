# listeler
## Liste Oluşturma
```sh
meyveler = ['elma', 'armut', 'üzüm', 'karpuz'] # listelerde ve bunun gibi gruplarda ilk eleman (elma) 0 olarak kabul edilir. 
meyveler 
```
['elma', 'armut', 'üzüm', 'karpuz']
```sh
len(meyveler) # len listenin eleman sayısını verir.
```
4
```sh
sayi = [1,2,3,45,156,5342]
sayiveisim = ['ege', 42,'atalay',385]
print(sayi, sayiveisim)
```
[1, 2, 3, 45, 156, 5342] ['ege', 42, 'atalay', 385]

boş liste bu şekilde oluşturulur.
```sh
bos = []
bos
```
[]
```sh
ege = "Atalay"
yeni_liste = list(ege) # list komutu ile string ifadeleri listeye ekleyebiliriz.
yeni_liste
```
['A', 't', 'a', 'l', 'a', 'y']
```sh
yeni_liste[2]
```
'a'
```sh
yeni_liste[1]
```
't'
```sh
yeni_liste[-1]
```
'y'
```sh
yeni_liste[:2]
```
['A', 't']
```sh
yeni_liste[:4]
```
['A', 't', 'a', 'l']
```sh
yeni_liste[2:4]
```
['a', 'l']
```sh
yeni_liste[::-1] # bu komut listenin tersten yazılmasını sağlar.
```
['y', 'a', 'l', 'a', 't', 'A']

## Listeleri Birleştirme
```sh
ad = ["ege","onur"]
soyad = ["atalay", "kızılarslan"]
isim_listesi = ad + soyad
isim_listesi
```
['ege', 'onur', 'atalay', 'kızılarslan']
```sh
isim_listesi_2 = isim_listesi + ["Melih"] 
isim_listesi_2
```
['ege', 'onur', 'atalay', 'kızılarslan', 'Melih']
```sh
isim_listesi_2 * 2 # liste çarpılabilir ama bu çarpım değişkenin yeriin almaz
```
['ege',
 'onur',
 'atalay',
 'kızılarslan',
 'Melih',
 'ege',
 'onur',
 'atalay',
 'kızılarslan',
 'Melih']
 ```sh
isim_listesi_2
```
['ege', 'onur', 'atalay', 'kızılarslan', 'Melih']

## Append
**append** listeye yeni eleman eklemek için kullanılır.
```sh
isim_listesi_2.append("ATALAY")
isim_listesi_2
```
['ege', 'onur', 'atalay', 'kızılarslan', 'Melih', 'ATALAY']
## POP Metodu
**pop metodu** seçilen liste elemanını ekrana yazar ve o elemanı listeden siler.
```sh
pop_listesi = [1,2,3,4,5,6,7,8,9]
pop_listesi
[1, 2, 3, 4, 5, 6, 7, 8, 9]
pop_listesi.pop(8)
```
9
```sh
pop_listesi
```
[1, 2, 3, 4, 5, 6, 7, 8]
## sort Metodu
  **sort metodu** listedeki elemanları küçükten büyüğe doğru sıralar.
```sh
km = [351,548341,1585,38431,95964151,11541,81468454466]
km.sort()
km
```
[351, 1585, 11541, 38431, 548341, 95964151, 81468454466]
```sh
km.sort(reverse = True) # bu komut listeyi büyüken küçüğe sıralar.
km
```
[81468454466, 95964151, 548341, 38431, 11541, 1585, 351]
```sh
marka = ["opel","ford","bmw","mercedes","audi","fiat","dacia"]
marka.sort() # Küçükten büyüğe doğru sıralamada kullanıyoruz.
marka
```
```sh
['audi', 'bmw', 'dacia', 'fiat', 'ford', 'mercedes', 'opel']
marka.sort(reverse = True)
marka
```
['opel', 'mercedes', 'ford', 'fiat', 'dacia', 'bmw', 'audi']

## İç İçe Liste
```sh
ic_ice = [pop_listesi,km,marka]
ic_ice
```
[[1, 2, 3, 4, 5, 6, 8],
 [81468454466, 95964151, 548341, 38431, 11541, 1585, 351],
 ['opel', 'mercedes', 'ford', 'fiat', 'dacia', 'bmw', 'audi']]
