# *args- ia toate valorile date fara nume si le pune intr-un tuplu

#x= "25"
#y= int(x)
#print(y+ 5)
#print("10"+"5")
#print(10+5)

#x= "19.99"
#print(type(x))
#decimal= float(x)
#print(type(decimal))

#operatori aritmetici
#simboluri folosite pt calcule matematice
# + adunare
# - scadere
# * inmultire
# / impartire
# ** ridicare la putere
# // impartirea intreaga
# % restul impartirii


#adunare
#a= 10
#b= 5
#suma= a + b
#print(suma)

#scadere
#diferenta= a - b
#print(diferenta)

#inmultire
#produs= a * b
#print(produs)

#impartire
#cat= a / b
#print(int(cat))

 #: 2f se foloseste ca sa afisam un nr zecimal cu exact doua cifre dupa virgula
 #f vine de la float
 # .2 inseamna doua zecimale

#rezultat = 10 / 3
#print(rezultat)
#print(f"{rezultat:.2f}")
 #Important:.2f nu schimba valoarea, doar modul de afisare

# impartirea intreaga
#print(10 // 3)
# pt ca 10 impartit la 3 este 3.333.. iar // pastreaza doar partea intreaga adica 3

# restul impartirii
#print(10 % 3)
#print(8 % 2)
#daca restul este 0, nr este divizibil cu 2
#util pt a verifica daaca un nr este par sau impar

#puterea
#print(2 ** 3)
#print(5 ** 2)

 #ordinea operatiilor
 #in python se respecta ordinea matematica a operatiilor
#print(2 + 3 * 4) # inmultirea sse face inaintea adunarii
#print((2+3)* 4) # parantezele schimba ordinea operatiilor, adunarea se face inaintea inmultirii

# in matematica "=" inseamna egalitate
# in programare "=" inseamna atribuire
#x = 10 #x primeste valoarea 10 in variabila x

# functia input() - cum citim date de la utilizator
# input este o functie care permite utilizarea sa scrie ceva de la tastatura

#nume = input("Cum te numesti? ")
#print(nume)

#1. programul afiseaza mesajul "Cum te numesti?"
#2. utilizatorul scrie ceva
#3. valoarea introdusa este salvata in variabila nume

# Input returneaza intotdeauna text
#varsta = input("Cati ani ai? ")
#print(varsta)
#print(type(varsta))

#varsta = int(input("Cati ani ai?\n "))
#print(varsta)
#print(type(varsta))

#inaltime = float(input("Ce inaltime ai?\n"))
#print(inaltime)
#print(type(inaltime))

#numar1 = input("primul numar: ")
#numar2 = input("al doilea numar: ")

#print(numar1 + numar2)

#numar1 = int(input("primul numar: "))
#numar2 = int(input("al doilea numar: "))
#print(numar1 + numar2)

# exemple operatii aritmetice
#a = 10
#b = 3
#print("adunare", a + b)
#print("scadere", a - b)
#print("inmultire", a * b)
#print("impatire", a / b)
#print("impartirea intreaga", a // b)
#print("restul impartirii", a % b)
#print("puterea", a ** b)

#greseli frecvente
#nume= Ana - corect: "Ana" ; variabilele de tip text/string trebuie sa fie intre ghilimele
#inaltime= 1,75 - corect: 1.75 ; in python folosim punctul "." pentru zecimale

# cand unesti text cu un numar fara conversie
#varsta = 20
#print("Am " + str(varsta) + " ani") #Trebuie sa convertim variabila varsta la string pt a putea lipi/concatena textul.

#input() returneaza intotdeauna text/string - ai nevoie sa faci conversie la tipul de date dorit. (int, float etc)

# se confunda / cu //
# / - rezultatul decimal
# // - doar partea intreaga

# Exercitii:

#1. Citeste de la tastatura numele utilizatorului, si afiseaza un mesaj: "Bun venit la curs."
#nume = input("nume: ")
#print("Bun venit la curs. " + nume)

#2. Citeste de la tastatura doua numere intregi si afiseaza suma lor.

#numar_1 = int(input("numar_1: "))
#numar_2= int(input("numar_2: "))

#suma = numar_1 + numar_2

#print(f"Suma numerelor este:{suma}")

#3. Citeste de la tastatura 2 numere intregi si afiseaza suma, scaderea, inmultirea si impartirea.

#numar_1 = int(input("numar_1: "))
#numar_2 = int(input("numar_2"))

#2suma = numar_1 + numar_2
#print(f"Suma numerelor este:{suma}")

#scaderea = numar_1 -numar_2
#print(f"Scaderea numerelor este:{scaderea}")

#inmultirea = numar_1 * numar_2
#print(f"inmultirea numerelor este:{inmultirea}")

#impartirea = numar_1 / numar_2
#print(f"impartirea numerelor este:{impartirea}")

# 3. Citeste varsta si afiseaza Peste 5 ani, voi avea x ani.

#varsta = int(input("varsta este: "))
#varsta_viitoare = varsta + 5
#print(f"Peste 5 ani voi avea varsta {varsta_viitoare} ")

# 4. Citeste un pret si o cantitate si calculeaza costul final.
#pret = float(input("pretul este: "))
#cantitate = int(input("cantitatea este: "))

#cost_final = pret * cantitate

#print(f"Costul final este {cost_final:.1f}")


