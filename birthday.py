from os import system, name

def temizle():
    if name == "nt":
        _=system("cls")
    else:
        _=system("clear")

temizle()

while True:
    print("----------------------\n(1)Kişi oluştur\n(2)Kişi arat\n(3)Kişileri listele\n(0)Çıkış yap\n----------------------")
    secenek=input("Yapmak istediğiniz işlemi girin: ")

    temizle()
    
    if secenek=="1":    
        dosya=open("database.txt","a")
        isim=input("İsim: ")
        gun=input("Gün: ")
        ay=input("Ay: ")
        yil=input("Yıl: ")
        dosya.writelines(isim+" "+gun+" "+ay+" "+yil+("\n"))
        print("-----------------")
        print("Kişi oluşturuldu.")
        print("-----------------")
        dosya.close()
        sorgu=input("Devam etmek için herhangi bir tuşa basın(Çıkış için q): ")
        if sorgu=="q":
            break
        else:
            temizle()
    elif secenek=="2":
        dosya=open("database.txt","r")
        kisiBulundu = False
        print("-----------------")
        arananisim=input("Aranan isim: ")
        dosya.seek(0)
        for i in dosya:
            if arananisim.lower() in i.lower():
                print("-----------------")
                print(i)
                kisiBulundu = True
        if kisiBulundu==False:
            print("-----------------")
            print("Kişi bulunamadı.")    
            dosya.close()
        print("-----------------")
        sorgu=input("Devam etmek için herhangi bir tuşa basın(Çıkış için q): ")
        if sorgu=="q":
            break
        else:
            temizle()
        

    elif secenek=="3":
        dosya=open('database.txt', 'r') 
        icerik =dosya.read()        
        print("-----------------")
        print(icerik)
        print("-----------------")
        dosya.close()
        sorgu=input("Devam etmek için herhangi bir tuşa basın(Çıkış için q): ")
        if sorgu=="q":
            break
        else:
            temizle()
            
    elif secenek=="0":
        print("Çıkış yapıldı.")       
        break
