while(True):
    sayi=int(input("Çift olup olmadığını kontrol etmek için bir sayı giriniz: "))
    if(sayi>0):
        if(sayi%2==0):
            print("Bu sayı çifttir")
        else: 
            print("Bu sayı tektir")
    else:
        print("Lütfen sıfırdan büyük bir sayı giriniz")