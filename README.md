# pythonMetaTwin

pythonMetaTwin adalah implementasi Python3 dari [MetaTwin] (https://github.com/threatexpress/metatwin) yang memungkinkan Anda menyalin metadata dan tanda tangan digital dari satu eksekusi Windows ke eksekusi lainnya menggunakan Wine pada platform non-Windows.

## Persyaratan

- Python 3.x
- Wine
- Peretas Sumber Daya
- SigThief

## Instalasi

Untuk menginstal dependensi yang diperlukan, jalankan skrip `install.sh` yang disediakan dalam repositori ini.

```bash
chmod +x install.sh
./install.sh
```

## Penggunaan

Setelah menginstal dependensi yang diperlukan, Anda dapat menjalankan skrip sebagai berikut:

```bash
python3 metatwin.py <source_file> <target_file>
<source_file> adalah jalur ke berkas yang dapat dieksekusi Windows yang ingin Anda salin metadata dan tanda tangan digitalnya.
<target_file> adalah jalur ke file yang dapat dieksekusi Windows yang ingin Anda salin metadata dan tanda tangan digitalnya.
```

Pastikan ResourceHacker.exe dan SigThief.exe terinstal dan dapat diakses di PATH sistem Anda atau direktori kerja pyMetaTwin.
