import random
karakterler="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
cevap =input("kaç karakter uzunlukta olsun maksimum 10")
if cevap.isdigit:
    uzunluk = int(cevap)
    if 1 <= uzunluk <= 10:
        sifre = ""
        for i in range(uzunluk):
            sifre += random.choice(karakterler)
        print(sifre)
