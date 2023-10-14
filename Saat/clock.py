import datetime

# Şu anki tarih ve saat bilgisini al
now = datetime.datetime.now()

# Azerbaycan saat dilimini ayarla (UTC+4)
azerbaijan_time = now + datetime.timedelta(hours=0)

# Tarihi ve saati yazdır
print("Azerbaycan'da şu anki saat:", azerbaijan_time)
