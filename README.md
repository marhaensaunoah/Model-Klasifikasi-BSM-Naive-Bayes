# Sistem Klasifikasi Penerima BSM Menggunakan Naive Bayes

Aplikasi web berbasis **Streamlit** untuk melakukan klasifikasi penerima **BSM (Bantuan Siswa Miskin)** menggunakan algoritma **Gaussian Naive Bayes**. Sistem ini mendukung proses upload dataset, preprocessing, edit data, visualisasi, training model, evaluasi, prediksi data baru, dan export hasil ke Excel.

## Ringkasan Project

Project ini dibuat untuk membantu proses analisis dan klasifikasi data penerima BSM secara lebih terstruktur. Model menggunakan pendekatan machine learning berbasis probabilitas dengan algoritma **Gaussian Naive Bayes**.

Aplikasi ini cocok digunakan untuk kebutuhan akademik, penelitian, atau demonstrasi sistem klasifikasi sederhana berbasis data tabular.

## Fitur Utama

- Upload dataset dalam format Excel `.xlsx`
- Download template dataset BSM
- Preprocessing data tanpa data leakage
- Split data training dan testing
- Encoding data kategorikal
- Normalisasi pendapatan menggunakan Z-Score
- Training model Gaussian Naive Bayes
- Evaluasi model dengan akurasi, precision, recall, F1-score, dan confusion matrix
- Visualisasi data interaktif menggunakan Plotly
- Edit dataset langsung dari aplikasi
- Tambah data baru
- Hapus data
- Prediksi manual untuk satu data siswa
- Prediksi massal dari file Excel
- Export hasil preprocessing, normalisasi, ringkasan model, dan hasil prediksi ke Excel
- Tampilan dashboard custom menggunakan CSS terpisah

## Teknologi yang Digunakan

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Plotly
- OpenPyXL

## Struktur File

```text
project/
├── app.py
├── styles.py
├── requirements.txt
└── README.md
```

Keterangan:

- `app.py` berisi kode utama aplikasi Streamlit, preprocessing, training model, evaluasi, prediksi, dan export.
- `styles.py` berisi custom CSS dan konfigurasi tampilan dashboard.
- `requirements.txt` berisi daftar library Python yang dibutuhkan.
- `README.md` berisi dokumentasi project.

## Instalasi

### 1. Clone atau buka folder project

```bash
cd nama-folder-project
```

### 2. Buat virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Menjalankan Aplikasi

Jalankan perintah berikut di terminal:

```bash
streamlit run app.py
```

Setelah itu aplikasi akan terbuka otomatis di browser. Jika tidak terbuka, buka alamat lokal yang muncul di terminal, biasanya:

```text
http://localhost:8501
```

## Format Dataset

Dataset yang digunakan harus berupa file Excel `.xlsx`.

Kolom dataset yang disarankan:

| Kolom | Keterangan |
|---|---|
| NO | Nomor data |
| NAMA PESERTA DIDIK | Nama siswa |
| SEKOLAH | Nama sekolah |
| KELAS | Kelas siswa |
| NIK | Nomor Induk Kependudukan |
| NISN | Nomor Induk Siswa Nasional |
| NAMA AYAH/IBU | Nama orang tua/wali |
| KECAMATAN | Kecamatan tempat tinggal |
| BESARAN BIAYA | Besaran biaya bantuan |
| PENDAPATAN ORANG TUA | Pendapatan orang tua |
| PEKERJAAN ORANG TUA | Pekerjaan orang tua |
| JUMLAH TANGGUNGAN | Jumlah tanggungan keluarga |
| STATUS RUMAH | Status kepemilikan rumah |
| LABEL | Target klasifikasi, berisi `Ya` atau `Tidak` |

Nilai pada kolom `LABEL` digunakan sebagai target klasifikasi:

- `Ya` berarti siswa termasuk penerima BSM
- `Tidak` berarti siswa tidak termasuk penerima BSM

## Fitur yang Digunakan Model

Model menggunakan 5 fitur utama:

| Fitur | Penjelasan |
|---|---|
| KELAS_NUM | Angka kelas siswa |
| PENDAPATAN_ZSCORE | Pendapatan orang tua setelah normalisasi Z-Score |
| PEKERJAAN ORANG TUA_ENC | Hasil encoding pekerjaan orang tua |
| JUMLAH TANGGUNGAN | Jumlah tanggungan keluarga |
| STATUS RUMAH_ENC | Hasil encoding status rumah |

## Alur Penggunaan Aplikasi

1. Buka aplikasi dengan perintah `streamlit run app.py`
2. Masuk ke menu **Data & Preprocessing**
3. Download template dataset jika belum memiliki format data
4. Upload dataset Excel
5. Atur rasio data testing pada sidebar
6. Jalankan preprocessing
7. Cek hasil preprocessing dan visualisasi data
8. Masuk ke menu **Training Model**
9. Jalankan training model Gaussian Naive Bayes
10. Buka menu **Evaluasi** untuk melihat performa model
11. Buka menu **Hasil Prediksi** untuk melihat hasil prediksi data testing
12. Gunakan menu **Prediksi Data Baru** untuk prediksi manual atau prediksi massal
13. Gunakan menu **Export Hasil** untuk mengunduh output ke Excel

## Menu Aplikasi

### Dashboard

Menampilkan ringkasan umum data, status model, dan informasi utama aplikasi.

### Data & Preprocessing

Digunakan untuk upload dataset, download template, mengatur pembagian data training/testing, serta menjalankan proses preprocessing.

### Edit Dataset

Digunakan untuk mengedit data langsung dari tabel, menambah baris baru, menghapus data, dan menyimpan perubahan di session aplikasi.

### Visualisasi

Menampilkan grafik distribusi label, pendapatan, pekerjaan orang tua, status rumah, kelas, dan korelasi fitur.

### Training Model

Digunakan untuk melatih model Gaussian Naive Bayes berdasarkan data training.

### Evaluasi

Menampilkan classification report, akurasi training/testing, precision, recall, F1-score, confusion matrix, dan grafik evaluasi.

### Hasil Prediksi

Menampilkan tabel hasil prediksi pada data testing, termasuk actual label, predicted label, probabilitas, dan status benar/salah.

### Prediksi Data Baru

Digunakan untuk prediksi data siswa baru secara manual atau prediksi massal dari file Excel.

### Kesimpulan Hasil

Menampilkan interpretasi hasil model dan ringkasan performa klasifikasi.

### Export Hasil

Digunakan untuk mengunduh hasil preprocessing, normalisasi, ringkasan model, dan hasil prediksi dalam format Excel.

### Tentang Sistem

Menampilkan informasi teknologi, tujuan sistem, dan fitur utama aplikasi.

## Preprocessing Data

Tahapan preprocessing yang dilakukan:

1. Standarisasi nama kolom
2. Menghapus data duplikat
3. Validasi label `Ya` dan `Tidak`
4. Split data menjadi training dan testing
5. Menghitung nilai imputasi dari data training
6. Encoding pekerjaan orang tua menggunakan LabelEncoder
7. Encoding status rumah menjadi nilai numerik
8. Normalisasi pendapatan menggunakan StandardScaler
9. Transformasi data testing menggunakan parameter dari data training

Catatan penting: preprocessing dibuat dengan pendekatan **tanpa data leakage**, yaitu scaler dan encoder di-fit hanya dari data training.

## Model Machine Learning

Algoritma yang digunakan:

```text
Gaussian Naive Bayes
```

Model ini dipilih karena cocok untuk klasifikasi sederhana berbasis fitur numerik dan kategorikal yang sudah diubah menjadi numerik.

Output model meliputi:

- Prior probability
- Mean atau theta per fitur
- Variance per fitur
- Akurasi training
- Akurasi testing
- Classification report
- Confusion matrix
- Probabilitas prediksi

## Export File

Aplikasi dapat menghasilkan beberapa file Excel:

| File | Isi |
|---|---|
| `data_bsm_preprocessed.xlsx` | Data hasil preprocessing |
| `data_normalisasi_zscore.xlsx` | Hasil normalisasi pendapatan |
| `ringkasan_model_bsm.xlsx` | Ringkasan model dan metrik evaluasi |
| `hasil_prediksi_bsm.xlsx` | Hasil prediksi data testing atau batch prediction |

## Catatan Penggunaan

- Pastikan format kolom dataset sesuai template.
- Kolom `LABEL` harus berisi nilai `Ya` atau `Tidak`.
- Jangan menghapus file `styles.py` karena aplikasi mengambil fungsi styling dari file tersebut.
- Jika dataset berubah setelah edit, tambah, atau hapus data, lakukan preprocessing dan training ulang.
- Folder `__pycache__` aman dihapus karena hanya berisi cache Python.

## Troubleshooting

### Aplikasi gagal dijalankan

Pastikan dependencies sudah terinstall:

```bash
pip install -r requirements.txt
```

### Error import dari `styles.py`

Pastikan file `styles.py` berada dalam folder yang sama dengan `app.py`.

### Dataset gagal terbaca

Periksa kembali:

- Format file harus `.xlsx`
- Nama dan jumlah kolom harus sesuai template
- Kolom label harus berisi `Ya` atau `Tidak`
- Tidak ada baris kosong berlebihan di bagian atas file

### Hasil akurasi berubah setelah edit dataset

Itu normal. Perubahan jumlah data, label, dan distribusi kelas dapat memengaruhi hasil training dan evaluasi model.

## Lisensi

Project ini dibuat untuk keperluan akademik dan pembelajaran.

## Author

Dibuat sebagai project sistem klasifikasi penerima BSM menggunakan Streamlit dan Gaussian Naive Bayes.
