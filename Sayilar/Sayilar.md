# SAYILAR
Bu bölümde aşağıdaki dersleri işleyeceğiz.

Tamsayılar
Ondalıklı Sayılar
Basit Matematiksel İşlemler
Değişkenler
Tamsayılar ( Integer )
Matematik desinden hatırladığımız tamsayılar bu bölümde de aynı şekilde işlenmektedir. Python yazılım dilinde tamsayılar "Integer" olarak adlandırılmaktadır. Tamsayılara örnek olarak;

1)1

2)235

3)-520

4)-12500

5)354

Ondalıklı Sayılar ( Float )
Matematik dersinden bildiğimiz ondalıklı sayılar konusu ile aynıdır. Python yazılım dilinde ondalıklı sayılar "float" olarak adlandırılmaktadır.

Basit Matematiksel İşlemler
## Toplama
```sh
2+2
```
4

## Çıkarma
```sh
19 - 7
```
12
## Bölme
```sh
15 / 5
```s
3.0
## Çarpma
```sh
16 * 2
```
32
# Değişkenler
## Değişkenimizin adı = Değişkenin değeri
```sh
i = 20
i
```
20
```sh
i * 2
```
40
```sh
i / 4
```
5.0
```sh
i * i
```
400
```sh
i = 10
i
```
10
```sh
i * 5
```
50
```sh
a = 10
b = 4
c = a + b
a
```
10
```sh
b
```
4
```sh
c
```
14

## Değişken Tanımlama Kuralları
1) Değişken isimleri bir sayı ile başlayamaz.
```sh
5a = 15
```
  File "C:\Users\onurk\AppData\Local\Temp\ipykernel_7488\840921684.py", line 1
    5a = 15
     ^
SyntaxError: invalid syntax

Değişken isimleri verilirken birden fazla kelime var ise boşluk bırakılmaz.
```sh
tam sayi = 5
```
  File "C:\Users\onurk\AppData\Local\Temp\ipykernel_7488\140381501.py", line 1
    tam sayi = 5
        ^
SyntaxError: invalid syntax

Özel karakterler ( !'^+%&/()=?- ) kullanılamaz. Ancak alt tire _ kullanılabilir.

```sh
&a = 5
```
  File "C:\Users\onurk\AppData\Local\Temp\ipykernel_7488\2437011851.py", line 1
    &a = 5
    ^
SyntaxError: invalid syntax
```sh
tam_sayi = 5
tam_sayi
```
5
Python yazılım dilinin kullandığı özel ifadeleri değişken adı olarak kullanamayız. Ör; while, not, if, else vb.
```sh
if = 5
```
  File "C:\Users\onurk\AppData\Local\Temp\ipykernel_7488\2630263448.py", line 1
    if = 5
       ^
SyntaxError: invalid syntax
```sh
a = 3
b = 5
a,b = b,a
a
```
5
```sh
b
```
3
```sh
a = a+1
a
```
6
```sh
a += 1
a
```
7
```sh
a += 2
a
```
9
```sh
a += 5
a
```
14
```sh
b = b-1
b
```
2
```sh
b -= 2
b
```
0
```sh
a *= 10
a
```
140
```sh
a *= 10 # Sayımızı hızlı bir şekilde çarpıp o değeri atamak için kullandığımız bir ifadedir. 
"""
Çoklu yorum satılarında
3 adet tırnak işareti 
kullanmamız gerekiyor.
Bu şekilde paragraf
yazılarını yazabilirsiniz.
"""
'\nÇoklu yorum satılarında\n3 adet tırnak işareti \nkullanmamız gerekiyor.\nBu şekilde paragraf\nyazılarını yazabilirsiniz.\n'
"""
Çoklu yorum satılarında
3 adet tırnak işareti 
kullanmamız gerekiyor.
Bu şekilde paragraf
yazılarını yazabilirsiniz.
"""
a
```
1400
 
