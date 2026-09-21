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

Special thx to:
- cecilia yang ngajarin input favicon
- melin dengan carousalnya
- marsya dengan music playernya (to be continued)
- my adek for my current custom favicon
- How to make transparent box: https://www.rumahweb.com/journal/belajar-css-bagian-20/ 
