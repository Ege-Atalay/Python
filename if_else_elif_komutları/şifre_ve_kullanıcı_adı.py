"""
bir internet giriş sitesi yapın :
önce bir şifre ve kullanıcı adı isteyin.
sonra bu kulnıcı adı ve şifreyi doğrulayın.
eğer 3 defa yanlış yazarsa programdan atın.

"""

#lütfen önce kendiniz yapın

kadi = "ege"
sifre= "atalay"

deneme = 3

while True:
    ad_girisi = input("Lütfen Sisteme Kayıtlı Kullanıcı Adınızı Giriniz: ")
    sifre_girisi = input("Lütfen Sisteme Kayıtlı Şifrenizi Giriniz: ")
    
    if (ad_girisi != kadi and sifre_girisi != sifre):
        print("Sisteme Kayıtlı Kullanıcı Adı ve Parola Hatalıdır..!")
        deneme -= 1

    elif (ad_girisi != kadi and sifre_girisi == sifre):
        print("Sisteme Kayıtlı Kullanıcı Adı ve Parola Hatalıdır..!")
        deneme -= 1    
        
    elif (ad_girisi == kadi and sifre_girisi != sifre):
        print("Sisteme Kayıtlı Kullanıcı Adı ve Parola Hatalıdır..!")
        deneme -= 1 
        
    else:
        print("Sisteme Hoşgeldiniz..!")
        break
        
    if (deneme == 0):
        print("Kullanıcı Adınız Bloke Olmuştur. Lütfen Sistem Yöneticiniz ile Görüşünüz..!")
        break
