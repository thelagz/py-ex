# Importa la funzione 'argv' dalla libreria 'sys'
from sys import argv

# Assegna delle variabili di input ad argv
script, first, second, third = argv

# Stampa le stringhe con le variabili inserite prima dell'esecuzione
print("Your script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

x = input("What's your fourth variable? ")

print("Your fourth variable is:", x)
