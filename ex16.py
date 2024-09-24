# Importa la funzione argv dalla libreria sys
from sys import argv

# Assegna due variabili ad argv
script, filename = argv

# Stampa le stringhe che spiegano cosa farà il programma
print(f"We're going to erase {filename}")
print("If you don't want to do this hit CTRL-C (^C) ")
print("If you want to do this hit RETURN")

input("?")

print("Now I'm opening the file...")
# Apre il file in modalità scrittura (w) eliminando tutto il contenuto
target = open(filename, 'w')

print("Now I'm truncating the file. Goodbye!")
#target.truncate()

print("Now I'm going to ask you for three lines")

# Chiede delle stringhe da inserire come input
line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("Now I will write to the file")

# Scrive le righe, mettendole a capo
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print("And finally, we close it.")
# Chiude il file
target.close()
