# Elimizdeki üç adet string içerisindeki rakamlar temizlenip (sadece harfler kalacak) temiz
# halleri bir listede tutulacaktır. Temiz halde listede bulunan isimlerin hepsi yan yana bir
# string değişkeninde birleştirilecek ve aralarında (-) işareti olacaktır.
# Örnek çıktı : Ahmet-Mehmet-Hakan

def TemizVeri():
    ilk_string ="Ah5me4t"
    ikinci_string = "M9eHm4eT"
    ucuncu_string ="Ha3K5a1n"
    ilk_string=''.join([i for i in ilk_string if i.isalpha()])
    ikinci_string= ''.join([i for i in ikinci_string if  i.isalpha()])
    ucuncu_string=''.join([i for i in ucuncu_string if i.isalpha()])

    
    Birlesmis_deger=ilk_string +"-"+ikinci_string+"-"+ucuncu_string
    print(Birlesmis_deger)
    return Birlesmis_deger
TemizVeri()