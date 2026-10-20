from . import Operasi

DB_NAME = "database.txt"
TEMPLATE = {
    "pk" : "XXXXXX",
    "date_add": "YYYY-MM-DD",
    "judul": 255*" ",
    "penulis": 255*" ",
    "tahun": "YYYY"
}

def init_console():
    try:
        with open(DB_NAME, "r") as file:
            print("Database ditemukan.")
    except:
        print("Database tidak ditemukan. Membuat database baru...")
        Operasi.create_first_data()