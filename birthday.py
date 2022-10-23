from os import system, name
import time

def temizle():
    if name == "nt":
        _=system("cls")
    else:
        _=system("clear")

temizle()

while True:
    print("(1)Kişi oluştur\n(2)Kişi arat\n(3)Kişileri listele\n(0)Çıkış yap")
    secenek=input("Yapmak istediğiniz işlemi girin: ")
    
    if secenek=="1":    
        dosya=open("database.txt","a")
        isim=input("İsim: ")
        gun=input("Gün: ")
        ay=input("Ay: ")
        yil=input("Yıl: ")
        dosya.writelines(isim+" "+gun+" "+ay+" "+yil+("\n"))
        print("Kişi oluşturuldu.")
        dosya.close()
        sorgu=input("Devam etmek için herhangi bir tuşa basın(Çıkış için q): ")
        if sorgu=="q":
            break
        else:
            temizle()
    elif secenek=="2":
        dosya=open("database.txt","r")
        kisiBulundu = False
        arananisim=input("Aranan isim: ")
        dosya.seek(0)
        for i in dosya:
            if arananisim.lower() in i.lower():
                print(i)
                kisiBulundu = True
        if kisiBulundu==False:
            print("Kişi bulunamadı.")    
            dosya.close()
        
        sorgu=input("Devam etmek için herhangi bir tuşa basın(Çıkış için q): ")
        if sorgu=="q":
            break
        else:
            temizle()
        

    elif secenek=="3":
        dosya=open('database.txt', 'r') 
        icerik =dosya.read()        
        print(icerik)
        dosya.close()
        sorgu=input("Devam etmek için herhangi bir tuşa basın(Çıkış için q): ")
        if sorgu=="q":
            break
        else:
            temizle()
            
    elif secenek=="0":
        print("Çıkış yapıldı.")       
        break
