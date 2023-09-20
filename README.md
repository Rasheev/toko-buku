# toko-buku

## Tautan Aplikasi Adaptable
[Klik disini](https://rasheev-tokobuku.adaptable.app)

## Checklists
- [x] Membuat sebuah proyek Django baru.
**Langkah-langkah:**
1. Membuat repositori baru `toko-buku` dan direktori baru `toko_buku`
2. Membuka *terminal* atau *command prompt* pada direktori tersebut lalu menggunakan perintah `git setup`
3. Menggunakan perintah `python.exe -m venv env`
4. Mengaktivasi *virtual environment* menggunakan perintah `env\Scripts\activate.bat`
5. Meng-*install* **django** menggunakan perintah `pip install django`
6. Menggunakan perintah `django-admin startproject toko_buku .` untuk membuat direktori proyek menggunakan template dari django

- [x] Membuat aplikasi dengan nama `main` pada proyek tersebut.
**Langkah-langkah:**
1. Menggunakan perintah `django-admin startapp main` pada direktori utama `toko_buku`

- [x] Melakukan *routing* pada proyek agar dapat menjalankan aplikasi `main`.
**Langkah-langkah:**
1. Buka `settings.py` dalam direktori proyek `toko_buku`
2. Menambahkan `main` (setelah koma) dalam bagian list `INSTALLED_APPS`

- [x] Membuat model pada aplikasi `main` dengan nama `Item` ...

- [x] Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
**Langkah-langkah:**
1. Membuat fungsi `show_main` dalam `views.py` seperti berikut
```python
from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Rashif Aunur Rasyid',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
```
2. Menambahkan direktori `templates` didalam direktori `main`
3. Menambahkan file `main.html` dimana nama aplikasi, beserta nama dan kelas akan ditampilkan

- [x] Membuat sebuah *routing* pada `urls.py` aplikasi main untuk memetakan fungsi yang telah dibuat pada `views.py`.
**Langkah-langkah:**
1. Menggunakan potongan *code* berikut untuk menghasilkan *url pattern*
```python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name="show_main"),
]
```
2. Pada `views.py` proyek, menggunakan potongan *code* berikut agar *url pattern* yang telah dibuat diatas dapat digunakan oleh proyek
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
]
```

- [x] Melakukan *deployment* ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
**Langkah-langkah:**
1. Pada Adaptable, menggunakan `Python App Template` dan *database type* `PostgreSQL`
2. Pada bagian *template settings*, pilih `python version 3.11` (karena saya menggunakan python 3.11.x) dan pada *Start Command* gunakan perintah `python manage.py migrate && gunicorn toko_buku.wsgi`

- [x] Membuat sebuah `README.md` yang berisi tautan menuju aplikasi Adaptable yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    - sudah tertulis diatas
2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.
    - 
3. Jelaskan mengapa kita menggunakan ***virtual environment***? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan ***virtual environment***?
    - Untuk mengisolasi/memisahkan 
4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
    - MVC adalah Model-View-Controller yang merupakan pola pemrograman berbasis platform yang paling umum dengan menggunakan Controller sebagai
    - MVT adalah Model-View-Template merupakan turunan dari MVC, perbedaannya adalah menggunakan Template sebagai
    - MVVC adalah Model-View-ViewController juga merupakan turunan dari MVC, perbedaannya adalah menggunakan ViewController sebagai

---

# Tugas 3: Implementasi Form dan Data Delivery pada Django
## Checklist:
- [x] Membuat input `form` untuk menambahkan objek model pada app sebelumnya
- [x] Tambahkan 5 fungsi `views` untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML _by ID_, dan JSON _by ID_.
- [x] Membuat routing URL untuk masing-masing `views` yang telah ditambahkan pada poin 2.
- [x] Menjawab beberapa pertanyaan berikut pada `README.md` pada _root folder_.
- [x] Mengakses kelima URL di poin 2 menggunakan Postman, membuat _screenshoot_ dari hasil akses URL pada Postman, dan menambahkannya ke dalam `README.md`.
- [] Melakukan `add`-`commit`-`push` ke GitHub.


#### Pertanyaan:
- [] apa perbedaan antara form `POST` dan form `GET` dalam Django?
    - 
- [] Apa perbedaan utama antara XML, JSON, dan HTMl dalam konteks pengiriman data?
    - 
- [] Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
    - 
- [] Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara _step-by-step_ (bukan hanya sekadar mengikuti tutorial).
    1. 


#### Screenshot Postman:
1. HTML
    - ![Postman - HTML](/assets/img/Bukti%20Postman%20-%20HTML.png)
2. XML
    - ![Postman - XML](/assets/img/Bukti%20Postman%20-%20XML.png)
3. JSON
    - ![Postman - JSON](/assets/img/Bukti%20Postman%20-%20JSON.png)
4. XML by id
    - ![Postman - XML by id](/assets/img/Bukti%20Postman%20-%20XML%20by%20id.png)
5. JSOn by id
    - ![Postman - JSON by id](/assets/img/Bukti%20Postman%20-%20JSON%20by%20id.png)