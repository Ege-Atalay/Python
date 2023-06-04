# break
**break** komutu belli bir koşul sağlandığında döngüyü kırmak için kullanılır.
```sh
i = 0

while (i < 10):
    print(i)
    if (i == 4):
        break
    i += 1
```
1

2

3

4

```sh
while True:
    tc_no = input("Lütfen TC Numaranızı Giriniz (Çıkış Yapmak İçin 0 Tuşuna Basınız.!):")
    if(tc_no == "0"):
        print("Sistem Sonlandırılıyor..!")
        break
    print(tc_no)
```
Lütfen TC Numaranızı Giriniz (Çıkış Yapmak İçin 0 Tuşuna Basınız.!):55

Lütfen TC Numaranızı Giriniz (Çıkış Yapmak İçin 0 Tuşuna Basınız.!):45

Lütfen TC Numaranızı Giriniz (Çıkış Yapmak İçin 0 Tuşuna Basınız.!):60

Lütfen TC Numaranızı Giriniz (Çıkış Yapmak İçin 0 Tuşuna Basınız.!):40

Lütfen TC Numaranızı Giriniz (Çıkış Yapmak İçin 0 Tuşuna Basınız.!):46

Lütfen TC Numaranızı Giriniz (Çıkış Yapmak İçin 0 Tuşuna Basınız.!):1

Lütfen TC Numaranızı Giriniz (Çıkış Yapmak İçin 0 Tuşuna Basınız.!):0

55456040461
