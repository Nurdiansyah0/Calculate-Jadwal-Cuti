from datetime import datetime, timedelta

def hitung_cuti(jadwal, tanggal_mulai_cuti, jumlah_hari_cuti):
    tanggal_cuti = []
    jumlah_cuti = 0

    for tanggal, nama_hari, shift in jadwal:
        if tanggal >= tanggal_mulai_cuti and jumlah_cuti < jumlah_hari_cuti:
            if shift in ["Pagi", "Malam"]:  # Hanya hitung hari kerja
                tanggal_cuti.append(tanggal)
                jumlah_cuti += 1

    return tanggal_cuti