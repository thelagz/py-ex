def funzione(x, y):
	print(f"Lo sdrogo oggi è {x}")
	print(f"Lo sdrogo massimo è {y}")
	print(f"Lo sdrogo supremo è {x * y}. \n")


funzione(10, 20)

oggi = int(input("Inserisci il tuo sdrogo giornaliero: "))
mass = int(input("Inserisci lo sdrogo massimo: "))

print("La funzione dello sdrogo ti dice: ")
funzione(oggi, mass)

print("Sdrogheggiamo con la matematica")

funzione(10 + oggi, 20 + mass)

print("Ora proviamo a passare direttamente l'input alla funzione")

funzione(int(input("> ")), int(input("$ ")))

def funz(i):
	print("Proviamo a chiamare la prima funzione all'interno di questa.\n")

funz(funzione(oggi, mass))
