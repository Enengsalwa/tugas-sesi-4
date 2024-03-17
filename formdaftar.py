nama = input("masukan nama anda: ")
Tempat_lahir = input("masukan tempat lahir anda: ")
Tanggal_lahir = input("masukan tanggal lahir anda: ")
Tahun_lahir = input("masukan tahun lahir anda: ")
Tahun_sekarang = input("masukan tahun sekarang: ")
Jenis_kelamin = input("masukan jenis kelamin anda: ")

Nilai_Inggris = float(input("masukan nilai Inggris anda: "))
Nilai_Matematika = float(input("masukan nilai Matematika anda: "))
Nilai_Indonesia = float(input("masukan nilai Indonesia anda: "))

nilai_rata_rata = (Nilai_Inggris + Nilai_Matematika + Nilai_Indonesia)/3
if nilai_rata_rata >= 80 and Jenis_kelamin.lower() == "Laki-laki":
    print("anda disarankan untuk masuk Jurusan Teknik Informatika")
elif nilai_rata_rata >= 80 and Jenis_kelamin.lower() == "Perempuan":
    print("anda masuk disarankan masuk Jurusan Sistem Informasi")
else :
    print("anda disarankan masuk Jurusan DKV")
    
usia = Tahun_sekarang - Tahun_lahir
    
if umur > 25:
    print("maaf anda tidak memenuhi persyaratan untuk diterima di universitas ini")