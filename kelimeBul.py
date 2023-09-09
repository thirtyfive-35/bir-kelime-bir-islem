
#-*-coding:utf-8-*-
import codecs
import random
import os 

def sozlukten_ara(randomKelime):
    dizin = os.getcwd()+"\sozluk.txt"
    with codecs.open(dizin,"r",encoding='utf-8') as infile:
        puan=0
        list1 = list(randomKelime)
        for line in infile:
            try:

                kelime = line
                kelime = list(kelime)
                kelime.remove("\n")
                yeniKelime = ""
                for harf in kelime:
                    for i in range(len(list1)):
                        if harf == list1[i]:
                                
                            yeniKelime += harf
                            list1[i]= "7"
                            break
                list1 = list(randomKelime)       
                if kelime == list(yeniKelime):
                    puan+=len(yeniKelime)
                    print(yeniKelime+" "+str(len(yeniKelime))+" puan")
            except ValueError:
                continue
        print("Toplam puan : "+str(puan))

def random_harf_uret():
    alfabe = ["a","b", "c", "ç", "d" ,"e" ,"f" ,"g" ,"ğ" ,"h" ,"i" ,"ı" ,"j" ,"k" ,"l" ,"m" ,"n" ,"o" ,"ö" ,"p" ,"r" ,"s" ,"ş" ,"t" ,"u" ,"ü", "v" ,"y", "z"]
    randomHarfler = list()
   
    for i in range(0,12):
        randomHarfler.append(random.choice(alfabe))
    return randomHarfler

randomHarf = random_harf_uret()
sozlukten_ara(randomHarf)
print(randomHarf)





            
                
            
                
                

            



    


            
                
            
                
                

            



    

