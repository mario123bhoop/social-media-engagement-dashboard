# Social Media Engagement Dashboard

**Mata Kuliah:** Visualisasi Data  
**Program Studi:** Sistem Informasi  
**Nama:** [Isi Nama Lengkap]  
**NPM:** [Isi NPM]

Dashboard interaktif untuk mengeksplorasi interaksi dan sentimen postingan media sosial menggunakan Python, Pandas, Plotly, dan Streamlit.

## 1. Tautan penting

- **Live Dashboard:** [Isi URL Streamlit Community Cloud setelah deployment]
- **Repositori GitHub:** [Isi URL repository GitHub]
- **Sumber dataset Kaggle:** https://www.kaggle.com/datasets/subashmaster0411/social-media-engagement-dataset

> Cantumkan tautan Kaggle di atas sebagai sumber asli dataset. Jika halaman Kaggle tidak dapat diakses, periksa kembali halaman dataset sebelum pengumpulan. Jangan mengganti tautan ini dengan tautan repository sendiri.

## 2. Latar belakang

Media sosial menghasilkan data mengenai platform, waktu publikasi, lokasi, kategori topik, sentimen, dan respons pengguna. Dashboard ini dibuat untuk membantu melihat pola interaksi, membandingkan performa antarplatform, serta memahami komposisi sentimen pada dataset.

Dataset yang digunakan merupakan dataset sekunder dari Kaggle. Dataset ini bersifat **machine-generated/sintetis**, sehingga hasil analisis menggambarkan pola pada data yang tersedia dan tidak otomatis mewakili seluruh perilaku pengguna media sosial di dunia nyata.

## 3. Dataset

- Nama: Social Media Engagement Dataset
- Jumlah data sumber: 12.000 baris
- Jumlah kolom: 28
- Periode timestamp pada file: Januari–Desember 2024
- Jenis variabel: kategorikal dan numerik
- Contoh variabel: `platform`, `location`, `topic_category`, `sentiment_label`, `likes_count`, `shares_count`, `comments_count`, `impressions`, dan `engagement_rate`.

File bersih yang digunakan dashboard berada di `data/social_media_engagement_clean.csv`.

## 4. Fitur dashboard

### KPI
1. Total interaksi (likes + shares + comments).
2. Rata-rata engagement rate.
3. Total impressions.
4. Jumlah postingan setelah filter.

### Visualisasi
1. Line chart: tren likes, shares, dan comments per minggu.
2. Bar chart: rata-rata engagement rate per platform.
3. Donut chart: proporsi sentimen.
4. Scatter plot: hubungan impressions dan likes.
5. Bar chart horizontal: total interaksi per kategori topik.

### Filter interaktif
- Platform (multiselect).
- Rentang tanggal.
- Sentimen.

Semua KPI, grafik, tabel, dan insight berubah mengikuti filter yang dipilih.

## 5. Key insights

Dashboard menghitung insight secara dinamis sesuai filter. Saat menulis laporan akhir, catat 3–5 temuan yang benar-benar terlihat pada dashboard, misalnya:
- Platform dengan rata-rata engagement rate tertinggi.
- Sentimen yang paling dominan.
- Kategori topik dengan total interaksi terbesar.
- Perubahan interaksi dari minggu ke minggu.
- Pola hubungan impressions dan likes.

**Penting:** Jangan menuliskan kesimpulan angka sebelum memeriksa hasil dashboard; insight dapat berubah ketika filter berubah.

## 6. Struktur repository

```text
Social_Media_Engagement_Dashboard/
├── app.py
├── requirements.txt
├── README.md
├── data/
│   └── social_media_engagement_clean.csv
├── scripts/
│   └── clean_data.py
└── notebooks/
    └── eksplorasi_dataset.ipynb
```

## 7. Menjalankan melalui JupyterLab

1. Ekstrak ZIP proyek.
2. Buka JupyterLab dan buka folder proyek.
3. Buka Terminal di JupyterLab.
4. Buat virtual environment (opsional tetapi disarankan):

   **Windows**
   ```powershell
   py -m venv .venv
   .venv\Scripts\activate
   ```

   **macOS/Linux**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

5. Instal library:
   ```bash
   python -m pip install -r requirements.txt
   ```

6. Jalankan dashboard:
   ```bash
   streamlit run app.py
   ```

7. Browser akan membuka alamat lokal, biasanya `http://localhost:8501`.

Jika ingin mengulang proses pembersihan dari file mentah, simpan file CSV asli sebagai `data/Social Media Engagement Dataset.csv`, kemudian jalankan:
```bash
python scripts/clean_data.py
```

## 8. Mengunggah ke GitHub

1. Buat repository baru di GitHub dan pilih **Public**.
2. Beri nama misalnya `social-media-engagement-dashboard`.
3. Ekstrak ZIP dan unggah seluruh isi folder proyek (bukan file ZIP-nya) ke repository.
4. Pastikan `README.md`, `app.py`, `requirements.txt`, folder `data`, `scripts`, dan `notebooks` terlihat di halaman utama repository.
5. Buka `README.md`, klik ikon pensil (**Edit**), lalu isi nama, NPM, URL repository, dan URL Live Dashboard setelah tersedia.
6. Klik **Commit changes**.

### Cara mencantumkan tautan sumber Kaggle di README

Gunakan format Markdown berikut:
```markdown
- **Sumber Dataset:** [Social Media Engagement Dataset – Kaggle](https://www.kaggle.com/datasets/subashmaster0411/social-media-engagement-dataset)
```
Teks di dalam tanda kurung siku adalah tulisan yang terlihat; URL di dalam tanda kurung adalah alamat yang dibuka ketika tautan diklik. Tautan ini harus mengarah ke halaman dataset asli di Kaggle, bukan ke file CSV lokal.

## 9. Deploy menjadi Live Dashboard

1. Pastikan repository GitHub sudah Public dan semua file telah diunggah.
2. Buka https://share.streamlit.io/ dan masuk menggunakan akun GitHub.
3. Pilih **Create app**.
4. Pilih repository, branch (biasanya `main`), dan file utama `app.py`.
5. Klik **Deploy** dan tunggu proses instalasi selesai.
6. Salin URL aplikasi yang diberikan Streamlit.
7. Edit README, lalu ganti `[Isi URL Streamlit Community Cloud setelah deployment]` dengan URL tersebut.
8. Buka URL dari browser lain/incognito untuk memastikan dashboard dapat diakses.

## 10. Catatan analisis

Dashboard ini bersifat deskriptif. `engagement_rate` merupakan metrik historis yang berkaitan langsung dengan jumlah likes, shares, comments, dan impressions. Karena itu, dashboard tidak mengklaim bahwa metrik tersebut dapat digunakan untuk memprediksi engagement masa depan. Dataset juga bersifat sintetis, sehingga keterbatasan ini perlu disebutkan ketika mempresentasikan hasil.

## 11. Teknologi

- Python
- JupyterLab (lingkungan kerja)
- Streamlit (web dashboard)
- Pandas (pembersihan dan pengolahan data)
- Plotly (visualisasi interaktif)
- GitHub (version control dan publikasi source code)
