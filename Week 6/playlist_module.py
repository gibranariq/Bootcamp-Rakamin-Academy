playlist = []

def add_song(nama_lagu):
    """
    Fungsi untuk menambahkan lagu ke dalam playlist.

    nama_lagu (str) -> nama-nama lagu yang akan ditambahkan

    """

    if nama_lagu:
        playlist.append(nama_lagu)
        print(f"lagu '{nama_lagu}' berhasil ditambahkan")
    else:
        print(f"Nama lagu tidak boleh kosong")


def remove_song(nama_lagu):
    """
    Fungsi untuk meremove lagu yang ada di dalam playlist
    
    nama_lagu (str) -> nama-nama lagu yang akan ditambahkan
    """

    try:
        playlist.remove(nama_lagu)
        print(f"Lagu '{nama_lagu}' berhasil dihapus")
    except:
        print(f"Lagu '{nama_lagu}' tidak ditemukan dalam playlist")

def show_playlist():
    """
    Fungsi untuk menampilkan isi playlist

    """

    if not playlist:
        print("Playlist kosong")
    else:
        print("Daftar lagu dalam playlist:\n")
        # for index, song in enumerate(playlist, start=1):
        #     print(f"{index}. {song}")
        index = 1
        for song in playlist:
            print(f"{index}. {song}")
            index += 1


def play_song(index):
    """
    Fungsi untuk memplay lagu

    index (int) -> index lagu yang ingin diplay (dimulai dari 1)

    """
    try:
        print(f"Memutar lagu: {playlist[index - 1]}")
    except IndexError:
        print("Index lagu tidak valid.")
    except TypeError:
        print("Index harus berupa angka.")

def shuffle_playlist():
    """
    Menggunakan algoritma shuffle sederhana berbasis iterasi.

    """
    if not playlist:
        print("Playlist kosong. Tidak ada lagu yang bisa diputar.")
        return

    # Buat salinan playlist
    temp_playlist = playlist[:]

    # Shuffle manual menggunakan algoritma pertukaran
    for i in range(len(temp_playlist)):
        # Cari indeks random dari i sampai akhir
        j = (i * 3 + 7) % len(temp_playlist)  
        # Tukar lagu di posisi i dan j
        temp_playlist[i], temp_playlist[j] = temp_playlist[j], temp_playlist[i]

    print("Memutar lagu secara acak:")
    print
    for song in temp_playlist:
        print(f"▶️ {song}")


print("""
🎵 Playlist Module 🎵

Cara Penggunaan:

1. Tambah lagu ke playlist:
   > pm.add_song("Judul Lagu")
      
2. Tampilkan seluruh playlist:
   > pm.show_playlist()

3. Hapus lagu dari playlist:
   > pm.remove_song("Judul Lagu")

4. Putar lagu berdasarkan urutan:
   > pm.play_song(nomor)

5. Putar semua lagu secara acak:
   > pm.shuffle_playlist()

""")

