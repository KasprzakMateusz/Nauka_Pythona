
print("próba importu/exportu list do plików")

lista = []

for i in range(5):
    skladniki = input("Składniki: ")
    lista.append(skladniki)

print(lista)

save_to_file = open("lista.txt","w").write(str(lista))

file = open("lista.txt","r").read()

