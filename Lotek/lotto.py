import random


liczby = ["pierwszą","drugą","trzecią","czwartą","piątą","szóstą","siódmą","ósmą","dziewiątą","dziesiątą"]
i = 0
lotto = []
while len(lotto) < 10:
    try:
        cyfra = int(input("podaj liczbę {}: ".format(liczby[i])))
        if cyfra in lotto:
            print("Podałeś już taką liczbę, podaj inną!")
        elif cyfra < 1 or cyfra > 49:
            print("Twója liczba nie znajduje się w przedziale od 1 do 49")
        else:
            lotto.append(cyfra)
            i += 1
    except ValueError:
        print("błąd związany ze zmiennymi")

lotto_wygrane = []
while len(lotto_wygrane) < 10:
    cyfra = random.randint(1,49)
    if cyfra not in lotto_wygrane:
        lotto_wygrane.append(cyfra)



print("Liczby wylosowane przez Ciebie: {}".format(lotto))
print("Liczby wylosowane przez komputer: {}".format(lotto_wygrane))



total = 0
for i in lotto:
    for j in lotto_wygrane:
        if int(i) == int(j):
            print("Trafiłeś liczbę: {}".format(i))
            total = total+1



if total == 0 or total >=5:
    print("Trafiłeś: {} liczb".format(total))
elif total == 1:
    print("Trafiłeś: {} liczbę".format(total))
else:
    print("Trafiłeś {} liczby".format(total))


