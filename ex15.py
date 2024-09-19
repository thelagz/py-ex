# importa il modulo argv dalla libreria sys
from sys import argv

# definisce due variabili e le assegna ad argv
script, filename = argv

# assegna alla variabile il comando open()
txt = open(filename)

# stampa la stringa ed il nome del file
print(f"Here is your filename {filename}")
# stampa il contenuto della variabile 'txt' eseguendo il comando 'read'
print(txt.read())
txt.close()

# definisce il prompt
prompt = '> '
# chiede input all'utente che scriverà a capo, dopo il prompt e lo assegna alla var
file_again = input("Type the filename again: \n"+ prompt)

# assegna alla variabile il compando open() (nuovamente)
txt_again = open(file_again)

# stampa il contenuto della variabile eseguendo read()
print(txt_again.read())
txt_again.close()
