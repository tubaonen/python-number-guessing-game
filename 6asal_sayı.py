import math

def asal_kontrol_et(sayi):
    if sayi <= 1: return False
    if sayi == 2: return True
    if sayi % 2 == 0: return False
    sinir = int(math.sqrt(sayi)) + 1
    for i in range(3, sinir, 2):
        if sayi % i == 0: return False
    return True

# --- YENİ EKLEDİĞİMİZ ALGORİTMA FONKSİYONU ---
def asal_carpanlari_bul(sayi):
    carpanlar = []
    bolen = 2
    
    # Sayıyı tam bölünemeyene kadar en küçük asal sayıdan başlayarak bölüyoruz
    while sayi > 1:
        if sayi % bolen == 0:
            if bolen not in carpanlar:
                carpanlar.append(bolen) # Listeye ekle
            sayi = sayi // bolen # Sayıyı küçült
        else:
            bolen += 1 # Bölünmüyorsa bir sonraki sayıya geç
            
    return carpanlar

def programi_baslat():
    print("🔢 Gelişmiş Asal Sayı ve Çarpan Analizörü 🔢")
    
    while True:
        giris = input("\nSayı girin (Çıkış için 'q'): ")
        
        if giris.lower() == 'q':
            print("👋 İyi çalışmalar!")
            break
            
        if not giris.isdigit():
            print("❌ Geçersiz giriş!")
            continue
            
        sayi = int(giris)
        
        if asal_kontrol_et(sayi):
            print(f"✨ {sayi} bir ASAL sayıdır! 🏆")
        else:
            print(f"❌ {sayi} bir asal sayı değildir.")
            # Yeni fonksiyonumuzu çağırıp listeyi alıyoruz
            carpan_listesi = asal_carpanlari_bul(sayi)
            print(f"🧬 {sayi} sayısının asal çarpanları: {carpan_listesi}")

# Eylem düğmesi - Programı ateşleyen satır!
programi_baslat()