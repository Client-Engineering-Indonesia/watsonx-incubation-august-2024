## Review, Recommendation, Sentiment
In this demonstration, your objective is to get sentiment **review, recommendation, or sentiment** based on the information from the passage text based on your specific requirements. Feel free to use zero-shot, one-shot, or few-shot learning, and adjust your model parameter and instruction of the prompt.

***

### Product Review:
Your task is to review the information based on the product perspective.


**Instruction:** Anda adalah asisten yang bertugas untuk menganalisis konteks dalam ulasan produk. Temukan informasi seperti sentimen pengguna (positif/netral/negatif) dan alasannya, apakah terdapat konteks yang mencerminkan kekecewaan atau kepuasan, nama produk yang diulas, dan berikan informasi tentang perusahaan yang bersangkutan. Sebagai asisten dalam ulasan produk, tugas Anda adalah menganalisis dan mengumpulkan informasi yang relevan dari ulasan yang tersedia. Jawablah pertanyaan dalam bahasa Indonesia dan susun dalam format JSON tanpa informasi tambahan atau tanggapan.


**Example:** 
- Kebetulan lagi perlu lampu untuk ruang tidur saya, dan ternyata lampu tidur LightPro ini punya battery cadangan juga, dan dari segi harga juga cukup terjangkau, jadi saya memutuskan langsung membelinya. Walau kabelnya rusak selama pengiriman, penjual mau menggantinya. Dan ternyata ada bagian yang kurang lengkap juga, dan saya langsung memberi tahu penjual. Barang yang kurang lengkap dikirim bersamaan dengan kabel yang baru! menurut saya Lumina adalah perusahaan yang peduli dengan pelanggannya, dan bertanggung jawab dengan produk mereka!!


**Result Example:**
```
{"sentimen": "positif",",
"produk": "Lampu tidur LightPro",
"perusahaan": "Lumina"}
```


**Exercise:**
- Saya sedang mencari earphone yang nyaman dan memiliki kualitas suara yang bagus untuk mendengarkan musik saat bepergian. Saya menemukan produk dari SoundWave yang memiliki ulasan bagus dan harganya juga cukup terjangkau. Setelah saya membelinya, saya menyadari bahwa kualitas suaranya memang luar biasa, namun sayangnya salah satu earphone-nya tidak berfungsi dengan baik setelah beberapa hari penggunaan. Saya menghubungi layanan pelanggan SoundWave, dan mereka dengan cepat mengirimkan penggantian earphone baru tanpa biaya tambahan. Selain itu, mereka juga memberikan saya bonus diskon untuk pembelian berikutnya sebagai kompensasi atas ketidaknyamanan yang saya alami. Saya sangat menghargai respons cepat dan pelayanan yang ramah dari SoundWave, sehingga saya merasa yakin untuk merekomendasikan produk-produk mereka kepada teman-teman saya.


***


### Recommendation
Your task is to give recommendations and suggestions based on the review


**Instruction:** Anda adalah asisten yang bertugas untuk menganalisis konteks dalam ulasan produk. Berikan rekomendasi untuk meningkatkan produk atas review yang diberikan


**Example:** 
- Saya biasanya memesan makanan dari restoran Thai Delight secara langsung dan selalu puas dengan kualitasnya. Namun, akhir-akhir ini saya mencoba menggunakan aplikasi pengiriman makanan untuk memesan makanan dari restoran tersebut. Sayangnya, saya menemui beberapa masalah, seperti pesanan yang sering terlambat sampai dan tidak sesuai dengan yang saya pesan. Bahkan, saya pernah mengalami kesulitan untuk menghubungi layanan pelanggan ketika ada masalah dengan pesanan saya.


**Result Example:**
```
1. Meningkatkan akurasi pesanan dengan memastikan bahwa pesanan yang dikirimkan sesuai dengan yang dipesan.
2. Meningkatkan kecepatan pengiriman pesanan untuk mengurangi waktu tunggu pelanggan.
3. Meningkatkan kualitas layanan pelanggan dengan memastikan bahwa pelanggan dapat dengan mudah menghubungi layanan pelanggan ketika ada masalah dengan pesanan.
```


**Exercise:**
- Saya seorang penggemar berat kopi, dan biasanya saya memesannya dari toko kopi lokal di sekitar tempat tinggal saya. Namun, ketika saya mencoba memesan kopi favorit saya melalui aplikasi pengiriman kopi, saya merasa sangat puas dengan pengalaman itu. Pesanan saya tiba tepat waktu dan kopi yang saya terima masih segar dan berkualitas. Proses pembayaran pun sangat mudah dan nyaman. Saya pasti akan menggunakan aplikasi ini lagi untuk memesan kopi di masa mendatang.

***
