# Sonradan-Gurme
mat132 proje ödevi

# 📌 sonradan gurme

sonradan gurme, kullanıcıların restoranlar hakkında yorum yapabileceği, gurmelerin önerilerini paylaşabileceği ve en iyi yemeklerin keşfedilebileceği bir platformdur. kullanıcılar restoranları değerlendirebilir, takip edebilir ve detaylı yorumlar yazabilir. 

## proje özellikleri
- **ana sayfa**: restoranları keşfetme ve öneriler alma.
- **authentication sistemi**: kullanıcı kayıt, giriş, şifremi unuttum ve sosyal medya ile giriş.
- **kullanıcı rolleri**: normal kullanıcı, gurme ve moderatör.
- **restoran yönetimi**: restoran ekleme, düzenleme ve google maps entegrasyonu.
- **yorum ve puanlama**: kullanıcıların restoranlara yorum ve puan bırakması.
- **ne, nerede yenir?**: en iyi yemeklerin önerildiği özel bir sekme.
- **moderasyon ve güvenlik**: küfür içeren yorumların filtrelenmesi, moderatör onay sistemi.

## proje yapısı
```
sonradan-gurme/
│── snrdngrm/        # django ana proje dizini
│── sgapp/           # ana uygulama
│── users/           # kullanıcı yönetimi uygulaması
│── templates/       # html şablonları
│── static/          # css, js, medya dosyaları
│── db.sqlite3       # veritabanı dosyası (geliştirme aşamasında)
│── manage.py        # django yönetim komut dosyası
│── requirements.txt # bağımlılıklar
│── readme.md        # proje açıklamaları
```

## yol haritası
- [ ] authentication (kayıt, giriş, şifre sıfırlama)
- [ ] kullanıcı rolleri (normal, gurme, moderatör)
- [ ] restoran yönetimi (moderasyon kontrolü)
- [ ] yorum ve puanlama sistemi
- [ ] ne, nerede yenir? sayfasının tamamlanması
- [ ] frontend geliştirmeleri (css, javascript)

## katkıda bulunma
projeye katkıda bulunmak isterseniz:
1. **fork** yapın
2. kendi dalınızı (branch) oluşturun: `git checkout -b yeni-ozellik`
3. değişikliklerinizi işleyin: `git commit -m 'yeni özellik eklendi'`
4. değişiklikleri gönderin: `git push origin yeni-ozellik`
5. bir **pull request (pr)** açın!

## lisans
mit lisansı altında yayımlanmıştır.
