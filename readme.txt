🚀 1LP Programming Language Compiler
Proyek Akhir Mata Kuliah Teknik Kompilasi Dosen: Sulistyo Puspitodjati

📝 Deskripsi Proyek
Proyek ini merupakan implementasi compiler sederhana (interpreter) untuk bahasa pemrograman kustom bernama "1LP". Compiler ini dibangun menggunakan bahasa Python dari nol (from scratch) tanpa menggunakan library eksternal seperti PLY atau Yacc.

Compiler ini menggunakan pendekatan Top-Down Parsing (LL(1)) dan dilengkapi dengan:

Lexical Analysis (Scanner) menggunakan Regular Expression.

Syntax Analysis (Parser) menggunakan metode Recursive Descent.

Semantic Analysis untuk manajemen memori (Symbol Table) dan evaluasi ekspresi aritmatika.

Error Recovery dengan pendekatan Panic Mode (sinkronisasi token).

👥 Informasi Kelompok
Kelas: 4IA04 Nama Anggota:

* Miskah Nurzakwan W (5042283)
* Dio Adelioya Putra (50422434)
* Pasya Shafaa Aaqila (51422281)
* Muhammad Alfian Rizki R (50422934)
* Muhammad Muhsin Azzam (51422095)

📂 Struktur Folder
Plaintext

Compiler_1LP_KelompokPy/
│
├── src/                  <-- Source Code Utama
│   ├── lexer.py          # Implementasi Scanner (Lexical)
│   ├── parser.py         # Implementasi Parser & Semantik
│   └── main.py           # Entry point untuk menjalankan compiler
│
├── tests/                <-- Contoh file kode 1LP (.txt)
│   ├── valid_code.txt    # Contoh kode yang berhasil dijalankan
│   ├── error_syntax.txt  # Contoh kode dengan kesalahan penulisan
│   └── error_semantic.txt# Contoh kode dengan kesalahan logika variabel
│
└── README.txt            # Dokumentasi proyek (file ini)
🛠️ Spesifikasi Teknis (Implementasi)
1. Tata Bahasa (Grammar)
Tata bahasa 1LP telah dimodifikasi menjadi bentuk LL(1) yang tidak ambigu, tidak mengandung left-recursion, dan tidak memiliki left-factoring.

Start Symbol: Stm

Operator: Penjumlahan (+), Pengurangan (-), Perkalian (*), Pembagian (/).

Fitur Unik: Mendukung assignment variabel, fungsi print, dan ekspresi bersarang (Stm, Exp).

2. Scanner (Lexical)
Mengenali token: ID, NUM, ASSIGN (:=), PRINT, SEMI (;), COMMA (,), LPAREN, RPAREN, serta operator matematika.

3. Analisa Semantik
Symbol Table: Menggunakan dictionary untuk menyimpan nilai variabel selama program berjalan.

Validasi: Mengecek variabel yang belum didefinisikan (undeclared variable).

Prioritas Operator: Menangani urutan operasi matematika (perkalian/pembagian sebelum penjumlahan).

🚀 Cara Menjalankan Program
Prasyarat:
Pastikan komputer Anda sudah terpasang Python 3.

Langkah-langkah:
Buka terminal atau Command Prompt.

Masuk ke folder proyek:

Bash

cd "C:/Lokasi/Folder/Proyek/Compiler_1LP_KelompokPy"
Jalankan salah satu perintah berikut untuk menguji:

A. Menguji Kode Valid:

Bash

python src/main.py tests/valid_code.txt
Ekspektasi: Program mencetak hasil perhitungan ke layar dan menampilkan Symbol Table.

B. Menguji Error Sintaks (Lupa Titik Koma):

Bash

python src/main.py tests/error_syntax.txt
Ekspektasi: Muncul pesan error [Syntax Error] sisa input terdeteksi.

C. Menguji Error Semantik (Variabel Tak Dikenal):

Bash

python src/main.py tests/error_semantic.txt
Ekspektasi: Muncul pesan error [Semantic Error] variabel belum didefinisikan.

📊 Contoh Hasil Output Valid
Jika menjalankan valid_code.txt, output akan terlihat seperti ini:

Plaintext

[SOURCE CODE]:
x := 10;
y := 5;
z := x + y * 2;
print(z, x);

[INFO] Parsing Selesai. Program Valid.
--> OUTPUT LAYAR: [20, 10]
[MEMORY DUMP] Symbol Table: {'x': 10, 'y': 5, 'z': 20}
