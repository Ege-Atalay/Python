# Print() Fonksiyonu
**Kodlarımızı ekrana yazdırmak için print() şeklinde ifade ile çalışıyoruz.**
```sh
print("Merhaba Dünya")
```
Merhaba Dünya
```sh
print(Merhaba Dünya)
```
File "C:\Users\onurk\AppData\Local\Temp\ipykernel_19204\997940271.py", line 1

print(Merhaba Dünya)

                   ^
                   
SyntaxError: invalid syntax
```sh
print('Merhaba Dünya')
```
Merhaba Dünya
```sh
print('''Merhaba Dünya''')
```
Merhaba Dünya
```sh
print(5) # Buradaki ifade int bir ifadedir.
```
5
```sh
print("5") # Buradaki ifade ise string bir ifadedir.
```
5
```sh
a = 5
b = 9
print (a+b)
```
14
```sh
x = 15
y = 19
print ("a+b")
```
a+b
```sh
print('Ege Atalay'ın Katıldığı Eğitim Python.)
```
File "C:\Users\onurk\AppData\Local\Temp\ipykernel_19204\883528299.py", line 1
    print('Ege Atalay'ın Katıldığı Eğitim Python.)
                      ^
SyntaxError: invalid syntax
```sh
print("Ege Atalay'ın Katıldığı Eğitim Python.")
```
Ege Atalay'ın Katıldığı Eğitim Python.
```sh
print("Ege", 12,45,3.14)
```
Ege 12 45 3.14
```sh
print("Melih","Ege","Onur")
```
Melih Ege Onur
```sh
print("elma,armut,karpuz")
```
elma,armut,karpuz
```sh
print("elma","armut","karpuz")
```
elma armut karpuz
## \n ifadesi
**print() fonksiyonu içerisindeki yazıları alt satırlara yazar.**
```sh
print("elma\narmut\nkarpuz")
```
elma

armut

karpuz
```sh
print("elma\n","armut\n","karpuz\n")
```
elma

armut

karpuz


## \t ifadesi
**print() ifadesi içerisinde kullanılan karakterler arasında bir tab boşluk bırakır.**
```sh
print("elma\tarmut\tkarpuz")
```
elma    armut    karpuz
```sh
print("elma\t\tarmut\t\tkarpuz")
```
elma		  armut		  karpuz
## type() fonksiyonu
**Kullanılan veri tipinin değerini bize verir**
```sh
type (5)
```
int
```sh
type(34.233)
```
float
```sh
type(ege)
```
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
~\AppData\Local\Temp\ipykernel_19204\1904048625.py in <module>
----> 1 type(ege)

NameError: name 'ege' is not defined
```sh
type("ege")
```
str
  
## sep Parametresi
```sh
print(5,3,63,45,263,74)
```
5 3 63 45 263 74
```sh
print(5,3,63,45,263,74,sep = ".")
```
5.3.63.45.263.74
```sh
print(5,3,63,45,263,74,sep = "*")
```
5 * 3 * 63 * 45 * 263 * 74
```sh
print(5,3,63,45,263,74,sep = "/")
```
5/3/63/45/263/74
```sh
print("elma","armut","karpuz", sep = "/" )
```
elma/armut/karpuz
```sh
print("elma","armut","karpuz", sep = "\n")
```
elma

armut

karpuz
## Yıldız Fonksiyonu
```sh
print("Ege Atalay")
```
Ege Atalay
```sh
print(*"Ege Atalay")
```
E g e   A t a l a y
```sh
print(*"Ege Atalay", sep="\n")
```
E

g

e


A

t

a

l

a

y
  
```sh
print("TRT", sep=".")
```
TRT
