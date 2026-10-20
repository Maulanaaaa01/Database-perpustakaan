import os
import CRUD as CRUD

if __name__ == "__main__":
    sistem_operasi = os.name
    
    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")
    
    print("SELAMAT DATANG DI PROGRAM")
    print("DATABASE PERPUSTAKAAN")
    print("============================")
    
    # check database itu ada atau tidak
    CRUD.init_console()
       
    while(True):
        match sistem_operasi:
            case "posix": os.system("clear")
            case "nt": os.system("cls")
        
        print("SELAMAT DATANG DI PROGRAM")
        print("DATABASE PERPUSTAKAAN")
        print("============================")
        
        print("1. Read Data")
        print("2. Create Data")
        print("3. Update Data")
        print("4. Delete Data")
        
        user_option = input("Masukan Pilihan (1-4): ")
    
        match user_option:
            case "1": CRUD.read_console()
            case "2": CRUD.create_console()
            case "3": CRUD.update_console()
            case "4": CRUD.delete_console()
        
        
        is_done = input("Apakah anda ingin keluar? (y/n): ")
        if is_done.lower() == "y":
            break

print("Terima kasih telah menggunakan program ini!")