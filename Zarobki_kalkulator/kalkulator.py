print("-"*30)

days = int(input("Ilość dni pracujących"))
zarobki = int(input("Zarobki neeto"))
stawka = (zarobki / days / 8)
ilosc_nadgodzin = int(input("Podaj ilosc nadgodzin"))

print((ilosc_nadgodzin*stawka)*2)

