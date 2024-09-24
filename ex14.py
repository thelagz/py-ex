# Importa la funzione 'argv' dalla libreria 'sys'
from sys import argv

# Assegna il nome dello script ed una variabile ad argv
script, user_name = argv
# Definisce in prompt
prompt = '> '

# Stampa il nome dell'utente e quello dello script
print(f"Hi {user_name}, I'm the {script} script.")
# Stampa le stringhe
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")

# Assegna alla variabile l'input che verrà scritto a destra del prompt
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print(f"What kind of computer do you have?")
computer = input(prompt)

# Stampa la stringa inserendo come variabile solo l'input escludendo il prompt
print(f"""
Alright, so you said {likes} about liking me,
you said you live in {lives}, dunno where it is,
and you have a {computer} computer. Nice.
""")
