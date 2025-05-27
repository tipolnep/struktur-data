
def asc_bubble_sort(names):
    n = len(names)
    for i in range(n):
        for j in range(0, n-i-1):
            if names[j] > names[j+1]:
                names[j], names[j+1] = names[j+1], names[j]
    return names

def desc_bubble_sort(names):
    n = len(names)
    for i in range(n):
        for j in range(0, n-i-1):
            if names[j] < names[j+1]:
                names[j], names[j+1] = names[j+1], names[j]
    return names

while True:
    print('\n >>>>>>>>>>>>>>>>>>>>>>>> PROGRAM SORTING NAMA <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< \n')
    n = int(input('Input jumlah element list (Angka): '))
    print()
    # simpan setiap nama yang diinput ke dalam list
    
    a = [input(f'Masukkan Nama ke-{i+1} (enter untuk lanjut): ')for i in range(n)]
    
    print("Daftar List : ",a)
    print()
    while True:
        pilih = input("Silahkan Pilih Sorting (1/2) ?\n1. Ascending  2. Descending: ").lower()
        if pilih == '1':
            print("Berikut Hasil List yang sudah di Sorting (Ascending)")
            sorted_names = asc_bubble_sort(a)
            print(sorted_names)
            print()
            break
        if pilih == '2':
            print("Berikut Hasil List yang sudah di Sorting (Descending)")
            sorted_names = desc_bubble_sort(a)
            print(sorted_names)
            print()
            break
    ulang = input("Apakah Anda ingin mengulang program? (y/n): ").lower()
    if ulang != 'y':
        print("Terima kasih telah menggunakan program ini. Sampai jumpa!")
        break


