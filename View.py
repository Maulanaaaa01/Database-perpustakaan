from . import Operasi

def delete_console():
    read_console()
    while(True):
        print("Pilih nomor buku yang ingin di delete")
        no_buku = int(input("Nomor Buku : "))
        data_buku = Operasi.read(index=no_buku)
            
        if data_buku:
            data_break = data_buku.strip().split(",")
            pk = data_break[0]
            data_add = data_break[1]
            judul = data_break[2]
            penulis = data_break[3]
            tahun = data_break[4]
            
            # ini adalah data yang di hapus
            print("\n"+"="*100)
            print("Silahkan pilih data apa yang ingin anda hapus")
            print(f"1. Judul\t: {judul:.40}")
            print(f"2. Penulis\t: {penulis:.40}")
            print(f"3. Tahun\t: {tahun:4}")
            
            is_done = input("Apakah anda yakin ingin menghapus data? (y/n): ")
            if is_done.lower() == "y":
                Operasi.delete(no_buku)
                break
        else:
            print("Nomor tidak valid silahkan masukan lagi")
    
    print("Data berhasil di hapus")
                
def update_console():
    read_console()
    while(True):
        print("Pilih nomor buku yang ingin di update")
        no_buku = int(input("Nomor Buku : "))
        data_buku = Operasi.read(index=no_buku)
        
        if data_buku:
            break
        else:
            print("Nomor tidak valid silahkan masukan lagi")
    
    data_break = data_buku.strip().split(",")
    pk = data_break[0]
    data_add = data_break[1]
    judul = data_break[2]
    penulis = data_break[3]
    tahun = data_break[4]
    
    while(True):
        # ini adalah data yang di update
        print("\n"+"="*100)
        print("Silahkan pilih data apa yang ingin anda ubah")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")
        
        # memilih mode untuk update
        user_option = input("Pilih data [1,2,3]: ")
        print("\n"+"="*100)
        match user_option:
            case "1": judul = input("Judul\t: ")
            case "2": penulis = input("Penulis\t: ")
            case "3":
                while(True):
                        try:
                            tahun = int(input("Tahun\t: "))
                            if len(str(tahun)) == 4:
                                break
                            else:
                                print("tahun harus angka,silahkan masukan tahun yang benar (yyyy)")
                        except:
                            print("tahun harus angka,silahkan masukan tahun yang benar (yyyy)") 
            case _: print("Index tidak sesuai")    
        
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")
        
        is_done = input("Apakah anda ingin keluar dari update data? (y/n): ")
        if is_done.lower() == "y":
            break
    
    Operasi.update(no_buku,pk,data_add,tahun,judul,penulis)
    
    
def create_console():
    print("\n\n"+"="*100)
    print("Silahkan tambah data buku\n")
    penulis = input("penulis\t: ")
    judul = input("judul\t: ")
    while(True):
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("tahun harus angka,silahkan masukan tahun yang benar (yyyy)")
        except:
            print("tahun harus angka,silahkan masukan tahun yang benar (yyyy)")
            
    Operasi.create(tahun,judul,penulis)
    print("Berikut adalah data baru anda")   
    read_console()
    
def read_console():
    data_file = Operasi.read()
    index = "No"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"
    
    # Header
    print("\n"+"="*100)
    print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:5}")
    print("-"*100)
    
    # Data
    
    
    for index, data in enumerate(data_file):
        if not data.strip():
            continue

        data_break = data.strip().split(",")

        if len(data_break) != 5:
            print(f"Format data salah pada baris {index + 1}: {data!r}")
            continue

        pk = data_break[0]
        data_add = data_break[1]
        judul = data_break[2]
        penulis = data_break[3]
        tahun = data_break[4]

        print(
            f"{index + 1:4} | {judul:.40} | "
            f"{penulis:.40} | {tahun:4}"
        )

    # Footer
    print("="*100+"\n")