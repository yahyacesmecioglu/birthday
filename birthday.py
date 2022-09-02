print("(1)Kişi oluştur\n(2)Kişi arat")
secenek=input("Yapmak istediğiniz işlemi girin: ")

if secenek=="1":    
    dosya=open("database.txt","a")
    isim=input("İsim: ")
    doğumtarihi=input("Doğum tarihi: ")
    dosya.writelines(isim+"\t"+doğumtarihi)
    print("Kişi oluşturuldu.")
    dosya.close()
elif secenek=="2":
    dosya=open("database.txt","r")
    arananisim=input("Aranan isim: ")
    dosya.seek(0)
    for i in dosya:
        if arananisim in i:
            print(i)
        elif arananisim not in i:
            print("Kişi bulunamadı.")    
    dosya.close()    

    