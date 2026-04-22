# recapitulare
from enum import nonmember
from operator import truediv

# variabila - este un loc din memorie in care stocam o valoare.
# exemple:
#nume = "ana" # stocheaza un text sau un streang
varsta = 20 # stocheaza un numar intreg
inaltime = 1,60 # stocheaza un numar zecimal

# semnul "=" pune valoarea din dreapta in variabila din stanga

# print - afiseaza imformatii pe ecran
# exemplu:

#print("salut")
#print(10)

# de ce folosim print:
#1. Afisam texte
#2. afisam valori
#3. afisam numerice
#4. afisam variabile
#5. verificam daca programul face ceea ce ne asteptam

# exemplu:
#print(nume)

# Putem afisa direct o valoare sau o variabila
#print("florin")
#print(25)

#varsta = 25
#print(varsta)

#print(nume,varsta) #python pune automat spatiu intre ele atunci cand sunt separate prin virgula.

# Putem afisa si text si variabile in acelasi print.
#print("numele meu este:",nume)

# Mai multe moduri de afisare cu print:

#Varianta 1- zic cu virgula in print
nume="Maria"
varsta=22

#print("numele este:",nume)
#print("varsta:",varsta)

# Varianta 2- cu "+" intre texte (streanguri)
#prenume="ion"
#nume_familie="popescu"

#print(prenume + ' ' + nume_familie) # ' ' -aceste ghilimele reprezinta un streang care tine un spatiu, pentru a separa prenumele de numele de familie.
# + -lipeste textele (in cazul nostru, nume de familie si prenume)
# cu + ambele parti trebuie sa fie stringuri (variabilele prenume si nume familie)

# Ok
#oras= "Timisoara"
#print("Locuiesc in " + oras)

# Ok
#varsta= 25
#print("Am " + varsta " ani") # eroare, pentru ca varsta este un numar intreg, nu un string
#varianta corectata
#print("Am " + str(varsta) + " ani") #converteste un numar intr-un string

#varianta 3- cu f-string/ cu acolade {}

#nume= "Andrei"
#varsta= 21

#print(f"Numele meu este {nume} si am {varsta} ani")
# litera f inainte de string spune ca in interior vom pune variabile
# variabilele se scriu intre acolade {}

#varianta 4- cuu metoda format(}
#varsta= 20

#print("Ma numesc {} si am {} ani".format(nume, varsta))

#Exercitiul 1 - creaza o variabila nume si afiseaz-o.

#nume= "denisa"
#print(nume)

#Exercitiul 2 - creaza 2 variabile nume si oras si afiseaza-le pe aceeasi linie.

#nume= "Maria"
#oras= "Bucuresti"
#print(f"{nume} din {oras}")
#print(nume + " din " + oras)
#print(nume, oras)

#text = " d"
#print(len(text))

# Tipuri de date in python:
# Un tip de date arata ce fel de valoare avem intr-o variabila
# Un nume este text
# O varsta este un numar intreg
# O inaltime este un numar zecimal/flotant
# O valoare de tip da/nu poate fi adevarata sau falsa.

#Python trebuie sa stie ce fel de imformatie pastreaza, pentru ca fiecare tip de date se comporta diferit.

#1. str - string-text
# String reprezinta textul
# Exemple:
nume= "Ana"
oras= "Cluj"
mesaj= "Salut"

a= "Python"
b= 'curs'
#Observatie- chiar daca scriem cifre intre ghilimele, ele vor fi considerate tot text.-Ex: "123" esste un string, nu un numar.

# Triple quotes- pentru stringuri care contin mai multe randuri
# Exemple comentariu pe mai multe randuri
'''
Acesta este un comentariu
care contine mai multe randuri.
'''
#nume= "Alex"
text='''Acesta este un text cu numele
care contine mai multe randuri
si se scrie intre triple quotes'''

#print(text)

# Diferenta dintre " " si ''' '''
# cu ghilimele normale scriem de obicei texte pe o singura linie
# cu ghilimele triple putem scrie texte mai lungi, pe mai multe linii

# \n- newline- trece pe linia urmatoare
#print("Salutare\nbine ai venit\nla curs")# textul este scris pe o singura linie de cod, dar la afisare apare pe mai multe linii.
#print("Meniu:\npizza\npaste\nsucuri")

# Int- Intiger- numar intreg- numere fara zecimale

varsta= 25
an= 2026
numar_persoane= 26

# Float- numar zecimal
inaltime= 1.75
pret= 19.99
temperatura= 15.5
# In python zecimalele se scriu cu punct (.), nu cu virgula (,).
print(15.5) #OK
print(15,5+2) #NOK

# bool- boolean- adevarat sau fals
# Acest tip de date are doar doua valori: true(adevarat) sau false(fals)

Invata_python =True
Este_ziua_mea =False

variabila= None


















