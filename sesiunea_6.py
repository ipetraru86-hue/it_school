# and inseamna adevarat doar daca toate conditiile sunt adevaratw
# or- inseamna adevarat daca macar una din conditii este adevarata
# not- inverseaza valoarea

#ploua = False
#print(not ploua)

#instructiunea FOR

#print("Salut")
#print("Salut")
#print("Salut")
#print("Salut")
#print("Salut")

#for i in range(5):
    #print("Salut")

# Instructiunea FOR este folosita atunci cand vrei sa repeti o actiune pentru fiecare element dintr-o colectie sau pentru un anumit numar de pasi
# FOR -> Ia pe rand fiecare valoare
# Executa acelasi bloc de cod pentru fiecare valoare

# Utilitati:
# afisam mai multe valori
# parcurgem o lista
# procesam literele dintr-un text
# calcule
# repetam instructiuni de un numar fix de ori

#sintaxa generala

#for variabila in colectie:
    #instructiune_1
    #instructiune_2
    #instructiune_3

# for - aici incepe bucla
# variabila - ia pe rand valorile
# in- din/in
# colectie- de unde luam valorile
# instructiunile dinn interior care trebuie sa fie indentate

#for i in range(5):
    #print(1)
# range(5) nu inseamna de la 1 pana la 5
# porneste de la 0
# se opreste inainte de 5

#ce este range()
# genereaza o secventa de numere

# 3 variante
# range (stop)- range(5)
# range(start, stop)- range (0,5)
# range(start, stop, pas) - range(0, 5, 2)

# produce o serie de numere pe care bucla for le foloseste unul cate unul
# ii spunem de ori vrem sa se repete ceva. (si) intre ce numere vrem sa mergem

#range(stop)
#for i in range(5):
 #    print(i)

#range(start, stop)
#for i in range(2, 6):
    #print(1)

#range(start, stop pas)
#for i in range(0, 10, 2):
    #print(1)

# Pas negativ
#for i in range(10, -10, -1):
     #print(i)

#rolul variabilei din for

 # i este o variabila care primeste pe rand valorile

#for numar in range(5):
    #print(numar)

# aceasta variabila este creata pentru bucla FOR
# isi schimba valoarea automat
# poate fi folosita in diferite operatii(calcule, conditii, afisari etc)

# Exemplu - calcul

#for i in range(5):
    #print(i + 10)

#for i in range(3):
 #x = i + 2
 #print(x)

# FOR nu este doar pt afisat valori
# se foloseste ca sa execute orice instructiune de mai multe ori

#for i in range(3):
    #print(i)
    #print("salut")

# FOR si variabile deja existente- poti folosi o variabila deja definita in interiorul buclei

#a = 10 # a ramane 10, fiind in afara buclei

#for i in range(3): # i ia valorile 0, 1 si 2
    #print(a + i) # se afiseaza suma dintre ele

# FOR si conditii IF
#Putem pune un IF in innteriorul buclei, ca sa verificam o conditie in fiecare pas
# exemplu:
#for i in range(6): # Bucla merge prin valorile 0, 1, 2, 3, 4, 5
    #if i % 2 == 0: # Pentru fiecare valoare verifica daca este para
        #print(i) # Doar valorile pare sunt afisate

# Cum se citeste un pseudocod
# 1. pt fiecare mr i de la 0 pana la 5
# 2. daca i este par
# 3. atunci afiseaza i

# FOR controleaza repetarea
# IF controleaza decizia

# FOR cu IF/ELSE
#for i in range(5):
    #if i < 3:
        #print(f"{i}-valoare mica" )
    #else:
        #print(f"{i}-valoare mare")

# FOR cu operatori de comparatie
# exemplu:
#for i in range(5):
    #if i ==3:
        #print("am gasit 3")
    #print(i)

# FOR si operatori logici
#for i in range(10):
    #if i >= 2 and i <= 6:
        #print(i)

# recap

# 1. range(5) inseamna de la 0 pana la stop - 1 (adica pana la 5 - 1)
# 2. Indentarea - Toate instructiunile pe care vrem sa le executam cu FOR trebuie sa fie indentate(cu un TAB in interiorul FOR ului)
# 3. Rolul variabilei i - i nu ramane mereu aceeasi; se schimba la fiecare pas; i este un nume dat de noi,

# BREAK/CONTINUR in FOR

# 1. BREAK- opreste complet bucla
# in momentul in care python intalneste break, iese din for si nu mai continua deloc cu restul iteratiilor
# Exemplu:
#for numar in range(1, 6): # range(1, 6) -> produce 1, 2, 3, 4, 5
    #if numar == 3: # la 1 -> se afiseaza; la 2 -> se afiseaza; la 3 -> conditia numar == 3 este adevarata/indeplinita
        #break # se executa break; bucla se opreste imediat
    #print(numar) # 4 si 5 nu mai sunt parcurse

# 2. CONTINUE - nu opreste bucla, doar sare peste iteratia curenta si trece la urmatoarea
# Exemplu:
#for numar in range(1, 6): # range(1, 6) -> produce 1, 2, 3, 4, 5
    #if numar == 3: # la 1 -> se afiseaza; la 2 -> se afiseaza; la 3 -> se executa continue
        #continue # Python nu mai executa print(numar) pentru 3; trece la urmatoarea iteratie
    #print(numar) # 4 si 5 se afiseaza normal

# diferente:
# BREAK - opreste toata bucla
# CONTINUE - opreste doar literatia curenta, bucla merge mai ddeparte

#exemplu
#for litera in "python":
   #if litera =="h":
       #break
   #print(litera)

# Exemplu: CONTINUE
#for litera in "python":
    #if litera == "h":
        #continue
    #print(litera)

 #exercitii:

# SA se calculeze suma nr pare de la 1 la 20, inclusiv.
#suma = 0
#for i in range (1,21):
    #if i % 2 ==0:
        #suma += i
#print(suma)

# Sa se parcurga nr de la 1 la 30 inclusiv si sa se afiseze cate nr sunt:> 10 si pare

#counter = 0
#for i in range(1,31):
    #if i > 10 and i % 2 ==0:
         #counter = counter + 1
#print(counter) # total = 10 nr pare intre (1,31)

# Sa se calculeze  suma nr de la 1 la 100 care sunt divizibile si cu 3 si cu 5
#suma = 0

#for i in range(1, 101):
    #if i % 3 == 0 and i % 5 ==0:
        #suma += i
        #print(i)
        #suma = suma + 1
#print("Suma este: ", suma)

#suma= 0
#i= 15
#suma += i
#devine suma = suma + i
#suma = 0 + 15
#suma = 15

# sa se parcurga nr de la 1 la 10. Pt fiecare nr se calculeaza rezultatul: rezultat = i * 3 - 2. Sa se afle cea mai mare val obtinuta.

#maxim = 0

#for i in range ( 1, 11):
    #rezultat = i * 3 - 2
    #if rezultat > maxim:
        #maxim = rezultat
        #print(maxim)
#print("Cea mai mare valoare este: ", maxim)

#  Se da un text. Pentru fiecare vocala, incrementam cu 2 puncte, iar pentru fiecare consoana cu 1 punct. la final afiseaza totalul punctelor

text = "python"
puncte = 0

for litera in text:
    if litera == "a" or litera == "e" or litera == "i" or litera == "o" or litera == "u":
        puncte = puncte + 2
        # puncte += 2
    else:
        puncte = puncte + 1
print("Total puncte: ", puncte)


