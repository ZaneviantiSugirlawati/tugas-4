data=[]
while(True):
    nama=input("Masukan Nama: ")
    nim=input("Masukan Nim: ")
    tugas=int(input("Masukan Nilai Tugas: "))
    uts=int(input("Masukan Nilai UTS: "))
    uas=int(input("Masukan Nilai UAS: "))
    akhir=int (30 * tugas / 100) + (35 * uts / 100) + (35 * uas / 100)
    data.append([nama, nim, tugas, uts, uas, akhir,])
    ulangi=input("Tambah Data (y/t)? ")
    if ulangi.lower() == 't' :
        break;

print("\nDAFTAR NAMA\n")
print("=====================================================================================")
print("|   NAMA    |    NIM     |     TUGAS     |     UTS      |     UAS     |     AKHIR   |")
print("=====================================================================================")
for x in data:
    print("| {0:10} | {1:10} | {2:13} | {3:10} | {4:13} | {5:10} |" .format(x[0], x[1], x[2], x[3], x[4], x[5]))
print("=====================================================================================")