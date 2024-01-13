
# Amadeus Travel to Future programı için Case & Study

Amadeus tarafından belirtilmiş web adreslerinin Back tarafında API'
ın çalışma testlerinin yapılması ve Front tarafında mantıksal çelişkileri tespit etme testlerinin yapılmasını sağlayan çalışmadır.

**Backend Testleri**

- HTTP durum kodlarının (status code) kontrolü,
- GET isteğine gelen cevabın içeriğindeki verinin yapısının ve içeriğinin kontrolü
- GET isteğine gelen cevabın içerik tipi başlığının (content-type header) kontrolü

**Frontend Testleri**

- Uçuş listeleme için kalkış ve iniş yerleri seçilen kutucukların seçim kontrolü
- Kalkış ve iniş kutucuklarını seçtikten sonra listelenen uçuşların sayısının kontrolü 
## İndirme ve Kullanım Yönergeleri



Projeyi klonlayın

```bash
  git clone https://github.com/lntreter/Case-Study.git
```

**Backend**

Proje dizinine gidin ve gerekli paketleri yükleyin

```bash
  cd Case-Study/back
  npm install
```

Testleri çalıştırın

```bash
  npm test
```

https://flights-api.buraky.workers.dev/ adresindeki backend testlerini otomatik kontrol eder


**Frontend**

Proje dizinine gidin ve gerekli paketleri yükleyin

```bash
  cd Case-Study/front
```

Proje gereksinimlerini indirin ve çalıştırın

```bash
  pip install selenium
  python fronttest.py  // ya da hangi python aliasını kullanıyorsanız
```

Ya da bir python sanal ortamı oluşturun ve gereksinimleri sanal ortma indirip çalıştırın

- Windows için

```bash
  python -m venv ortam_adi
  ortam_adi\Scripts\activate
  pip install selenium
  python fronttest.py
```
- Mac & Linux için

```bash
  python -m venv ortam_adi
  source ortam_adi/bin/activate
  pip install selenium
  python fronttest.py
```
Çalıştığında otomatik olarak https://flights-app.pages.dev/ adresinde test yapmaya başlar. (Varsayılan olarak Firefox tarayıcısını kullanır ve çalışırken biraz bekletebilir)

**NOT**

Kontrol edenler için frontend kontrollerinde iki testi de kullandım biri uzun yoldan biri kısa yoldan.



  
