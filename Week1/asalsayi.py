
for i in range(5):
    print(f"Asallık kontrolü için {i+1}. sayıyı giriniz:")
    asalmi=True
    sayi=int(input())
    if sayi==1:
        print("Asal değildir")
        continue
    elif sayi<1:
        print("Lütfen pozitif bir sayı giriniz:")
        continue
    for j in range(2,sayi):
        if (sayi%j)==0:
            asalmi=False
    if asalmi:
        print("Asal")
    else:
        print("Asal değil")        

