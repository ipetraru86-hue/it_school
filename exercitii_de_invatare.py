           #exercitii
           #if/else:

# 1. Scrie un numar intreg si afiseaza, daca este par sau impar.

#x = 5
#if x % 2 == 0:
#    rezultat = "par"
#else:
 #   rezultat = "impar"
 #  print(rezultat)

#rezultat = "par" if x % 2 == 0 else "impar"
#print(rezultat)

#if x % 2 != 0: rezultat = "impar"
#print(rezultat)

# 2. Cere utilizatorului varsta. Daca are 18 ani sau mai mult, afiseaza "Poti vota", si daca nu are,afiseaza "esti minor.

#varsta = int(input("Introdu varsta ta: "))
#if varsta >= 18:
#    print("Poti vota")
#else:
#    print("esti minor")

# 3. Verifica daca un numar introdus de la tastatura este pozitiv/negativ sau zero.

#numar_1 = int(input("Valoarea: "))

#if numar_1 == 0:
#    print("Este zero")

#if numar_1 >=0:
#    print("pozitiv")

#if numar_1 <= 0:
#    print("negativ")

       #if/else/elif:

# 1. Primeste un punctaj (0-100) si afiseaza nota corespunzatoare ( A=90+, B=89+ si C=70+).

#punctaj = int(input("Punctajul: "))

#if punctaj < 100:
 #  print("A=90+")
#elif punctaj < 90:
 #   print("B=89+")
#elif punctaj < 80:
#    print("C=70+")

    # exercitii while

#1 Folositi for pentru a citi n numere si if pt a calcula sumaaa doar a celor pare

numere = (1,101)
suma = 0
for i in range(1,101):
    if i % 2 == 0:
        suma += 1
print(suma)
























