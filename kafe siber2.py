print ("SELAMAT DATANG KE SISTEM EPAY")
print ("")

print("Adakah pelanggan seorang ahli tetap? ( y = yes, n = no) ")
status = input()

durasi = float(input("Masukkan durasi penggunaan dalam minit: "))

if durasi <= 60:
    bayaran = durasi * 1.5

elif 60<durasi<121:
    bayaran = 1.8 + (durasi / 60) * 0.025

else :
    bayaran = 1.8 + 1.5 + (durasi - 120) * 0.02

if status == "y":
    diskaun = bayaran * 1/10
    bayaran = bayaran - diskaun

else :
    diskaun = 0
    bayaran = bayaran

print("Jumlah yang perlu dibayar: RM","%.2f" % bayaran)
print("Jumlah diskaun: RM","%.2f" % diskaun)

