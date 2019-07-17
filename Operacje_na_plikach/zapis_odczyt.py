import os

print("-"*30)
path = os.getcwd()
print(path)
print("-"*30)

print("Chcesz stworzyć jakiś plik? Podaj jego nazwę: ")
file = input("Nazwa pliku: ")
content = input("Treść pliku: ")

plik = open(file,"w").write(content)


print("Wyciąganie treści z pliku")

print("nazwa pliku: {}".format(file))
print("Treść pliku: {}".format(open(file,'r').read()))


wybor = input("chcesz skasować plik? (tak / nie)")

if wybor == "tak":
    os.remove(file)
    print("skasowano plik")
elif wybor == "nie":
    print("nie skasowano pliku")
else:
    print("błędna komenda")

