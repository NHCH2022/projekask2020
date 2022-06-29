#Atur cara mengira kadar gaji bulanan pekerja di sesebuah syarikat

#Pengisytiharan pemboleh ubah dan pemalar
#Input
gred = str(input("Masukkan gred pekerja(A hingga D): "))
if(gred == 'A' or gred == 'a'):
    gaji = 3100
elif(gred=='B' or gred=='b'):
    gaji = 2100
elif(gred=='C' or gred=='c'):
   gaji = 1300
elif(gred=='D' or gred=='d'):
   gaji = 1100
else:
   print("Tiada gred pekerja yang anda masukkan")
   quit()
jumlahjamkerjalebihmasapadaharibiasa = float(input("Masukkan jumlah jam kerja lebih masa pada hari biasa: ")) 
jumlahjamkerjalebihmasapadaharicutiam = float(input("Masukkan jumlah kerja lebih masa pada hari cuti am: "))
hasiltambahkerjalebihmasa = jumlahjamkerjalebihmasapadaharibiasa + jumlahjamkerjalebihmasapadaharicutiam
if(hasiltambahkerjalebihmasa>104):
   print("Jumlah jam kerja lebih masa melebihi had")
   quit()

kadarkerjalebihmasapadaharibiasa = float(1.5)
kadarkerjalebihmasapadaharicutiam = float(2)
kwsp = float(11)
perkesopekerja = float(3)

#proses
gajikasar = gaji
gajikerjalebihmasapadaharibiasa = gajikasar / 26 / 8 * jumlahjamkerjalebihmasapadaharibiasa * kadarkerjalebihmasapadaharibiasa
gajikerjalebihmasapadaharicutiam = gajikasar / 26 / 8 * jumlahjamkerjalebihmasapadaharicutiam * kadarkerjalebihmasapadaharicutiam
jumlahgajimasuk = gajikasar + (gajikasar / 26 / 8 * jumlahjamkerjalebihmasapadaharibiasa * kadarkerjalebihmasapadaharibiasa) + (gaji / 26 / 8 * jumlahjamkerjalebihmasapadaharicutiam * kadarkerjalebihmasapadaharicutiam)
potongangajiKWSP = kwsp / 100 * gajikasar                                                                                                   
potongangajiperkeso = perkesopekerja                                                                                                                         
jumlahgajikeluar = (kwsp / 100 * gajikasar) + perkesopekerja
jumlahgajikeseluruhan = (gajikasar + (gajikasar / 26 / 8 * jumlahjamkerjalebihmasapadaharibiasa * kadarkerjalebihmasapadaharibiasa) + (gajikasar / 26 / 8 * jumlahjamkerjalebihmasapadaharicutiam * kadarkerjalebihmasapadaharicutiam)) - ((kwsp / 100 * gajikasar) + perkesopekerja)

#output
print("\n\nGaji kasar:RM ", gajikasar)
print("Gaji kerja lebihan masa pada hari biasa  :RM ", "%.2f" % gajikerjalebihmasapadaharibiasa)
print("Gaji kerja lebih masa pada hari cuti am:RM ", "%.2f" % gajikerjalebihmasapadaharicutiam)
print("Jumlah gaji masuk:RM ", "%.2f" % jumlahgajimasuk)
print("Potongan gaji KWSP:RM ", "%.2f" % potongangajiKWSP)
print("Potongan gaji perkeso:RM ","%.2f" % potongangajiperkeso)
print("Jumlah gaji keluar:RM ", "%.2f" % jumlahgajikeluar)
print("Jumlah gaji keseluruhan:RM ","%.2f" % jumlahgajikeseluruhan)
