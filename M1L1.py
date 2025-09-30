meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "cringe": "Garip ya da utandırıcı bir şey",
            "lol": "Komik bir şeye verilen cevap",
            "stan":"Aşırı hayran olmak, takıntılı şekilde desteklemek",
            "STAN":"Aşırı hayran olmak, takıntılı şekilde desteklemek",
            "slay":"Çok iyi görünmek, harika bir iş yapmak",
            "SLAY":"Çok iyi görünmek, harika bir iş yapmak",
            "YEET":"Bir şeyi fırlatmak ya da coşkulu bir ifade (bağırmak gibi)",
            "yeet":"Bir şeyi fırlatmak ya da coşkulu bir ifade (bağırmak gibi)",
}
while True:
    print("merhaba")
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!) ÇIKIŞ İÇİN cıkıs yazınn: ")
    if word == "cıkıs":
        print("görüşürüz")
        break

    if word in meme_dict.keys():
        # Kelime eşleşiyorsa ne yapmalıyız?
        meaning = meme_dict[word]
        print("Anlamı:", meaning)
    else:
        # Kelime eşleşmiyorsa ne yapmalıyız?
        print("maalesef sözlükte bu kelime yok")
