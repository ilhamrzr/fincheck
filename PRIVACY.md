# PRIVACY & LEGAL NOTICE

FINCHECK — Financial Intelligence Account Checker

Penting: Bacalah dokumen ini sebelum menggunakan Fincheck. Tool ini mengirimkan data ke layanan pihak ketiga dan dapat memproses data pribadi. Penggunaan yang tidak patuh dapat menimbulkan risiko hukum dan etika.

---

## Ringkasan singkat

Fincheck adalah alat CLI untuk memeriksa validitas rekening bank dan nomor e‑wallet dengan menggunakan API eksternal. Tool ini dikirimkan "as‑is" untuk tujuan edukasi, testing, dan penggunaan internal. Pengguna bertanggung jawab atas kepatuhan hukum, perlindungan data, dan etika penggunaan.

---

## Endpoint eksternal yang digunakan

Fincheck mengirimkan permintaan ke endpoint berikut (atau mirror terkait):

- https://rfpdev.site
- https://rfpdevid.site
- https://rfpdev.me

Pastikan Anda memahami kebijakan privasi dan Terms of Service pada penyedia API tersebut sebelum menggunakan Fincheck.

---

## Data yang dikirim

Tergantung pada mode, Fincheck akan mengirimkan beberapa field berikut:

- E‑wallet: `phone_number`, `ewallet_code`, `api_key` (jika disertakan)
- Bank: `account_number`, `bank_code`, `api_key` (jika disertakan)

Catatan: `api_key` bersifat sensitif. Hindari mengeksposnya di logs, file, atau history shell.

---

## Pedoman Legal & Persetujuan

- Jangan proses data milik orang lain tanpa persetujuan eksplisit dari pemilik data atau dasar hukum yang sesuai.
- Untuk organisasi: dokumentasikan alasan pemrosesan, tujuan, lama penyimpanan, serta mekanisme penghapusan.
- Bulk processing (mode `bulk`) berisiko paling tinggi — hanya gunakan untuk data yang Anda berhak proses.

---

## Penanganan API key (praktik aman)

- Jangan mengetik API key langsung dalam command line (menghindari tersimpan di shell history).
- Preferensi: simpan API key dalam environment variable (mis. `FINCHECK_API_KEY`) atau gunakan secret manager.
  - Contoh:
    - export FINCHECK_API_KEY="your_key_here"
    - fincheck bulk bank file.txt --api-key "$FINCHECK_API_KEY"
- Jangan sertakan API key dalam output ringkasan, file log, atau file yang disimpan tanpa enkripsi.
- Jika API key terindikasi bocor, segera rotasi/cabut key di penyedia layanan.

---

## Logging, Penyimpanan & Retensi

- Hindari menyimpan output yang mengandung data sensitif di lokasi tidak aman.
- Jika menyimpan hasil:
  - Enkripsi file output.
  - Batasi akses hanya ke pihak berwenang.
  - Terapkan kebijakan retensi (mis. hapus setelah jangka waktu tertentu).
- Gunakan `--dry-run` untuk simulasi tanpa mengirim data ke API.

---

## Bulk Mode — kehati‑hatian tambahan

- Bulk mode memproses banyak entri; pastikan:
  - Anda memiliki izin untuk setiap entri.
  - Anda memahami dan mematuhi rate limit dari penyedia API.
  - Anda tidak menyimpan API key atau data sensitif pada file output tanpa proteksi.
- Disarankan menguji pada subset kecil sebelum memproses keseluruhan file.

---

## Anonimisasi & Minimasi Data

- Hanya kirim data yang benar‑benar diperlukan.
- Jika memungkinkan, pseudonimisasi atau mask data sebelum menyimpan hasil.
- Untuk pengujian, gunakan data dummy atau `--dry-run`.

---

## Kepatuhan Hukum

Jika Anda beroperasi di yurisdiksi yang diatur:

- Pastikan ada dasar hukum untuk pemrosesan data.
- Siapkan mekanisme untuk permintaan akses atau penghapusan data (DSAR).
- Simpan catatan pemrosesan sesuai kewajiban regulasi.

Fincheck sendiri bukan layanan penyimpanan—namun data yang dihasilkan/ditulis oleh pengguna dapat memiliki kewajiban kepatuhan.

---

## Keamanan Teknis

- Jalankan di lingkungan terisolasi (virtualenv, container).
- Jangan jalankan sebagai root.
- Batasi egress network jika memungkinkan (hanya ke endpoint API yang diperlukan).
- Perbarui dependensi dan periksa kerentanan secara berkala.
- Implementasi rekomendasi teknis (retry, backoff, rate limit) adalah tanggung jawab pengguna atau maintainer.

---

## Insiden & Kebocoran

Jika terjadi indikasi kebocoran atau penyalahgunaan:

1. Segera hentikan proses yang berjalan.
2. Cabut/rotasi API key di penyedia layanan.
3. Audit output/log untuk menentukan cakupan.
4. Hubungi penyedia API jika perlu.
5. Lakukan pelaporan sesuai persyaratan regulasi lokal bila data pribadi terlibat.

---

## Disclaimer

Fincheck disediakan untuk tujuan edukasi, riset, dan penggunaan internal. Pengembang tidak bertanggung jawab atas penggunaan yang melanggar hukum, penyalahgunaan, atau kerugian yang timbul akibat penggunaan tool ini. Ini bukan nasihat hukum.
