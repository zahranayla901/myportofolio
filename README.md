| Nama | NPM | Kelas |
| :--- | :---: | ---: |
| Zahra Nayla Azfa | 2506534163 | PBP-E |

### Tugas 1
1. Dalam pengerjaan tugas individu 1 ini, saya menggunakan elemen semantik HTML5 berupa section. penggunaan section sangat membantu dalam organize my program. batasan section memperjelas fungsi bagian program tersebut, misalnya kayak misahin part profile dengan part experiences.

2. Kendala yang ditemui ada pada ukuran font h1 dan foto avatar. font h1 terlalu besar. Hal ini tidak masalah di desktop, tapi begitu pindah ke mobile, user hanya disambut h1 itu tadi sebagai first impression. Menurut saya hal ini harus ditangani, karena ketika membuka suatu situs, jika dalam sekali lihat user tidak langsung tahu garis besar isi artikelnya, mereka malas scroll kebawah. Untuk menangi hal ini, saya memperkecil ukuran font dan membaginya menjadi 2 line. jadi mau di desktop atau di mobile, tidak kelihatan terlalu penuh. 
Untuk foto avatar sendiri, saya hanya mengubah yang selalu rata kiri menjadi auto center ketika dalam bentuk mobile untuk memberikan balance.

3. Karena pertama kali juga membuat web dan memakai html css, saya cukup kesulitan ketika harus mengedit isi webnya secara manual per line. sebelumnya, saya sempat design lewat figma dulu, tapi ternyata realisasi dalam code programnya cukup sulit tidak seperti ekspektasi. lalu ngecek apakah posisi dan hasil yang diinginkan juga harus runserver berulang. belum lagi jika ada kesalahan ukuran yang kurang pas. 
Untuk pengembangan selanjutnya, saya ingin coba mengadakan fitur message yang dihubungkan dengan django form & database agar bisa tersimpan otomatis di email. Selain itu, fitur message juga mempermudah user reach-out tanpa perlu membuka aplikasi lain seperti social media.

AI Disclosure: Dalam pengerjaan proyek tugas individu 1, saya menggunakan bantuan AI berupa Claude Sonnet 5 version. Mempertimbangkan pengalaman pertama menyentuh html dan css, saya meminta ai me-breakdown fungsi dari tiap raw code untuk saya kembangkan kedepannya. Claude memberikan penjelasan interaksi anatar css dengan html, struktur halaman (header, main, footer), convert font dan ukuran rem px, dan table struktur beserta outputnya. selain itu saya juga memakai AI untuk debugging git dan pws karena ada kendala file git dan lokal yang tidak sinkron terupdate. 

### Tugas 2
1. User mengirim permintaan http get dengan mengakses alamat url --> urls.py proyek mencocokkan permintaan lalu mengarahkan ke urls.py aplikasi --> urls.py aplikasi mengarahkan sub-path spesifik ke view class untuk halaman tersebut --> view nerima permintaan, manggil data dari model, dan memasukkannya dalam context --> model ngambil data yang diminta dari database dengan Django ORM lalu ngembaliin ke view --> view ngirimin context ke file template lalu template merender tag dinamis jadi struktur HTML statis --> view ngembaliin hasil akhir file HTML ke browser User.

2. Data disimpan dalam model untuk menerapkan prinsip Separation of Concerns. Sebelumnya pengelolaan data (tambah, hapus, ubah) dilakukan langsung pada HTML (static). Hal ini menyebabkan risiko tinggi terjadinya kerusakan struktur karena perubahan data yang dilakukan. Dengan pengelolaan data dilakukan pada database (Django Admin), risiko ini dapat tercegah karena perubahan data tidak menyentuh HTML. Selain itu, dengan penggunaan database, data menjadi fleksibel dan reusable untuk fitur-fitur lainnya.

3. makemigrations membuat file migrasi baru berdasarkan perubahan model. migrate mengaplikasikan file migrasi yang ada ke dalam database.
Contohnya ketika menambahkan thumbnail untuk project. makemigrations membuat file migrasi baru bernama 0003_project_thumbnail.py lalu migrate mengaplikasikan file tersebut ke database agar thumbnail tersimpan dalam tabel database.

AI Disclosure: Dalam pengerjaan proyek tugas individu 2, saya menggunakan bantuan AI berupa Claude Sonnet 5 version. Penggunaan AI paling banyak pada debugging dan add/delete input data karena tidak adanya sinkronisasi antara pws dengan lokal. Pemakaian lainnya ada pada permintaan style agar warna block pada project bisa otomatis berganti dalam scope yang ditentukan.

### Tugas 3
1. Penggunaan ModelForm didasarkan pada efisiensi. Dengan ModelForm, field HTML otomatis digenerate dari struktur model yang sudah ada dalam models.py seperti tipe data. Hal ini meringankan beban memasukkan validasi dan input secara manual untuk tiap file HTML. Lalu adanya kemudahan penyimpanan database dengan .save() dan pengembalian invalid input langsung pada HTML.
{% csrf_token %} digunakan untuk mencegah CSRF (Cross-Site Request Forgery). Dengan token unik terenkripsi, form request dipastikan valid dari User dan bukan pihak ketiga. Intinya csrf_token mastiin keamanan dan validitas request berdasarkan kecocokan dengan token unik terenkripsi.

2. JSON lebih disukai karena ukuran sintaksnya lebih ringkas dibandingkan XML yang perlu closing tag setiap elemen. Hal ini menyebabkan payload data lebih kecil yang membuat proses parsing di server menjadi lebih cepat. Selain itu, JSON lebih mudah dibaca oleh developer karena struktur datanya yang mirip sebagian besar bahasa pemrograman modern dan tidak perlu menggunakan library tambahan karena JSON sendiri terinspirasi dari JavaScript.

3. Browsser ngirim req HTTP ke URL --> path URL dicocokkan dengan fungsi view --> View ngambil queryset dari db yang berisi objek Python --> Objek diproses oleh serializers --> Objek dikonversi menjadi struktur data format teks JSON --> Hasil tadi dibungkus dengan HttpResponse atau JsonResponse dengan content_type="application/json" --> HttpResponse dikembalikan ke browser --> browser ngerender JSON dan menampilkan halaman tersebut pada User.
Serialization diperlukan karena HTTP hanya bisa mengirim data berbentuk bytes, sementara objek model Django berbentuk objek Python kompleks yang menyimpan referensi ke db. Disini serialization dipakai untuk mengonversi objek tersebut menjadi format bytes yang dapat dikirim dan dipahami bahasa pemrograman. intinya sebagai translator.

AI Disclosure: Dalam pengerjaan proyek tugas individu 3, saya menggunakan bantuan AI berupa Claude Sonnet 5 version. Penggunaan AI paling banyak pada debugging run local, deploy pws, dan set DateField.
log prompting: https://claude.ai/share/ffb755f7-c32a-4d04-b3d0-ee653db096a5 

### Tugas 4 
AI Disclosure: Dalam pengerjaan proyek tugas individu 4, saya menggunakan bantuan AI berupa Claude Sonnet 5 version. Penggunaan AI paling banyak pada debugging run local, deploy pws, dan struktur html.
log prompting: https://claude.ai/share/f51e31e9-01a7-46c2-9c58-8d697e73e60a 

### Tugas 5
1. Debouncing adalah teknik untuk menunda sebuah fungsi hingga suatu jeda waktu berlalu tanpa event baru. Mekanisme ini memastikan browser hanya mengirimkan permintaan setelah User jeda mengetik selama beberapa saat.
Teknik ini diperlukan pada fitur pencarian berbasis AJAX karena dapat mengurangi beban server, menghemat bandwidth, dan mencegah race condition. Intinya debouncing ini mencegah pengiriman req berulang ke server dan hanya mengirim input terakhir.

2. await berfungsi menahan eksekusi baris selanjutnya dalam fungsi async sampai objek Promise yang dikembalikan oleh fetch() selesai diproses dan mengembalikan objek Response.
Kalau await tidak digunakan, maka fetch() bakal langsung ngembaliin objek Promise dengan status pending, bukan response dari server. Risiko kesalahan dalam pemrosesan data akan meningkat karena menggunakan objek yang belum selesai diproses.

3. Cross-Site Scripting (XSS) adalah serangan ketika penyerang berhasil menyisipkan kode JavaScript miliknya ke dalam halaman web yang kemudian dijalankan di browser pengguna lain.
Data yang ditampilkan melalui AJAX/JS lebih rentan karena mereka memiliki sifat dinamis. Selain itu, template Django memiliki fitur proteksi bawaan, sehingga tidak perlu sanitasi manual.

AI disclosure: Dalam pengerjaan proyek tugas individu 5, saya menggunakan bantuan AI berupa Claude Sonnet 5 version. Penggunaan AI paling banyak pada debugging github. Awalnya sempat ada error karena discrepancy antara lokal dan github padahal sudah pull origin main. Claude langsung memberi saran overwrite permanen tanpa mencoba mencari dulu kesalahannya. Karena khawatir, saya akhirnya menelusuri history commit satu per satu dan menemukan letak kesalahannya. Ternyata merge terakhir ini ikut menyatukan merge #6 yang mana masih menyimpan data tugas 4, sehingga perubahan pada tutorial 5 teroverwrite.
log prompting: https://claude.ai/share/55cc2720-5b69-4338-a9f5-a2740b922ccc 

### Tugas 6
1. REST (Representational State Transfer) berperan sebagai arsitektur untuk merancang web API, bukan library atau format data. Oleh karena itu, API yang cuma mengembalikan JSON belum tentu RESTful. 
Karakteristik REST antara lain: data diperlakukan sebagai resource yang diakses lewat URI; stateless (setiap request membawa semua informasi yang dibutuhkan); klien dan server dipisah; antarmukanya seragam lewat metode HTTP standar; ada HATEOAS (Hypermedia As The Engine Of Application State) yang membuat respons memuat tautan ke aksi lain. Untuk PUT dan PATCH, keduanya sama-sama dipakai untuk mengubah data, tapi cakupannya berbeda. PUT mengganti seluruh representasi resource, yang membuat klien/user harus mengirim semua field yang dibutuhkan. PATCH hanya mengubah field yang dikirim. Contohnya, PUT cocok dipakai saat form edit profil dikirim lengkap, sedangkan PATCH cocok saat user cuma ingin mengganti alamat e-mailnya.

2. Serializer di DRF berperan sebagai representasi dan validasi data serta bekerja dua arah. Pada GET, serializer mengubah objek model jadi tipe data Python yang bisa dirender ke JSON (serialization). Pada POST atau PATCH, serializer menerima input, memvalidasinya, lalu menghasilkan data yang siap disimpan (deserialization). Hasilnya belum berupa string JSON,  selanjutnya renderer DRF megubah hasil tersebut menjadi JSON. Keuntungan dibanding merakit dictionary manual dengan memakai JsonResponse seperti di Tutorial 05 adalah validasi dan pemilihan field sudah ditangani serializer. Jadi kita tidak perlu menulis pengecekan tipe dan aturan input satu per satu, dan field yang tidak didaftarkan di `fields` (misalnya data sensitif) otomatis tidak ikut terkirim. selain itu, serializer juga mendukung penyimpanan dan pembaruan objek model melalui .save(). Intinya serializer ini penjaga pintu masuk dan keluar data. 

3. Autentikasi berperan sebagai verifikasi identitas, yaitu memastikan siapa yang sedang mengirim request. Otorisasi adalah penentuan hak akses dan bertugas memastikan apa yang boleh dilakukan user tersebut. Hak akses harus dicek pakai permission class di server karena menyembunyikan tombol di template cuma soal tampilan. siapa pun bisa mengirim request langsung lewat DevTools atau curl tanpa melewati template. Jadi kalau pengecekannya cuma di sisi tampilan, request yang tidak sah tetap bisa masuk. Dengan permission class, DRF memeriksa hak akses setelah proses autentikasi dan sebelum fungsi view dijalankan. Jika pengguna tidak memiliki hak akses, DRF akan menolak request dengan status 403 (Forbidden) atau 401 (Unauthorized), tergantung kondisi autentikasi dan konfigurasi yang digunakan. Permission class yang kita pakai juga tetap dibuat sendiri (IsPortfolioOwnerOrEditorOrReadOnly) karena aturan perannya khusus untuk proyek ini.

4. SessionAuthentication mengenali user dari cookie sesi lalu browser otomatis mengirim cookie itu (termasuk untuk request yang dipicu dari situs lain). Oleh karena itu, situs jahat bisa saja membuat browser user yang sedang login mengirim POST ke API dan mengubah data tanpa sepengetahuan user. Ini yang disebut CSRF. Makanya request yang mengubah data (POST, PUT, PATCH, DELETE) wajib membawa token CSRF lewat header X-CSRFToken. Situs lain tidak bisa membaca token ini karena kebijakan same-origin membuat request dari luar akan ditolak. 
Test yang memakai force_authenticate tidak cukup untuk membuktikan hal ini. Fungsi tersebut melewati proses autentikasi sepenuhnya, termasuk pengecekan CSRF di SessionAuthentication. Akibatnya test tetap lulus walaupun perlindungan CSRF tidak jalan. Untuk membuktikannya, kita perlu APIClient(enforce_csrf_checks=True) dengan .login() supaya sesinya dibuat sungguhan. Lalu kita cek apakah request tanpa token ditolak dan request dengan token diterima.

AI disclosure: Dalam pengerjaan proyek tugas individu 6, saya menggunakan bantuan AI berupa ChatGPT. Penggunaan AI paling banyak pada debugging. Salah satunya membaca output hasil pengecekan di terminal yang memakai kode unik. Selain itu juga digunakan untuk resolve error (line merah) pada experience.html. 
Kekurangan AI terdapat pada resolve Error. Saran perbaikan yang diberikan oleh ChatGPT tidak ada yang bisa me-resolve error tersebut, karena katanya dari segi syntax seharusnya sudah benar. Akan tetapi, editor (VS code) tetap menganggapnya sebagai error. Setelah ditelaah sendiri, ditemukan error terjadi karena editor membaca JS mentah, sehingga parser JavaScript mengira ada objek yang belum memiliki assignment. Namun syntax tersebut akan valid setelah Django merender template.
log prompting: https://chatgpt.com/share/6af18882-6614-83ec-8888-df9bef6f6aff

Special thx to:
- cecilia yang ngajarin input favicon
- melin dengan carousalnya
- marsya dengan music playernya (to be continued)
- my adek for my current custom favicon
- How to make transparent box: https://www.rumahweb.com/journal/belajar-css-bagian-20/ 
