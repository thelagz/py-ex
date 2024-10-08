# importa la funzione argv dalla libreria sys
from sys import argv

# inserisce le variabili in argc, quindi per avviare lo script serviranno 3 parametri 
script, from_file, to_file = argv

# Stampa la stringa con il nome 
print(f"Copying {from_file} to {to_file}")

# prende come dati in lettura il primo file
indata = open(from_file).read()

# apre e scrive nel secondo file
to_file = open(to_file, 'w').write(indata)
