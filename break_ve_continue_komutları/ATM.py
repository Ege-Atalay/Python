"""
bu örnekTE BİR ATM yapacağız.
bu ATM girilen her sayıyı toplar. (0 sayısı girilirse toplamayı bırakır ve sonraki işleme geçer. )
bunlarla üç farklı işlem yapılır:
para yükleme
para çekme
ne kadar para olduğuna bakma
ve her işlmeden sonra çıkış yapılıp yapılmaması gerektiğini kullanıcıya sorun.
"""





bakiye = 0
deger = 0
while deger == 0:
    eleman = float(input('Bir para girin (çıkmak için "0" girin): '))
    if eleman == 0:
        deger = 1
    bakiye += eleman

print("""
***************
bakiyenizi görmek için biri,
para yatırmak için ikiyi,
para çekmek için için üçü tuşlayınız.
***************
""") 
while(True):
    islem = input('bir işlem giriniz\nEğer işiniz bitti ise "x" tuşu ile çıkabilirsiniz\n')
    if islem.upper() == "X":
        print ("yine bekleriz...")
        break
    elif islem == "1":
        print("kalan bakiyeniz {} tl'dir".format(bakiye))
    elif islem == "2":
        Ymiktar = float(input("yatırmak istediğiniz miktarı giriniz:\n"))
        bakiye += Ymiktar
        print("artık mevcut bakiyeniz {} tl para yatırılması ile {} tl'ye çıkmıştır".format(Ymiktar,bakiye))
    elif islem == "3":
        Cmiktar = float(input("çekmek istediğiniz miktarı seçin:\n"))
        if Cmiktar > bakiye:
            print("bankada bu kadar paranız yok.")
            continue
        else:
            bakiye -= Cmiktar
            print("başarılı\nbakiyenizden {} tl çekilmiştir kalan bakiyeniz{} tl'dir".format(Cmiktar,bakiye))
    else:
        print("böyle bir işlem bulunmamaktadır.")
    
