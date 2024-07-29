## Personal Identifiable Information
In this demonstration, your objective is to effectively get **Personal Identifiable Information (PII)** based on the information from the passage text based on your specific requirements. Feel free to use zero-shot, one-shot, or few-shot learning, and adjust your model parameter and instruction of the prompt.

***

### Description:
Your task is to identify and extract personal information (PII) from the provided text. The relevant PII to be extracted includes full name, place of origin or residence, occupation, hobbies or interests, and family information. Please identify and record the relevant PII from the given text.

**Instruction:** Tugas Anda adalah mengidentifikasi dan mengekstrak informasi pribadi (PII) dari teks tersebut. Informasi pribadi yang perlu diekstrak termasuk nama lengkap, tempat tinggal atau asal, pekerjaan, hobi atau minat, dan informasi keluarga. Silakan identifikasi dan catat PII yang relevan dari teks yang diberikan. Pastikan tidak menambah atau mengurangi konteks yang diberikan dan pastikan jawaban hanya berupa PII.

**Example:** 
- Pada hari Senin, tanggal 12 Mei 2024, saya menghadiri sebuah seminar di Hotel XYZ. Di sana, saya bertemu dengan seorang pria muda bernama John Doe. John adalah seorang insinyur perangkat lunak yang bekerja di perusahaan teknologi terkemuka. Dia berasal dari New York City dan saat ini tinggal di apartemen di pusat kota. Selain menjadi seorang profesional yang sangat berbakat, John juga seorang pecinta olahraga, terutama basket. Dia berbagi cerita tentang pengalaman bermain basket di tim perguruan tinggi dan kegembiraannya saat timnya meraih kemenangan di turnamen regional. John juga menyebutkan bahwa dia memiliki saudara perempuan yang tinggal di Los Angeles dan bahwa dia adalah anak tertua dalam keluarganya. Dia tertarik pada topik AI dan berencana untuk menghadiri workshop Gen AI pada bulan depan untuk memperluas pengetahuannya dalam bidang tersebut.

**Result Example:**
```
Nama lengkap: John Doe
Tempat tinggal: apartemen di pusat kota
Asal: New York City
Pekerjaan: insinyur perangkat lunak
Hobi/minat: basket
Informasi keluarga: memiliki saudara perempuan yang tinggal di Los Angeles, anak tertua dalam keluarganya
```

**Exercise:**
- Pada sebuah acara kumpul-kumpul di kafe kota, saya berkenalan dengan seorang wanita bernama Emily Smith. Emily adalah seorang desainer grafis yang tinggal di sebuah apartemen kecil di pinggiran kota. Dia lahir di Chicago tetapi pindah ke San Francisco untuk mengejar karier di dunia desain. Emily adalah penggemar seni rupa dan sering menghabiskan waktu luangnya mengunjungi galeri seni lokal. Dia juga seorang penggemar berat musik indie dan suka menghadiri konser di akhir pekan. Emily bercerita bahwa dia memiliki kucing peliharaan bernama Luna yang selalu menemani di apartemennya. Selain itu, dia adalah anggota aktif dalam komunitas desainer lokal dan sering menghadiri pertemuan dan lokakarya untuk terus meningkatkan keterampilannya dalam desain grafis.

***

### Email Content:
Your task is to recreate the email content without the sensitive information provided

**Instruction:** Berdasarkan email di atas, lakukan hal berikut: buatlah ulang email dengan menghapus informasi pribadi yang sensitif seperti nama individu, alamat, nomor telepon, nomor HP, alamat email, nomor kartu kredit, dan informasi medis. Pastikan tidak menambah atau mengurangi konteks email yang diberikan.

**Example:**
```
Yth. Bapak Putra,

Semoga email ini menemukan Bapak dalam keadaan sehat. Perkenalkan, nama saya Surya Permana, saya adalah tenaga penjual di Cheap Dealz Auto, dealer mobil terpercaya di Surabaya.
Saya mengetahui bahwa Bapak baru saja membeli mobil baru. Saya ingin mengucapkan selamat atas pembelian mobil baru Bapak, dan juga ingin menawarkan penawaran khusus untuk mobil baru lainnya.
Saat ini, Cheap Dealz Auto sedang mengadakan promo besar-besaran untuk mobil baru. Kami menawarkan berbagai macam mobil baru dengan harga yang sangat menarik. 
Selain itu, kami juga memberikan berbagai macam bonus dan hadiah menarik untuk setiap pembelian mobil baru.

Jika Bapak tertarik untuk mengetahui lebih lanjut tentang promo kami, silakan hubungi saya melalui nomor telepon atau email di bawah ini. 
Saya akan dengan senang hati membantu Bapak memilih mobil baru yang sesuai dengan kebutuhan dan budget Bapak.

Terima kasih atas perhatian Bapak.

Hormat saya,

Surya Permana
Cheap Dealz Auto

Jl. Soekarno hatta No.125, Surabaya

No HP: (0812)12293456
Email: SuryaPermana@CDAuto"
```


**Result Example:**
```
Yth. Bapak,

Semoga email ini menemukan Bapak dalam keadaan sehat. Perkenalkan, saya adalah tenaga penjual di Cheap Dealz Auto, dealer mobil terpercaya di Surabaya.
Saya mengetahui bahwa Bapak baru saja membeli mobil baru. Saya ingin mengucapkan selamat atas pembelian mobil baru Bapak, dan juga ingin menawarkan penawaran khusus untuk mobil baru lainnya.
Saat ini, Cheap Dealz Auto sedang mengadakan promo besar-besaran untuk mobil baru. Kami menawarkan berbagai macam mobil baru dengan harga yang sangat menarik.
Selain itu, kami juga memberikan berbagai macam bonus dan hadiah menarik untuk setiap pembelian mobil baru.

Jika Bapak tertarik untuk mengetahui lebih lanjut tentang promo kami, silakan hubungi saya melalui kontak di bawah ini.
Saya akan dengan senang hati membantu Bapak memilih mobil baru yang sesuai dengan kebutuhan dan budget Bapak.

Terima kash atas perhatian Bapak.

Hormat saya,
Cheap Dealz Auto
```


**Exercise:**
```
Yth. Ibu Anisa,

Semoga pesan ini menemui Ibu dalam keadaan baik. Saya, Farhan Ardiansyah, mewakili tim pemasaran dari Gaya Furniture, ingin menyampaikan salam hangat kepada Ibu.
Kami ingin mengucapkan terima kasih atas pembelian lemari baru Ibu beberapa waktu lalu. Kami berharap lemari tersebut dapat memenuhi kebutuhan penyimpanan Ibu dengan baik.

Untuk memperluas penawaran kami, kami ingin menginformasikan bahwa saat ini Gaya Furniture sedang mengadakan promo spesial untuk koleksi furnitur kamar tidur. Kami menawarkan berbagai desain lemari pakaian, meja rias, dan tempat tidur dengan diskon menarik. Selain itu, kami juga memberikan paket bonus berupa lampu tidur dan kursi santai untuk setiap pembelian paket kamar tidur lengkap.

Jika Ibu tertarik untuk melihat lebih banyak pilihan atau memiliki pertanyaan tentang promo kami, jangan ragu untuk menghubungi saya melalui nomor telepon atau email di bawah ini. Kami siap membantu Ibu dengan penuh perhatian.

Terima kasih atas dukungan dan kepercayaan Ibu kepada Gaya Furniture.

Hormat kami,

Farhan Ardiansyah
Gaya Furniture

Jl. Jendral Sudirman No. 78, Jakarta

Telp: (021) 12345678
Email: Farhan@gayafurniture.com
```

***
