# toko-buku

## Tautan Aplikasi Adaptable
[title](https://rasheev-tokobuku.adaptable.app)

## Checklists
- [x] Membuat sebuah proyek Django baru.
        **Langkah-Langkah:**
        - Membuat repositori baru `toko-buku` dan direktori baru `toko_buku`
        - Membuka *terminal* atau *command prompt* pada direktori tersebut lalu menggunakan perintah `git setup`
        - Menggunakan perintah `python.exe -m venv env`
        - Mengaktivasi *virtual environment* menggunakan perintah `env\Scripts\activate.bat`
        - Meng-*install* **django** menggunakan perintah `pip install django`
        - Menggunakan perintah `django-admin startproject toko_buku .` untuk membuat direktori proyek menggunakan template dari django

- [x] Membuat aplikasi dengan nama `main` pada proyek tersebut.
        **Langkah-Langkah:**
        - Menggunakan perintah `django-admin startapp main` pada direktori utama `toko_buku`

- [x] Melakukan *routing* pada proyek agar dapat menjalankan aplikasi `main`.

- [x] Membuat model pada aplikasi `main` dengan nama `Item` ...

- [x] Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.

- [x] Membuat sebuah *routing* pada `urls.py` aplikasi main untuk memetakan fungsi yang telah dibuat pada `views.py`.

- [x] Melakukan *deployment* ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.