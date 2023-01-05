def indeks(x):

    """
    fungsi untuk mencari indeks nilai terhadap suatu nim
    parameter : list

    ------deskripsi----- 
    fungsi indeks mengakumulasi perolehan indeks berdasarkan data 
    dari sebuah list yang menampung pasangan k dan v

    - k = nim
    - v = dict yang berisi pasangan k & v.
          k : clo 1, clo2, clo3, clo4
          v : nilai dari masing masing key

    Presentase CLO
    CLO 1 = 10%
    CLO 2 = 25%
    CLO 3 = 25%
    CLO 4 = 40%
    """
        
    c1 = int(x[1])
    c2 = int(x[2])
    c3 = int(x[3])
    c4 = int(x[4])
    sum = (10 * c1 / 100) + (25 * c2 / 100) +(25 * c3 / 100) +(40 * c4 / 100)

    if sum > 80: return 'A'
    elif sum > 70: return 'AB'
    elif sum > 65: return 'B'
    elif sum > 60: return 'BC'
    elif sum > 50: return 'C'
    elif sum > 40: return 'D'
    else: return 'E'

def report_nim_nilai(x):

    """
    fungsi untuk menampilkan seluruh nim mahasiswa beserta nilainya dengan separator tab
    parameter : list

    ------deskripsi----- 
    fungsi ini memproses data yang diperoleh dari
    suatu list yang menampung pasangan k dan v

    - k = nim
    - v = dict yang berisi pasangan k & v.
          k : clo 1, clo2, clo3, clo4
          v : nilai dari masing masing key   
    
    """
    print("NIM\t\tCLO 1\tCLO 2\tCLO 3\tCLO 4")
    
    for i in x:
        print(i,
              "\t",data_nilai[0][i][1],
              "\t",data_nilai[0][i][2],
              "\t",data_nilai[0][i][3],
              "\t",data_nilai[0][i][4])


def report_all(x):

    """
    fungsi untuk menampilkan seluruh nim, nilai, beserta indeksnya dengan separator tab
    parameter : list

    ------deskripsi----- 
    fungsi ini memproses data yang diperoleh dari
    suatu list yang menampung pasangan k dan v

    - k = nim
    - v = dict yang berisi pasangan k & v.
          k : clo 1, clo2, clo3, clo4
          v : nilai dari masing masing key   
    
    """
    print("NIM\t\tCLO 1\tCLO 2\tCLO 3\tCLO 4\tIndeks")
    
    for i in x:
        print(i,
              "\t",data_nilai[0][i][1],
              "\t",data_nilai[0][i][2],
              "\t",data_nilai[0][i][3],
              "\t",data_nilai[0][i][4],
              "\t", indeks(data_nilai[0][i]))
        
        sum_a = 0
        for i in x:
            if indeks(data_nilai[0][i]) == "A":
                sum_a = sum_a + 1

        sum_ab = 0
        for i in x:
            if indeks(data_nilai[0][i]) == "AB":
                sum_ab = sum_ab + 1
    print()
    print("Jumlah mahasiswa yang mendapat A =", sum_a)
    print("Jumlah mahasiswa yang mendapat AB =", sum_ab)


#---------------MAIN PROGRAM-------------------------------------#
    
filetext = open("nilai.txt", "r")

#1. Convert masing masing baris pada file text ke dalam bentuk list of string
list_data_nilai = []
for i in filetext:
    i = i.replace("\n", "")
    list_data_nilai.append(i.split("\t"))

#2. Convert list_data_nilai kedalam bentuk dictionary
dictionary_nilai = dict() 
for i in list_data_nilai:
    dictionary_nilai[i[0]] = {1:i[1], 2:i[2], 3:i[3], 4:i[4]}
    
#3. Memasukkan dictionary_nilai kedalam sebuah variable bernama data_nilai
    #- data_nilai adalah list yang menampung dictionary didalamnya
    #- data_nilai akan menjadi data utama yang digunakan di setiap proses dalam fungsi yang telah dibuat
    
data_nilai = [] 
data_nilai.append(dictionary_nilai)

#4. Program menu utama
print("\t\t\tSELAMAT DATANG DI PROGRAM NILAI HORE HORE")
print()
print("1 : Ketik 1 untuk mencari indeks nilai mahasiswa berdasarkan NIM")
print("2 : Ketik 2 untuk menampilkan NIM dan nilai seluruh mahasiswa")
print("3 : Ketik 3 untuk menampilkan NIM, nilai, dan Indeks nilai seluruh mahasiswa")
print("4 : Ketik 4 untuk menampilkan dictionary nilai")
print("0 : Ketik 0 untuk mengakhiri program")
print()

menu = input("Pilih Menu :")
while menu != '0':

    if menu == '1':
        print()
        nim = input("Masukkan NIM :")

        if nim in data_nilai[0]:
            print("Indeks nilai dari mahasiswa dengan NIM", nim, "adalah :", indeks(data_nilai[0][nim]))
        else:
            print("NIM tidak ditemukan")

    elif menu == '2':
        print()
        print("NIM dan Nilai Seluruh Mahasiswa")
        print()
        report_nim_nilai(data_nilai[0])
        
    elif menu == '3':
        print()
        print("NIM dan Indeks Nilai Seluruh Mahasiswa")
        print()
        report_all(data_nilai[0])

    elif menu == '4':
        print()
        for k,v in data_nilai[0].items():
            print("key: ",k,"value: ",v)

        
    print()
    menu = input("Pilih Menu :")

filetext.close()
