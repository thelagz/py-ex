# L'escape sequence '\t' rende una stringa spostata di un tab
tabby_cat = "\t I'm tabbed in"
# L'escape sequence '\n' mette a capo ciò che lo segue
persian_cat = "I'm split\non a line"
# L'escape sequence '\\' permette di stampare il carattere '\'
backslash_cat = "I'm \\ a \\ cat"

# Mix di formattazione con le quote triple e le escape sequqnces
fat_cat = '''
I'll do a list:
\t* Catfood
\t* Fishies
\t* Catnip\n\t* Grass
'''

# Stampa le variabili
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
