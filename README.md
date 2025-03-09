# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut adalah institusi pendidikan tinggi yang berdiri sejak tahun 2000, yang telah menghasilkan banyak lulusan berkualitas. Meskipun demikian, mereka menghadapi tantangan besar terkait tingginya angka dropout di kalangan mahasiswa. Hal ini tidak hanya memengaruhi reputasi institut tetapi juga kualitas pendidikan yang diberikan. Untuk mengatasi masalah ini, Jaya Jaya Institut ingin mengidentifikasi mahasiswa yang berisiko drop-out lebih awal, agar dapat diberikan dukungan atau intervensi yang lebih tepat dan terarah.

Seiring dengan meningkatnya persaingan dalam dunia pendidikan tinggi dan semakin kompleksnya kebutuhan mahasiswa, penting bagi Jaya Jaya Institut untuk mengadopsi teknologi berbasis data untuk membantu mengatasi masalah ini. Dengan menggunakan analitik dan machine learning, institut ini berharap dapat mengidentifikasi mahasiswa yang berisiko drop-out lebih dini dan memberikan bimbingan yang diperlukan agar mereka dapat menyelesaikan studi mereka dengan sukses.

### Permasalahan Bisnis
1. **Tingginya Angka Dropout**  
   Jaya Jaya Institut menghadapi tantangan dengan tingginya angka mahasiswa yang keluar sebelum lulus, yang berdampak pada reputasi dan tingkat kelulusan.

2. **Kesulitan Mengidentifikasi Mahasiswa Berisiko Dropout**  
   Pihak institut kesulitan mendeteksi mahasiswa yang berisiko dropout secara dini, sehingga tidak dapat memberikan intervensi tepat waktu.

3. **Kurangnya Sistem Dukungan yang Efisien**  
   Tidak ada sistem berbasis data yang memungkinkan pemberian dukungan atau intervensi secara terarah dan cepat untuk mahasiswa yang membutuhkan.

4. **Pemanfaatan Data yang Terbatas**  
   Data yang ada belum dimanfaatkan secara maksimal untuk memprediksi dan mencegah risiko dropout, sehingga keputusan terkait kebijakan dan intervensi kurang berbasis data.

### Cakupan Proyek
- **Dashboard Analitik**: Membuat dashboard analitik untuk memvisualisasikan performa mahasiswa dan mendeteksi pola yang bisa menunjukkan potensi risiko drop-out. Dashboard ini memberikan insight tentang statistik performa mahasiswa, seperti tingkat kelulusan, kehadiran, dan nilai mata kuliah.
  
- **Model Machine Learning**: Mengembangkan model machine learning untuk memprediksi status mahasiswa (Dropout, Graduate, Enrolled) berdasarkan data yang ada. Model ini menggunakan berbagai algoritma untuk memaksimalkan akurasi prediksi, membantu pihak manajemen dalam membuat keputusan terkait intervensi.

- **Aplikasi Streamlit**: Membangun aplikasi berbasis Streamlit yang memungkinkan pihak manajemen dan dosen untuk memasukkan data mahasiswa secara langsung dan mendapatkan prediksi status mahasiswa serta informasi performa secara keseluruhan. Aplikasi ini mempermudah pengguna untuk mengakses model dan insight yang telah dikembangkan.

- **Rekomendasi untuk Intervensi, Kebijakan, dan Action Items**: Berdasarkan hasil analisis dan model prediksi, diberikan rekomendasi tindakan untuk intervensi yang tepat bagi mahasiswa berisiko dropout, seperti meningkatkan program bimbingan atau mentoring. Selain itu, disarankan kebijakan untuk meningkatkan tingkat kelulusan dan kepuasan mahasiswa dengan memanfaatkan data untuk membuat keputusan kebijakan yang lebih tepat dan terarah.

### **Persiapan**

**Sumber Data**  
Data yang digunakan dalam proyek ini dapat diakses melalui [link berikut](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

#### **Setup Environment**  
Berikut adalah langkah-langkah untuk menyiapkan environment dan menjalankan Streamlit dashboard serta membuka Looker Studio Dashboard:

##### 1. **Membuat Virtual Environment dengan Conda**
   Pertama, buat environment baru menggunakan Conda:

   ```bash
   conda create --name streamlit-venv python=3.10
   ```

   Aktifkan environment yang telah dibuat:

   ```bash
   conda activate streamlit-venv
   ```

##### 2. **Install Dependencies dari `requirements.txt`**
   Setelah environment aktif, pastikan Anda memiliki file `requirements.txt` yang berisi daftar library yang dibutuhkan untuk proyek ini. Jika belum ada, buat file `requirements.txt` dan masukkan dependensi yang dibutuhkan. Contoh `requirements.txt` harus berisi:

   ```
   streamlit
   pandas
   scikit-learn
   matplotlib
   numpy
   joblib
   ```

   Untuk menginstall dependencies dari file `requirements.txt`, jalankan:

   ```bash
   pip install -r requirements.txt
   ```

##### 3. **Menjalankan Streamlit Dashboard**
   Setelah semua dependensi terinstall, jalankan Streamlit dashboard dengan perintah:

   ```bash
   streamlit run nama_file_dashboard.py
   ```

   Gantilah `nama_file_dashboard.py` dengan nama file Python yang berisi Streamlit dashboard Anda.

   Setelah perintah dijalankan, Streamlit akan memberikan URL (biasanya `http://localhost:8501`) di mana Anda bisa melihat dashboard tersebut di browser.

Tentu! Berikut adalah penjelasan yang lebih lengkap:

##### 4. **Membuka Looker Studio Dashboard**
Untuk melihat Looker Studio Dashboard, Anda perlu melakukan langkah-langkah berikut:


1. **Login dengan Akun Google**  
   Pastikan Anda sudah login ke akun Google Anda. Jika belum, login terlebih dahulu menggunakan akun Google yang valid.

2. **Akses Dashboard**  
   Setelah login, buka [Tautan ini](https://lookerstudio.google.com/reporting/90881462-9394-4715-bd2d-473f526ed2da). di browser Anda. Anda akan diarahkan ke dashboard yang telah dibuat dan dapat melihatnya secara langsung.

Dengan langkah-langkah ini, Anda dapat mengatur lingkungan kerja, menjalankan aplikasi Streamlit, dan membuka Looker Studio dashboard dengan mudah.


## Business Dashboard

### 1. Overview of the Business Dashboard
**Student Performance Analytics Dashboard** menyediakan wawasan utama tentang data mahasiswa, termasuk tren **enrollment**, **dropout**, dan **graduation**. Dashboard ini mendukung pemangku kepentingan dalam mengambil keputusan berbasis data. Kamu dapat mengaksesnya di sini: [Looker Studio Dashboard](https://lookerstudio.google.com/reporting/90881462-9394-4715-bd2d-473f526ed2da).

### 2. Available Filters
Dashboard ini memiliki dua filter utama: **Status**, yang memungkinkan pemfilteran mahasiswa berdasarkan kategori seperti **Enrolled** (794 mahasiswa), **Dropout** (1.420 mahasiswa), dan **Graduate** (2.210 mahasiswa); serta **Marital Status**, yang mengelompokkan mahasiswa berdasarkan status pernikahan mereka.

### 3. Key Metrics
Dashboard ini menampilkan beberapa metrik utama: **Total Students** sebanyak 4,42K, **Total Courses** sebanyak 17, **Nationalities Represented** sebanyak 21, **Average Unemployment Rate** sebesar 11,57%, dan **Average Age** sebesar 23,27 tahun.

### 4. Insights dari Setiap Visualisasi

- **Perbandingan Status Siswa Berdasarkan Course**: Jumlah lulusan tertinggi berasal dari **Nursing** (548 mahasiswa), diikuti oleh **Social Services** (248 mahasiswa). Jumlah mahasiswa **dropout** cukup tinggi di **Management Evening** (136), **Nursing** (118), dan **Journalism** (101). Mahasiswa **enrolled** paling banyak terdapat di **Management** (108) dan **Nursing** (100).

- **Presentasi Gender Berdasarkan Status**: Dari total lulusan, **75,19% adalah perempuan** dan **24,81% laki-laki**, menunjukkan tingkat keberhasilan yang lebih tinggi pada mahasiswa perempuan. Pada kategori **dropout**, distribusi gender hampir seimbang, yaitu **50,67% perempuan** dan **49,33% laki-laki**. Untuk mahasiswa yang masih **enrolled**, **61,34% adalah perempuan**, sementara **38,66% laki-laki**.

- **Siswa Berdasarkan Gender**: Terdapat **2.868 mahasiswa perempuan** dan **1.556 mahasiswa laki-laki**, yang menunjukkan tingkat **enrollment** perempuan lebih tinggi di institusi ini.

- **Siswa Berdasarkan Marital Status**: Mayoritas mahasiswa **berstatus single** (3,9K mahasiswa, sekitar **88%**), sementara **mahasiswa menikah berjumlah 379**. Kategori lainnya meliputi **divorced** (91), **legally separated** (25), dan **widowed** (4).

- **Nilai Semester 1 dan 2 Non/Beasiswa**: Mahasiswa **tanpa beasiswa** memiliki **curricular units** lebih tinggi di **semester 1 (33,8K)** dan **semester 2 (32,2K)** dibandingkan mahasiswa **dengan beasiswa** (13,3K di semester 1 dan 13K di semester 2). Hal ini menunjukkan bahwa mahasiswa non-beasiswa cenderung mengambil lebih banyak kredit akademik.

- **Jumlah Siswa Berdasarkan Umur**: **Enrollment** tertinggi terjadi pada usia **18 tahun (1.036 mahasiswa)** dan **19 tahun (911 mahasiswa)**. Jumlah mahasiswa menurun tajam setelah usia **21 tahun**, dengan kurang dari **100 mahasiswa** per kelompok usia di atas **25 tahun**. Mahasiswa tertua yang terdaftar berusia **48 tahun**, namun jumlahnya sangat kecil.

### 5. Kesimpulan untuk Dashboard
Dashboard ini memberikan wawasan yang dapat ditindaklanjuti mengenai performa mahasiswa, menyoroti tren **enrollment**, tingkat **dropout**, dan pencapaian akademik. Temuan utama meliputi **tingginya tingkat dropout pada beberapa course seperti Management Evening (136) dan Nursing (118)**, **dominan mahasiswa perempuan (64,8% dari total)**, dan **mayoritas mahasiswa berusia muda, dengan 84% berusia 18-21 tahun**. Institusi dapat menggunakan data ini untuk meningkatkan strategi retensi, memperkuat dukungan akademik bagi course dengan risiko tinggi, serta mengeksplorasi preferensi pendidikan berdasarkan gender.

## Menjalankan Sistem Machine Learning

Langkah-langkah untuk menjalankan sistem machine learning melalui dashboard Streamlit adalah sebagai berikut:

1. **Buka Streamlit Dashboard**  
   Akses dashboard melalui link berikut: [Example Streamlit](https://app-prediction-dashboard-for-student-status-bjeylyuhper3sltxt8.streamlit.app/). Tunggu beberapa saat hingga halaman sepenuhnya ter-load.

2. **Navigasi Menu**  
   Setelah halaman ter-load, perhatikan berbagai menu yang ada. Pada sidebar, kamu dapat membaca informasi tentang diri saya serta penjelasan mengenai dashboard.  

   Di halaman utama, terdapat 3 menu utama yang bisa dipilih:
   - 🏡 **Home**  
   - 🔎 **Predict Data**  
   - 📃 **Download Data**

3. **Download Data**  
   Jika kamu belum memiliki data untuk diprediksi, pergi ke menu **📃 Download Data** untuk mengunduh data yang dibutuhkan.

4. **Predict Data**  
   Setelah mengunduh data, atau jika sudah memiliki data, pergi ke menu **🔎 Predict Data**. Pilih model yang sesuai dengan kebutuhanmu dengan memperhatikan detail model yang tersedia.

5. **Upload Data untuk Prediksi**  
   Setelah memilih model, unggah data yang telah diunduh atau data yang sudah kamu miliki ke dalam file uploader yang tersedia. Sistem akan secara otomatis memproses dan memprediksi data tersebut.

6. **Download Dataset Hasil Prediksi**  
   Setelah proses prediksi selesai, kamu dapat mengunduh dataset hasil prediksi yang telah diolah oleh sistem.

Dengan mengikuti langkah-langkah di atas, kamu bisa dengan mudah memanfaatkan sistem machine learning yang tersedia pada dashboard Streamlit untuk melakukan prediksi data.

## Conclusion

Proyek ini bertujuan untuk mengatasi permasalahan tingginya angka dropout di Jaya Jaya Institut dengan pendekatan berbasis data. Melalui kombinasi **dashboard analitik**, **model machine learning**, dan **aplikasi Streamlit**, institusi kini memiliki alat yang lebih canggih dan akurat untuk mengidentifikasi mahasiswa berisiko dropout serta menerapkan intervensi yang tepat waktu.

Berdasarkan hasil analisis data dan implementasi model prediktif, ditemukan beberapa temuan penting:
1. **Faktor utama yang mempengaruhi dropout** termasuk program studi tertentu (seperti Management Evening dan Nursing), distribusi gender, serta status sosial-ekonomi mahasiswa.
2. **Mahasiswa dengan beasiswa cenderung memiliki tingkat kelulusan lebih tinggi**, menunjukkan bahwa dukungan finansial memainkan peran penting dalam keberhasilan akademik.
3. **Sebagian besar mahasiswa yang dropout berusia antara 18-21 tahun**, mengindikasikan bahwa periode awal perkuliahan adalah tahap kritis yang memerlukan intervensi lebih intensif.
4. **Dashboard analitik** memberikan pemahaman mendalam tentang performa mahasiswa dan tren akademik, memungkinkan pengambilan keputusan yang lebih tepat berbasis data.
5. **Model machine learning** memiliki akurasi yang cukup tinggi dalam memprediksi status mahasiswa, yang dapat digunakan untuk mengoptimalkan kebijakan akademik dan dukungan mahasiswa.

Dengan adanya sistem ini, Jaya Jaya Institut dapat mengembangkan strategi intervensi yang lebih proaktif dan berbasis bukti untuk menurunkan angka dropout, meningkatkan tingkat kelulusan, dan memperbaiki reputasi institusi secara keseluruhan.

### Rekomendasi Action Items
Agar proyek ini memberikan dampak maksimal, berikut beberapa rekomendasi yang dapat dilakukan oleh Jaya Jaya Institut:

1. **Meningkatkan Program Mentorship dan Bimbingan Akademik**
   Institusi perlu menyediakan mentor atau tutor dari dosen senior dan mahasiswa tingkat akhir bagi mahasiswa berisiko dropout. Sesi konsultasi rutin dapat diterapkan untuk membantu mahasiswa beradaptasi. Implementasi nyata meliputi pembentukan kelompok mentoring mingguan, pengembangan platform online untuk konsultasi, dan chatbot AI untuk bimbingan akademik.

2. **Pengembangan Sistem Peringatan Dini**
   Sistem ini memberikan notifikasi otomatis kepada dosen dan staf akademik terkait mahasiswa berisiko dropout berdasarkan performa akademik dan kehadiran. Langkah konkret mencakup integrasi model prediksi ke dalam dashboard akademik, pengiriman peringatan melalui email/SMS, dan penyediaan sesi bimbingan wajib bagi mahasiswa yang terdeteksi berisiko.

3. **Peningkatan Dukungan Finansial dan Beasiswa**
   Perluasan program beasiswa dan skema bantuan finansial dapat membantu menekan angka dropout. Implementasi nyata mencakup peningkatan kuota beasiswa, pengembangan sistem pinjaman pendidikan dengan cicilan ringan, serta peluang kerja paruh waktu di kampus seperti asisten penelitian dan dosen.

4. **Optimalisasi Penggunaan Dashboard dan Data Analitik**
   Dashboard harus dimanfaatkan secara maksimal untuk pengambilan keputusan berbasis data. Dosen dan staf akademik perlu mendapatkan pelatihan rutin dalam analisis data. Langkah konkret meliputi workshop pelatihan, dashboard yang lebih interaktif dengan rekomendasi otomatis, serta laporan bulanan untuk manajemen.

5. **Evaluasi dan Pengembangan Lebih Lanjut**
   Evaluasi berkala diperlukan untuk memastikan efektivitas sistem. Model machine learning harus terus dikembangkan dengan mempertimbangkan faktor psikologis dan motivasi mahasiswa. Implementasi nyata meliputi survei kepuasan mahasiswa, pembaruan model prediksi setiap semester, serta pengembangan fitur analisis sentimen dari umpan balik mahasiswa.

Dengan menerapkan rekomendasi ini, Jaya Jaya Institut dapat meningkatkan kualitas pendidikan, menekan angka dropout, dan menciptakan lingkungan akademik yang lebih inklusif serta mendukung kesuksesan mahasiswa.