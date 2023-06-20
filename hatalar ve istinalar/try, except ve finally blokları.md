# hatalar ve istisnalar(try-except bloğu)
try: 
  
  Hataya sebep olabilecek kodlar buraya yazılır

except HataAdi:


```sh
try:
    a = 15;
    b = 0;

    c = a/b;
    
except ZeroDivisionError:
    print("Hata Kodu: ZeroDivisionError - Hiçbir sayı 0 ile bölünemez. Lütfen sayıyı kontrol ediniz..!")

except NameError:
    print("Hata Kodu: NameError - Girilen Değer Sayı Değil. Lütfen bir sayı giriniz..!")
```

Hata Kodu: ZeroDivisionError - Hiçbir sayı 0 ile bölünemez. Lütfen sayıyı kontrol ediniz..!

```sh
try:
    sayi = int(input("Bir Sayı Giriniz: "))

except ValueError:    
    print("Geçerli Bir Değer Girilmedi..!")
    
else:
    print("Girilen Değer: " ,sayi)
    
finally:
    print("Bilgi verildi...")
```

Bir Sayı Giriniz: abc

Geçerli Bir Değer Girilmedi..!

Bilgi verildi...
## raise - Hata Fırlatma
**raise HataAdı(hata mesajı)**

```sh
def ters(metin):
    if(type(metin) != str):
        raise ValueError("Lütfen Yazı Giriniz..!")
    else:
        return metin[::-1]
print(ters("ATALAY"))
```

YALATA

``` sh
print(ters("2154")) #tırnak işareti olduğu için hata vermez
```

4512

```sh
print(ters(2154)
```

---------------------------------------------------------------------------

ValueError                                Traceback (most recent call last)

~\AppData\Local\Temp\ipykernel_11160\3725191688.py in <module>
  
----> 1 print(ters(2154))
  
~\AppData\Local\Temp\ipykernel_11160\1635460536.py in ters(metin)
  
1 def ters(metin):
  
2     if(type(metin) != str):
  
----> 3         raise ValueError("Lütfen Yazı Giriniz..!")
  
4     else:
  
5         return metin[::-1]
  
ValueError: Lütfen Yazı Giriniz..!
  
