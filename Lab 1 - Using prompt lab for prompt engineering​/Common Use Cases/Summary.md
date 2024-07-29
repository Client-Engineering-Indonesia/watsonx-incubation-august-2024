## Summary
In this demonstration, your objective is to get a **Summarization** based on the information from the passage text based on your specific requirements. Feel free to use zero-shot, one-shot, or few-shot learning, and adjust your model parameter and instruction of the prompt.


***


### Meeting Summarization:
Your task is to summarize the information from the meeting conversation and generate Minutes Of Meeting (MoM) report.

**Instruction:** 
Anda adalah asisten yang bertugas untuk menganalisis percakapan dalam rapat. Buatlah dalam bahasa Indonesia dengan format Minutes Of Meeting (MoM), mencakup topik, kapan meeting dilaksanakan, daftar peserta, ringkasan, poin penting dalam bentuk daftar, dan langkah-langkah selanjutnya yang diambil.


**Example:** 
```
00:00 [Agus] Selamat pagi, semuanya. Terima kasih sudah hadir dalam pertemuan online pada hari ini. Saya sangat senang cuaca hari ini baik karena kemarinl 7 Mei hujan terus.
00:05 [Agus] Kita akan memulai dengan membahas implementasi sistem baru untuk proses produksi yang menjadi fokus utama.
00:15 [Agus] Pak Budi, mohon penjelasan mendalam mengenai desain dan arsitektur sistem baru yang akan diterapkan.
00:30 [Budi] Tentu. Sistem baru yang kami rencanakan dirancang untuk memanfaatkan infrastruktur cloud computing yang canggih, dengan lapisan keamanan yang ditingkatkan dan mekanisme redundansi yang kuat untuk memastikan kehandalan operasional.
00:45 [Budi] Keuntungan utama dari implementasi ini adalah efisiensi yang ditingkatkan melalui penggunaan sumber daya yang terelastis dan skalabilitas yang dapat disesuaikan dengan kebutuhan produksi, serta integrasi yang lebih mulus dengan sistem yang ada.
01:05 [Agus] Terima kasih, Pak Budi, penjelasan yang sangat komprehensif.
01:10 [Agus] Apakah ada pertanyaan lebih lanjut seputar infrastruktur atau aspek teknis lainnya?
01:15 [Cici] Saya ingin memahami lebih dalam tentang strategi yang akan diterapkan dalam memitigasi risiko dan menangani potensi kendala selama proses migrasi.
01:30 [Budi] Tentu. Kami telah merancang rencana mitigasi risiko yang komprehensif, termasuk uji coba terperinci, pemulihan bencana, dan perencanaan kebalikan. Selain itu, kami juga memiliki tim respons yang siap tanggap untuk menangani kendala yang mungkin muncul secara proaktif.
01:45 [Agus] Pertanyaan yang sangat relevan, Cici. Terima kasih atas kecerdasan dalam mempertanyakan hal tersebut.
01:50 [Agus] Apakah ada pertimbangan tambahan atau pemikiran lain sebelum kita lanjut ke tahap selanjutnya?
01:55 [Dedi] Saya mendukung implementasi sistem baru ini, namun saya ingin menyarankan agar ada evaluasi rutin untuk memastikan bahwa performa sistem tetap optimal dan sesuai dengan harapan.
02:00 [Agus] Saya setuju dengan saran tersebut. Evaluasi rutin akan menjadi bagian penting dari siklus pengembangan dan perbaikan berkelanjutan.
02:05 [Agus] Baiklah, dengan dukungan dari semua pihak, saya rasa kita sudah cukup untuk tahap diskusi saat ini. Terima kasih atas kontribusi dan pemikiran yang sangat berharga dari masing-masing dari Anda.
02:10 [Agus] Pak Budi, saya harap Anda dapat mengoordinasikan dengan tim IT untuk memulai tahap migrasi data yang telah direncanakan dengan cermat.
```


**Result Example:** 
```
Minutes of Meeting (MoM)

Topik: Implementasi Sistem Baru untuk Proses Produksi
Tanggal: 8 Mei
Daftar Peserta:
- Agus
- Budi
- Cici
- Dedi

Ringkasan:
Pertemuan online ini membahas implementasi sistem baru untuk proses produksi yang menjadi fokus utama. Pak Budi menjelaskan desain dan arsitektur sistem baru yang akan diterapkan, termasuk keuntungan utama seperti efisiensi yang ditingkatkan dan integrasi yang lebih mulus dengan sistem yang ada. Peserta juga membahas strategi mitigasi risiko dan menangani potensi kendala selama proses migrasi.

Poin Penting:
- Implementasi sistem baru untuk proses produksi
- Desain dan arsitektur sistem baru menggunakan infrastruktur cloud computing yang canggih
- Keuntungan utama: efisiensi yang ditingkatkan dan integrasi yang lebih mulus dengan sistem yang ada
- Strategi mitigasi risiko dan menangani potensi kendala selama proses migrasi
- Evaluasi rutin untuk memastikan performa sistem tetap optimal

Langkah-Langkah Selanjutnya:
- Pak Budi akan mengoordinasikan dengan tim IT untuk memulai tahap migrasi data yang telah direncanakan dengan cermat.
- Evaluasi rutin akan dilakukan untuk memastikan performa sistem tetap optimal dan sesuai dengan harapan.
```


**Exercise:** 
```
10:00 [Rina] Selamat pagi, semuanya. Terima kasih telah bergabung dalam pertemuan strategis HR hari ini, tanggal 13 Mei 2024. Kita akan mulai dengan membahas rencana pengembangan karyawan untuk tahun ini.
10:05 [Rina] Pertama-tama, saya ingin menyampaikan bahwa target kita tahun ini adalah meningkatkan tingkat retensi karyawan sebesar 15% dari tahun sebelumnya.
10:10 [Rina] Untuk mencapai target tersebut, kami telah merancang program pelatihan dan pengembangan yang lebih terstruktur dan menyeluruh.
10:15 [Rina] Pak Joko, bisakah Anda memberikan gambaran singkat mengenai program pelatihan yang direncanakan?
10:20 [Joko] Tentu, Rina. Kami merencanakan program pelatihan yang terdiri dari serangkaian kursus online dan pelatihan langsung yang disesuaikan dengan kebutuhan karyawan di setiap departemen.
10:25 [Joko] Selain itu, kami juga akan mengadakan sesi mentoring dan coaching untuk membantu karyawan dalam pengembangan keterampilan spesifik dan pencapaian tujuan karir mereka.
10:30 [Rina] Terima kasih, Pak Joko, rencana tersebut terdengar sangat komprehensif.
10:35 [Rina] Ada pertanyaan atau saran lain terkait program pelatihan dan pengembangan?
10:40 [Santi] Saya ingin menyarankan agar ada mekanisme evaluasi yang jelas untuk mengukur efektivitas program pelatihan tersebut. Bagaimana rencana evaluasinya?
10:45 [Joko] Kami telah merencanakan survei kepuasan peserta setelah setiap sesi pelatihan, serta melakukan evaluasi kinerja sebelum dan sesudah pelatihan untuk mengukur peningkatan kinerja yang terkait.
10:50 [Rina] Pertimbangan yang bagus, Santi. Evaluasi akan menjadi kunci untuk memastikan program pelatihan kita berjalan dengan baik.
10:55 [Rina] Ada saran atau pertimbangan lain sebelum kita lanjut ke langkah berikutnya?
11:00 [Budi] Saya ingin menyarankan agar kita juga mempertimbangkan program penghargaan dan insentif untuk mengapresiasi partisipasi dan pencapaian karyawan dalam program pelatihan ini.
11:05 [Rina] Saya setuju dengan saran tersebut, Budi. Program penghargaan akan menjadi motivasi tambahan bagi karyawan untuk mengambil bagian aktif dalam pengembangan mereka.
11:10 [Rina] Dengan adanya dukungan dari semua pihak, saya rasa kita sudah siap untuk melangkah ke tahap implementasi. Terima kasih atas kontribusi dan ide-ide yang sangat berharga dari masing-masing dari Anda.
11:15 [Rina] Pak Joko, tolong koordinasikan dengan tim pelatihan untuk memulai implementasi program pengembangan karyawan sesuai dengan rencana yang telah disusun.
```


***


### Meeting Summarization in JSON:
Your task is to summarize the information based on the information provided.

**Instruction:** 
Anda adalah asisten yang bertugas untuk menganalisis percakapan dalam rapat. Jawaban hanya berupa struktur format json yang berisi rangkuman dari transkrip tersebut tanpa menambah informasi lainnya selain format json

**Example:**
Input:
```
00:00 [Budi] Halo semua, 
00:05 [Budi] Saya ingin membagikan pembaruan tentang proyek Y hari ini. 
00:15 [Budi] Proyek Y telah memasuki tahap pengembangan. Kami telah menyelesaikan beberapa fitur utama, dan kami sedang mengerjakan fitur-fitur lainnya. 
00:30 [Cici] Bagus sekali! 
00:35 [Cici] Saya mendengar dari pelanggan A hari ini, dan mereka sangat senang dengan proyek Y. Mereka mengatakan bahwa proyek ini memenuhi semua kebutuhan mereka. 
00:45 [Dedi] Pelanggan B juga mengatakan mereka sangat puas dengan proyek Y. Mereka hanya memiliki beberapa permintaan perubahan kecil. 
01:05 [Budi] Kami akan bekerja sama dengan pelanggan B untuk memenuhi permintaan perubahan mereka. Kami berharap dapat menyelesaikan pengembangan proyek Y pada Senin, 30 Oktober 2023, pukul 17.00 WIB. 
01:20 [Cici] Baiklah, saya akan menghubungi pelanggan A dan B untuk mengatur rapat demo pada Jumat, 27 Oktober 2023, pukul 14.00 WIB. 
01:30 [Dedi] Saya akan menyiapkan dokumen desain sistem proyek Y untuk disampaikan kepada pelanggan pada Rabu, 25 Oktober 2023, pukul 11.00 WIB. 
01:40 [Budi] Terima kasih atas kerja keras kalian semua. 
```

Output:
```
{
    "action_items": [
        {
            "action": "Kerjakan fitur-fitur lainnya dari proyek Y.",
            "due_to": "Senin, 30 Oktober 2023, pukul 17.00 WIB",
            "pic": "Budi"
        },
        {
            "action": "Jawab pertanyaan pelanggan B tentang proyek Y.",
            "due_to": "Senin, 30 Oktober 2023, pukul 17.00 WIB",
            "pic": "Budi dan Dedi"
        },
        {
            "action": "Siapkan dokumen desain sistem proyek Y untuk disampaikan kepada pelanggan.",
            "due_to": "Rabu, 25 Oktober 2023, pukul 11.00 WIB",
            "pic": "Dedi"
        },
        {
            "action": "Hubungi pelanggan A dan B untuk mengatur rapat demo.",
            "due_to": "Jumat, 27 Oktober 2023, pukul 14.00 WIB",
            "pic": "Cici"
        }
    ]
}
```

```
00:00 [Budi] Halo semua, 
00:05 [Budi] Saya ingin membagikan pembaruan tentang proyek X hari ini. 
00:15 [Budi] Proyek X telah memasuki tahap pengujian akhir. Kami telah menyelesaikan semua fitur utama, dan kami sedang mengerjakan beberapa perbaikan bug kecil. 
00:30 [Cici] Bagus sekali! 
00:35 [Cici] Saya mendengar dari pelanggan Y hari ini, dan mereka sangat senang dengan proyek X. Mereka mengatakan bahwa proyek ini memenuhi semua kebutuhan mereka. 
00:45 [Dedi] Pelanggan Z juga mengatakan mereka sangat puas dengan proyek X. Mereka hanya memiliki beberapa permintaan perubahan kecil. 
01:05 [Budi] Kami akan bekerja sama dengan pelanggan Z untuk memenuhi permintaan perubahan mereka. Kami berharap dapat menyelesaikan proyek X pada Jumat, 27 Oktober 2023, pukul 12.00 WIB. 
01:20 [Cici] Baiklah, saya akan menghubungi pelanggan Y dan Z untuk mengatur pengiriman produk dan jadwalkan pelatihan pada Kamis, 26 Oktober 2023, pukul 10.00 WIB. 
01:30 [Dedi] Saya akan menyiapkan laporan proyek untuk disampaikan kepada tim penjualan pada Rabu, 25 Oktober 2023, pukul 08.00 WIB. 
01:40 [Budi] Terima kasih atas kerja keras kalian semua. 
```

**Result Example:**
```
{
    "action_items": [
        {
            "action": "Kerjakan perbaikan bug kecil dari proyek X",
            "due_to": "Jumat, 27 Oktober 2023, pukul 12.00 WIB",
            "pic": "Budi"
        },
        {
            "action": "Jawab pertanyaan pelanggan Z tentang proyek X.",
            "due_to": "Jumat, 27 Oktober 2023, pukul 12.00 WIB",
            "pic": "Budi dan Dedi"
        },
        {
            "action": "Siapkan laporan proyek untuk disampaikan kepada tim penjualan.",
            "due_to": "Rabu, 25 Oktober 2023, pukul 08.00 WIB",
            "pic": "Dedi"
        },
        {
            "action": "Hubungi pelanggan Y dan Z untuk mengatur pengiriman produk dan jadwalkan pelatihan.",
            "due_to": "Kamis, 26 Oktober 2023, pukul 10.00 WIB",
            "pic": "Cici"
        }
    ]
}
```


**Exercise:**
```
00:00 [Manager] Selamat pagi tim, saya harap semuanya dalam keadaan baik hari ini.
00:05 [Manager] Seperti yang telah dibahas sebelumnya, kita perlu meninjau kemajuan Proyek Alpha dan merencanakan langkah selanjutnya.
00:15 [Project Lead] Saya senang bisa memberitahu Anda bahwa Proyek Alpha telah mencapai tahap pengembangan akhir.
00:25 [Project Lead] Saat ini, kami sedang melakukan uji coba integrasi antara modul A dan B.
00:35 [Developer 1] Ada beberapa masalah kecil yang muncul selama uji coba, tapi kami sedang dalam proses penyelesaian.
00:45 [Manager] Bagus. Kami perlu memastikan bahwa semua bug diperbaiki sebelum tahap pengujian lanjutan.
00:55 [QA Lead] Saya akan memastikan tim QA untuk memeriksa semua fitur dan melaporkan bug secepat mungkin.
01:05 [Project Lead] Saya berharap kita dapat menyelesaikan pengujian tambahan dan perbaikan bug pada Rabu, 25 Mei 2024, pukul 18.00 WIB.
01:20 [Manager] Baiklah. Setelah itu, kita perlu merencanakan peluncuran beta.
01:30 [Marketing Lead] Saya akan mengoordinasikan dengan tim pemasaran untuk mempersiapkan kampanye peluncuran beta.
01:40 [Manager] Selain itu, kita juga perlu mempersiapkan materi pelatihan untuk pelanggan yang akan menggunakan produk ini.
01:50 [Training Lead] Saya akan memimpin tim pelatihan untuk menyusun materi dan jadwal pelatihan.
02:05 [Manager] Terakhir, saya ingin menyampaikan bahwa presentasi proyek akan dilakukan pada Jumat, 26 Mei 2024, pukul 10.00 WIB.
02:15 [Manager] Terima kasih atas dedikasi dan kerja keras kalian. Mari kita pastikan Proyek Alpha sukses diluncurkan!
```

