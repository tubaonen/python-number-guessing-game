import random

def oyun_baslat():
    print("🎲 Gelişmiş Sayı Tahmin Oyununa Hoş Geldiniz! 🎲")
    
    en_yuksek_skor = None  # En iyi skoru tutmak için değişken

    while True:
        gizli_sayi = random.randint(1, 50)
        hak = 5
        toplam_tahmin = 0
        
        print("\n1 ile 50 arasında bir sayı tuttum. Bakalım bulabilecek misin?")
        # print(f"(Hile Ekranı - Bilgisayarın tuttuğu sayı: {gizli_sayi})") # Test için açabilirsin

        while hak > 0:
            print("-" * 40)
            print(f"Kalan Tahmin Hakkınız: {hak}")
            
            # Girdinin sayı olup olmadığını kontrol eden güvenli bölge
            tahmin_girisi = input("Tahmininiz nedir?: ")
            if not tahmin_girisi.isdigit():
                print("❌ Lütfen sadece tam sayı giriniz!")
                continue
                
            tahmin = int(tahmin_girisi)
            
            if tahmin < 1 or tahmin > 50:
                print("⚠️ Lütfen 1 ile 50 arasında bir sayı giriniz!")
                continue
            
            # Geçerli bir tahmin yapıldıysa hak düşür ve hamleyi say
            hak -= 1
            toplam_tahmin += 1

            if tahmin == gizli_sayi:
                print(f"🎉 TEBRİKLER! Sayıyı {toplam_tahmin}. denemede doğru bildiniz! 🥳")
                
                # En yüksek skor kontrolü (Daha az deneme = daha iyi skor)
                if en_yuksek_skor is None or toplam_tahmin < en_yuksek_skor:
                    en_yuksek_skor = toplam_tahmin
                    print(f"🏆 YENİ REKOR! En iyi skorunuz: {en_yuksek_skor} deneme.")
                else:
                    print(f"📊 Mevcut rekorunuz: {en_yuksek_skor} deneme.")
                break
            elif tahmin < gizli_sayi:
                print("📈 Daha BÜYÜK bir sayı giriniz. (Yukarı! ⬆️)")
            else:
                print("📉 Daha KÜÇÜK bir sayı giriniz. (Aşağı! ⬇️)")

        if hak == 0 and tahmin != gizli_sayi:
            print("-" * 40)
            print(f"🔴 Haklarınız bitti! Maalesef kaybettiniz. Tuttuğum sayı: {gizli_sayi}")

        # Tekrar oynama sorgusu
        tekrar = input("\nTekrar oynamak ister misiniz? (E / H): ").upper()
        if tekrar != "E":
            print("👋 Oyundan çıkılıyor. Tekrar görüşmek üzere!")
            break

# Oyunu çalıştır
oyun_baslat()