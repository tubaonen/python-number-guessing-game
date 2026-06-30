def alışveriş_liste_uygulamasi():
    # Yapı: [["Elma", 2, "Kg", 40.0, False]] -> Son eleman alındı mı kontrolü (False = Alınmadı)
    alisveris_listesi = []
    
    print("🛒 Alışveriş ve Bütçe Takip Uygulamasına Hoş Geldiniz! 🛒")
    
    while True:
        print("\n" + "="*45)
        print("1. Listeyi Görüntüle (Bütçe Dahil)")
        print("2. Ürün Ekle / Güncelle")
        print("3. Ürünü 'Alındı' Olarak İşaretle")
        print("4. Ürün Sil")
        print("5. Çıkış Yap")
        print("="*45)
        
        secim = input("Yapmak istediğiniz işlemin numarasını girin: ")
        
        if secim == "1":
            if len(alisveris_listesi) == 0:
                print("ℹ️ Listeniz şu an bomboş.")
            else:
                print("\n📋 GÜNCEL ALIŞVERİŞ LİSTENİZ:")
                print("-" * 55)
                toplam_butce = 0.0
                
                for sira, paket in enumerate(alisveris_listesi, 1):
                    # Durum simgesi belirleme
                    durum = "✅ [ALINDI]" if paket[4] else "❌ [BEKLİYOR]"
                    urun_toplam = paket[1] * paket[3]
                    toplam_butce += urun_toplam
                    
                    print(f"{sira}. {paket[0]} ({paket[1]} {paket[2]}) - Birim Fiyat: {paket[3]} TL -> Toplam: {urun_toplam} TL | {durum}")
                
                print("-" * 55)
                print(f"💰 Tahmini Toplam Alışveriş Tutarı: {toplam_butce} TL")
                    
        elif secim == "2":
            yeni_urun = input("Ürün adını yazın: ").capitalize()
            
            # Miktar kontrolü
            miktar_girisi = input(f"Kaç tane/kg {yeni_urun} alınacak?: ")
            if not miktar_girisi.isdigit():
                print("❌ Hata: Miktar sadece tam sayı olmalıdır!")
                continue
            miktar = int(miktar_girisi)
            
            # Birim seçimi
            print("\nBirim: 1-Adet | 2-Kg | 3-Paket")
            b_secim = input("Seçiminiz: ")
            birim = "Adet" if b_secim == "1" else "Kg" if b_secim == "2" else "Paket" if b_secim == "3" else "Birim"
            
            # Fiyat kontrolü
            fiyat_girisi = input(f"1 {birim} {yeni_urun} tahmini kaç TL?: ")
            try:
                fiyat = float(fiyat_girisi)
            except ValueError:
                print("❌ Hata: Fiyat sadece sayısal değer olmalıdır!")
                continue
            
            # Aynı ürün ve aynı birim var mı kontrolü
            bulundu = False
            for paket in alisveris_listesi:
                if paket[0] == yeni_urun and paket[2] == birim:
                    paket[1] += miktar
                    paket[3] = fiyat # En son girilen fiyatı günceller
                    print(f"🔄 Miktar ve fiyat güncellendi! Yeni: {paket[1]} {birim}")
                    bulundu = True
                    break
            
            if not bulundu:
                # [İsim, Miktar, Birim, Fiyat, Alındı Mı]
                alisveris_listesi.append([yeni_urun, miktar, birim, fiyat, False])
                print(f"✅ {yeni_urun} listeye eklendi.")
                
        elif secim == "3":
            if len(alisveris_listesi) == 0:
                print("❌ Listeniz boş.")
            else:
                urun_adi = input("Alındı olarak işaretlemek istediğiniz ürünün adı: ").capitalize()
                bulundu = False
                for paket in alisveris_listesi:
                    if paket[0] == urun_adi:
                        paket[4] = True # Durumu True (Alındı) yapıyoruz
                        print(f"🎉 {urun_adi} başarıyla 'ALINDI' olarak işaretlendi!")
                        bulundu = True
                        break
                if not bulundu:
                    print("❌ Ürün listede bulunamadı.")
                    
        elif secim == "4":
            if len(alisveris_listesi) == 0:
                print("❌ Listenizde silinecek ürün yok.")
            else:
                silinecek = input("Silmek istediğiniz ürünün adını yazın: ").capitalize()
                bulundu = False
                for paket in alisveris_listesi:
                    if paket[0] == silinecek:
                        alisveris_listesi.remove(paket)
                        print(f"🗑️ {silinecek} listeden kaldırıldı.")
                        bulundu = True
                        break
                if not bulundu:
                    print("❌ Ürün bulunamadı!")
                    
        elif secim == "5":
            print("👋 Çıkış yapılıyor. İyi alışverişler!")
            break
        else:
            print("❌ Geçersiz seçim!")

alışveriş_liste_uygulamasi()