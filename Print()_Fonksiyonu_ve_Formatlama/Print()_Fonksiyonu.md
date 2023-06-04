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

print('Merhaba Dünya')
Merhaba Dünya
print('''Merhaba Dünya''')
Merhaba Dünya
print(5) # Buradaki ifade int bir ifadedir.
5
print("5") # Buradaki ifade ise string bir ifadedir.
5
a = 5
b = 9
print (a+b)
14
x = 15
y = 19
print ("a+b")
a+b
print('Ege Atalay'ın Katıldığı Eğitim Python.)
  File "C:\Users\onurk\AppData\Local\Temp\ipykernel_19204\883528299.py", line 1
    print('Ege Atalay'ın Katıldığı Eğitim Python.)
                      ^
SyntaxError: invalid syntax
print("Ege Atalay'ın Katıldığı Eğitim Python.")
Ege Atalay'ın Katıldığı Eğitim Python.
print("Ege", 12,45,3.14)
Ege 12 45 3.14
print("Melih","Ege","Onur")
Melih Ege Onur
print("elma,armut,karpuz")
elma,armut,karpuz
print("elma","armut","karpuz")
elma armut karpuz
\n ifadesi
print() fonksiyonu içerisindeki yazıları alt satırlara yazar.

print("elma\narmut\nkarpuz")
elma
armut
karpuz
print("elma\n","armut\n","karpuz\n")
elma
 armut
 karpuz

\t ifadesi
print() ifadesi içerisinde kullanılan karakterler arasında bir rab boşluk bırakır.

print("elma\tarmut\tkarpuz")
elma	armut	karpuz
print("elma\t\tarmut\t\tkarpuz")
elma		armut		karpuz
type() fonksiyonu
Kullanılan veri tipinin değerini bize verir

type (5)
int
type(34.233)
float
type(ege)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
~\AppData\Local\Temp\ipykernel_19204\1904048625.py in <module>
----> 1 type(ege)

NameError: name 'ege' is not defined
type("ege")
str
sep Parametresi
print(5,3,63,45,263,74)
5 3 63 45 263 74
print(5,3,63,45,263,74,sep = ".")
5.3.63.45.263.74
print(5,3,63,45,263,74,sep = "*")
5*3*63*45*263*74
print(5,3,63,45,263,74,sep = "/")
5/3/63/45/263/74
print("elma","armut","karpuz", sep = "/" )
elma/armut/karpuz
print("elma","armut","karpuz", sep = "\n")
elma
armut
karpuz
Yıldız Fonksiyonu
print("Ege Atalay")
Ege Atalay
print(*"Ege Atalay")
E g e   A t a l a y
print(*"Ege Atalay", sep="\n")
E
g
e
 
A
t
a
l
a
y
print("TRT", sep=".")
TRT
