# DIAGNOSIS — news-image-20261123 v3 (vs live v2)

Penulis: subagent builder (Muse-build; relay Codex masih 503 per smoke 18:38 WIB).
Tanggal: 24 Nov 2026 ~18:55 WIB. Entri live v2: submission 01a20a5c,
ronde 2 rank #3.720/9.643, judge 0,540098. v1 ronde 1: #2.939/7.226,
judge 0,536337. Keduanya photo-led, layout koran front-page.

## 1. Yang saya lihat di entry.png v2 (1024×1024, dilihat langsung)

Layout: masthead serif "THE WORLD TODAY" + foto hero aula COP31 yang kosong,
headline besar "COP31 ENDS WITH NO DEAL", lalu baris NATO/jet + angka "258"
Democrats, lalu baris sport (Alcaraz, Verstappen), lalu ticker "ALSO TODAY"
satu baris di footer. Secara teknis rapi; masalahnya ada di isi dan hierarki:

### Cacat konkret

1. **Foto hero generik dan tanpa manusia/aksi.** Aula COP31 yang kosong,
   gelap, tanpa orang — tidak ada konflik, tidak ada emosi. Caption-nya
   sendiri mengaku "Illustrative photo". Pada pandangan pertama (dan judge
   membandingkan dua gambar sekilas), yang terbaca hanya "ruangan kosong
   biru gelap", bukan "perundingan iklim gagal".
2. **Foto kedua juga generik.** Dua jet tempur stok melawan langit mendung —
   tidak menunjukkan Polandia, rudal, atau NATO apa pun. Tanpa caption,
   gambar ini bisa jadi berita apa saja tentang pesawat tempur.
3. **Terlalu banyak cerita, perhatian terpecah.** 5 cerita + ticker 6 cerita
   dalam satu halaman. Judge memilih gambar yang PALING merangkum hari itu;
   v2 tidak punya satu momen dominan — COP31, Polandia, House 258, dan dua
   olahraga semuanya berebut perhatian dengan bobot hampir sama.
4. **Olahraga memakan ~15% ruang untuk berita paling ringan.** Alcaraz dan
   Verstappen adalah filler di hari ketika ada perang, COP gagal, dan
   Nvidia. Foto sport-nya pun kecil dan gelap (Alcaraz nyaris siluet,
   foto Vegas lebih menonjolkan neon daripada mobil F1).
5. **Ticker "ALSO TODAY" tidak terbaca.** Enam cerita dijejalkan dalam satu
   baris ~11 px di footer — pada 1024×1024 praktis tidak bisa dibaca, jadi
   hanya jadi derau abu-abu.
6. **Angka "258" adalah elemen terkuat kedua, tapi ceritanya terpotong.**
   Headline "DEMOCRATS TAKE THE HOUSE" bagus dan besar; deck-nya pendek dan
   oke. Ini satu-satunya blok selain COP31 yang benar-benar bekerja.
7. **Semua foto "illustrative".** Tiga foto AI/stok yang diakui bukan foto
   peristiwa. Diperbandingkan dengan entri yang gambarnya terasa seperti
   momen nyata, v2 terasa seperti mockup koran, bukan "hari itu dalam
   gambar".

### Yang bekerja di v2 (dipertahankan semangatnya, bukan bentuknya)

- Headline utama besar dan terbaca ("COP31 ENDS WITH NO DEAL").
- Kicker merah + angka besar "258" sebagai jangkar visual kedua.
- Deck satu-dua baris yang bisa dipahami tanpa feed.

## 2. Apa yang judge butuhkan

Judge membandingkan dua gambar dan memilih yang paling merangkum berita
23 November 2026 — dan judge TIDAK punya news feed. Artinya gambar harus
bisa dipahami sendiri oleh orang yang tidak membaca berita hari itu:
satu momen dominan yang langsung terbaca, plus 3–4 cerita besar dengan
headline yang cukup besar untuk dibaca tanpa zoom. Entri yang menyebar ke
6–11 cerita kecil kalah dari entri yang menyampaikan 4–5 cerita besar
dengan jelas.

## 3. Perubahan desain terbesar untuk v3 (2–3)

1. **Satu momen dominan yang dramatis, bukan aula kosong.** Hero v3 adalah
   adegan laut malam: kapal perang Rusia dihantam drone laut Ukraina di
   lepas Libya — ledakan, kapal siluet, drone dengan jejak ombak. Ini
   cerita paling visual hari itu dan langsung terbaca sebagai "perang di
   laut", tanpa perlu caption. Gaya berubah total: dari koran krem-serif
   menjadi poster gelap "breaking news" (hitam, merah, kuning).
2. **Kurangi dari 5 cerita + ticker menjadi 5 cerita saja, tanpa sport,
   tanpa ticker.** Alcaraz/Verstappen dan ticker "ALSO TODAY" dibuang.
   Empat blok cerita di bawah hero, masing-masing satu baris headline
   BESAR (40 px) + satu baris deck — COP31, Nvidia/Huang, Democrats 258,
   sanksi Iran. Sedikit cerita, semuanya terbaca.
3. **Hierarki satu sumbu.** v2 punya tiga baris foto dengan bobot mirip
   (hero, jet, sport). v3 punya satu sumbu vertikal tegas: hero 50% →
   empat baris cerita seragam → footer sumber. Mata pembaca tidak perlu
   memilih-milih; urutan baca sudah ditentukan layout.

## 4. Berita 23 November 2026 yang dipakai v3 (dari pencarian sendiri)

- **Hero — Ukraina:** tujuh drone laut Ukraina menenggelamkan korvet Rusia
  Merkury di lepas Libya dan menghantam kapal kargo Angara (Zelenskyy);
  NATO rapat darurat soal serangan ke Polandia.
- **COP31:** perundingan iklim di Antalya berakhir tanpa kesepakatan —
  pertama sejak 2009 — setelah draf akhir menghapus semua penyebutan
  bahan bakar fosil; UE menolak teks itu.
- **Nvidia:** dewan mengembalikan Jensen Huang sebagai CEO setelah
  intervensi Trump; saham melonjak ~30% setelah minggu terburuk (-23%).
- **AS:** Demokrat mencapai 258 kursi DPR — mayoritas terbesar sejak 1992.
- **Iran:** AS menjatuhkan sanksi baru ke jaringan shadow banking Iran;
  Trump menyebut Iran meluncurkan minggu rudal terberat dalam setahun.

Sumber: Reuters/AP/CNN/BBC via pencarian web 24 Nov 2026 (dailysummaryof,
BusinessWorld, Broadcast Prism, Standard Topic).
