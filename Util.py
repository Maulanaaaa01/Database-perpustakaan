import random
import string


def random_string(panjang:int) -> str:
    hasil_string =''.join(random.choices(string.ascii_letters, k=panjang))
    return hasil_string