import time

istek = str(input("E/H\nMarket yazılımını çalıştırmak istiyor musunuz? "))
cizgi = "-" * 50
para = 200

stok = {
       'muz': 6,
       'elma': 0,
       'portakal': 32,
       'doritos': 15,
       'karpuz' : 12
        }
urunler = {
       'muz': 10,
       'elma': 10,
       'portakal': 15,
       'doritos': 5,
       'karpuz' : 20
        }


class market():
    cuzdan = para
    def urunal(urun):
        if urunsecim in urunler and stok[urunsecim] > 0:
            if para >= urunler[urunsecim]:
                cuzdan = para - urunler[urunsecim]
                print("Başarıyla", urunsecim, "Aldınız!\n Cüzdanınızda kalan para:", cuzdan,"\n Markette '" + urunsecim + "' adlı üründen", stok[urunsecim], "adet kaldı.")
                time.sleep(3)
            else:
                print("Maalesef paranız yetmiyor.")
                time.sleep(3)
        else:
            print("Hatalı bir ürün girdiniz ya da ürün stoğumuzda kalmadı.")
            time.sleep(3)
            return urunsecim

    def stokekle(urun):
        if urunsecim in stok and stok[urunsecim] >= 150:
            print("Bu ürün stok sınırını aştı. Lütfen daha sonra tekrar deneyiniz.")
            time.sleep(3)
            return
        else:
            kactane = int(input("Stoğa kaç adet ürün eklenecek: "))
            if kactane + stok[urunsecim] > 150:
                print("Bu kadar ürün eklerseniz depomuz dolar. Lütfen daha az bir sayı ile tekrar deneyiniz.")
                time.sleep(3)
                return kactane
            else:
                stok[urunsecim] += kactane
                print(f"Ürünler başarıyla eklendi. Yeni stok sayısı {stok[urunsecim]}")
    def fiyatlarveurunler():
        for gosterilecekler in urunler:
            print(f"{gosterilecekler.upper()}\nFiyat: {urunler[gosterilecekler]}\nStok: {stok[gosterilecekler]}\nYanınızdaki mevcut para: {para}\n", cizgi)
            time.sleep(3)

while istek.lower() == "e":

    menu = str(input(cizgi + """\nZMarket'e Hoş Geldiniz!\nLütfen yapmak istediğiniz işlemi seçiniz.\nİşlemler\n1 - Ürün Al\n2 - Stok Ekle\n3 - Fiyatlar/Ürünler\n İşleminiz: """))
    if menu.lower() == "1":
        urunsecim = str(input(cizgi + "\nÜrün seçiniz: "))
        urunsecim = urunsecim.lower()
        market.urunal(urunsecim)
    elif menu.lower() == "2":
        urunsecim = str(input(cizgi + "\nÜrün seçiniz: "))
        market.stokekle(urunsecim)
    elif menu.lower() == "3":
        market.fiyatlarveurunler()
    else:
        print("Hatalı veya sistemde olmayan bir işlem seçtiniz. Lütfen tekrar deneyiniz.")


print("Script Kapatılıyor.")

#elimizde_yok = ["Maalesef bu ürün elimizde bulunmamaktadır.", "İstediğiniz ürün stoğumuzda kalmadı"]
#paraniz_yetmiyor = ["Maalesef bu ürüne paranız yetmiyor.", "Bu ürünü almak için yeterli paranız bulunmamakta.", "Bu ürünü almak için", para - urunler[urunsecim], "liranız eksik."]
