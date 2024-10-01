print('Nama = Muhammad Romadhoni')
print('NIM  = 2409116104')
print('Kelas = Sistem Informasi C') 

#register
nama = str(input('masukan username anda = '))
sandi = str(input('masukan sandi anda = '))


print('-----------------------(selamat datang user)-------------------------')
print('-----(silahkan masukan username dan password untuk proses register)-----')

#login User dan Password
while True:
    print('-----halaman menu login-----')
    username = str(input("silahkan input username anda = " ))
    password = str(input("silahkan input password anda = " ))
    if username==nama and password==sandi:
        print('----------Selamat Datang' ,nama , 'dengan Nim' , sandi,'----------')
#transaksi barang
        barang = str(input('masukan nama barang belanjaan anda = '))
        harga = int(input('masukan harga barang yang ingin dibeli = Rp : '))
        jumlah = int(input('masukan jumlahnya = '))
        total = harga * jumlah

        if total >= 250000:
            diskon = total * 0.25
            total = total - diskon
            print('anda mendapatkan diskon = 25%')
            print('total belanjaan anda = Rp',total)
            print('terimakasih')

        else:
            print('anda tidak mendapatkan diskon')
            print('total belanjaan anda = Rp',total)
            print('terimakasih')
        print('Silahkan pilih menu di bawah ini')
        print('1. Beli Lagi')
        print('2. Exit')
        pilih = int(input('pilih = '))
        if pilih == 1:
            continue
        elif pilih == 2:
            break
        
        else:
            print('pilihan anda salah')
    else:
        print('username atau password anda salah')


                        