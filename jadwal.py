from datetime import datetime, timedelta

def buat_jadwal(tanggal_mulai, nama_hari_pertama, hari_kerja=4, hari_libur=2):
    jadwal = []
    tanggal_sekarang = tanggal_mulai

    # Tentukan nama hari untuk setiap tanggal
    nama_hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    
    # Tentukan indeks hari pertama
    indeks_hari_pertama = nama_hari.index(nama_hari_pertama)

    # Buat jadwal untuk 1 bulan
    while tanggal_sekarang < tanggal_mulai + timedelta(days=30):
        for i in range(hari_kerja):
            # Tentukan nama hari untuk tanggal sekarang
            nama_hari_sekarang = nama_hari[(indeks_hari_pertama + i) % 7]
            jenis_shift = "Pagi" if i < 2 else "Malam"
            jadwal.append((tanggal_sekarang, nama_hari_sekarang, jenis_shift))
            tanggal_sekarang += timedelta(days=1)

        # Tambahkan hari libur
        for _ in range(hari_libur):
            nama_hari_sekarang = nama_hari[(indeks_hari_pertama + hari_kerja) % 7]
            jadwal.append((tanggal_sekarang, nama_hari_sekarang, "Libur"))
            tanggal_sekarang += timedelta(days=1)
            indeks_hari_pertama += 1

        # Perbarui indeks untuk siklus berikutnya
        indeks_hari_pertama = (indeks_hari_pertama + hari_kerja + hari_libur) % 7

    return jadwal