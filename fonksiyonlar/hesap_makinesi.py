def toplama(x, y):
    return x + y

def cikarma(x, y):
    return x - y

def carpma(x, y):
    return x * y

def bolme(x, y):
    if y != 0:
        return x / y
    else:
        return "Geçersiz işlem: Sıfıra bölme hatası!"

print("Hesap Makinesi")
print("İşlemler:")
print("1. Toplama")
print("2. Çıkarma")
print("3. Çarpma")
print("4. Bölme")

while True:
    secim = input("Bir işlem seçin (1/2/3/4): ")

    if secim in ['1', '2', '3', '4']:
        num1 = float(input("Birinci sayıyı girin: "))
        num2 = float(input("İkinci sayıyı girin: "))

        if secim == '1':
            print("Sonuç:", toplama(num1, num2))
        elif secim == '2':
            print("Sonuç:", cikarma(num1, num2))
        elif secim == '3':
            print("Sonuç:", carpma(num1, num2))
        elif secim == '4':
            print("Sonuç:", bolme(num1, num2))
        
        devam = input("Devam etmek istiyor musunuz? (E/H): ")
        if devam.upper() == 'H':
            break
    else:
        print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")
