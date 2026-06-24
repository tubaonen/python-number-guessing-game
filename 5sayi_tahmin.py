import random

print("🎲 Sayı Tahmin Oyununa Hoş Geldiniz! 🎲")
print("1 ile 50 arasında bir sayı tuttum. Tahmin edebilecek misin?")

gizli_sayi = random.randint(1, 50)
print(f"(Hile Ekranı - Bilgisayarın tuttuğu sayı: {gizli_sayi})")

hak = 5

while hak > 0:
    print("---------------------------------")
    print(f"Kalan Tahmin Hakkınız: {hak}")
    
    tahmin = int(input("Tahmininiz nedir?: "))
    hak = hak - 1
    
    if tahmin == gizli_sayi:
        print(f"🎉 TEBRİKLER! Sayıyı doğru bildiniz! 🎉")
        break
    elif tahmin < gizli_sayi:
        print("📈 Daha BÜYÜK bir sayı giriniz. (Yukarı!)")
    else:
        print("📉 Daha KÜÇÜK bir sayı giriniz. (Aşağı!)")
    
if hak == 0 and tahmin != gizli_sayi:
    print("---------------------------------")
    print(f"🛑 Haklarınız bitti! Maalesef kaybettiniz. Tuttuğum sayı: {gizli_sayi}")