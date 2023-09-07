import os
import shutil

# Klasör yolunu belirtin
klasor_yolu = "C:\\Users\\hakso\\Downloads"

# Klasördeki dosyaları listeleyin
dosyalar = os.listdir(klasor_yolu)

# "spotifydown.com - " yazısını silip dosya adını değiştirin ve yeni klasöre kaydedin
for dosya in dosyalar:
    eski_yol = os.path.join(klasor_yolu, dosya)
    
    # Dosyanın adındaki "spotifydown.com - " kısmını silin
    yeni_dosya_adı = dosya.replace("spotifydown.com - ", "")
    
    yeni_yol = os.path.join('C:\\Users\\hakso\\Downloads', yeni_dosya_adı)
    
    # Dosyayı yeni klasöre taşıyın
    shutil.move(eski_yol, yeni_yol)