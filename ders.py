a = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            }
w = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if w in a.keys():
    if w == ("CRINGE"):
        print("Garip ya da utandırıcı bir şey")
    elif w == ("LOL"):
        print("Komik bir şeye verilen cevap")
else:
    print("bu kelime yok")
