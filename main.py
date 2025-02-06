import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
from jadwal import buat_jadwal
from cuti import hitung_cuti
TK_SILENCE_DEPRECATION =1

def tampilkan_jadwal():
    try:
        # Ambil input dari GUI
        tanggal_str = ent_tanggal_mulai.get()
        nama_hari = cb_hari_pertama.get()
        tanggal_mulai = datetime.strptime(tanggal_str, "%d/%m/%Y")

        # Generate jadwal
        jadwal = buat_jadwal(tanggal_mulai, nama_hari)

        # Bersihkan output sebelumnya
        text_output.delete("1.0", tk.END)

        # Tampilkan jadwal di GUI
        text_output.insert(tk.END, "\nJadwal Dinas Anda:\n")
        for tanggal, nama_hari, shift in jadwal:
            text_output.insert(tk.END, f"{tanggal.strftime('%d %B %Y')} - {nama_hari} - {shift}\n")

    except ValueError:
        # Tangani kesalahan input
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, "Format tanggal salah. Gunakan format: Tanggal/Bulan/Tahun (contoh: 01/01/2024)")

def tampilkan_cuti():
    try:
        # Ambil input dari GUI
        tanggal_str = ent_tanggal_mulai.get()
        nama_hari = cb_hari_pertama.get()
        tanggal_mulai = datetime.strptime(tanggal_str, "%d/%m/%Y")
        
        tanggal_cuti_str = ent_tanggal_cuti.get()
        tanggal_mulai_cuti = datetime.strptime(tanggal_cuti_str, "%d/%m/%Y")
        jumlah_hari_cuti = int(ent_jumlah_cuti.get())

        # Generate jadwal dan hitung cuti
        jadwal = buat_jadwal(tanggal_mulai, nama_hari)
        tanggal_cuti = hitung_cuti(jadwal, tanggal_mulai_cuti, jumlah_hari_cuti)

        # Bersihkan output sebelumnya
        text_output.delete("1.0", tk.END)

        # Tampilkan hasil cuti di GUI
        text_output.insert(tk.END, "\nHari Cuti Anda:\n")
        for tanggal in tanggal_cuti:
            text_output.insert(tk.END, f"{tanggal.strftime('%d %B %Y')}\n")

        total_hari_libur = len(tanggal_cuti)
        text_output.insert(tk.END, f"\nTotal hari cuti yang diambil: {total_hari_libur} hari.\n")

        # Mencari tanggal masuk kerja kembali
        tanggal_cuti_terakhir = tanggal_cuti[-1] 
        tanggal_kembali = tanggal_cuti_terakhir + timedelta(days=1)
        while tanggal_kembali.strftime('%A') in ["Saturday", "Sunday"]:
            tanggal_kembali += timedelta(days=1)

        text_output.insert(tk.END, f"\nJadwal masuk kerja kembali: {tanggal_kembali.strftime('%d %B %Y')}")

    except ValueError:
        # Tangani kesalahan input
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, "Format tanggal salah. Gunakan format: Tanggal/Bulan/Tahun (contoh: 01/01/2024)")


# --- GUI setup ---
window = tk.Tk()
window.title("Kalkulator Cuti")

# --- Frame Input ---
frame_input = ttk.Frame(window)
frame_input.pack(padx=10, pady=10)

lbl_tanggal_mulai = ttk.Label(frame_input, text="Tanggal Kerja Pertama (dd/mm/yyyy):")
lbl_tanggal_mulai.grid(row=0, column=0, sticky=tk.W)
ent_tanggal_mulai = ttk.Entry(frame_input)
ent_tanggal_mulai.grid(row=0, column=1, sticky=tk.E)

lbl_hari_pertama = ttk.Label(frame_input, text="Hari Kerja Pertama:")
lbl_hari_pertama.grid(row=1, column=0, sticky=tk.W)
cb_hari_pertama = ttk.Combobox(frame_input, values=["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"])
cb_hari_pertama.grid(row=1, column=1, sticky=tk.E)

lbl_tanggal_cuti = ttk.Label(frame_input, text="Tanggal Mulai Cuti (dd/mm/yyyy):")
lbl_tanggal_cuti.grid(row=2, column=0, sticky=tk.W)
ent_tanggal_cuti = ttk.Entry(frame_input)
ent_tanggal_cuti.grid(row=2, column=1, sticky=tk.E)

lbl_jumlah_cuti = ttk.Label(frame_input, text="Jumlah Hari Cuti:")
lbl_jumlah_cuti.grid(row=3, column=0, sticky=tk.W)
ent_jumlah_cuti = ttk.Entry(frame_input)
ent_jumlah_cuti.grid(row=3, column=1, sticky=tk.E)

# --- Tombol ---
btn_jadwal = ttk.Button(window, text="Tampilkan Jadwal", command=tampilkan_jadwal)
btn_jadwal.pack(pady=5)

btn_cuti = ttk.Button(window, text="Hitung Cuti", command=tampilkan_cuti)
btn_cuti.pack(pady=5)

# --- Output ---
text_output = tk.Text(window, wrap=tk.WORD)
text_output.pack(padx=10, pady=10)
window.mainloop()