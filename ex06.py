# assegna un intero alla varibile
types_of_people = 10
# assegna la stringa perfomattata alla variabile
x = f"There are {types_of_people}"

# assegna la stringa alla variabile
binary = "binary"
# assegna la stringa alla variabile
do_not = "don't"
# assegna la stringa preformattata alla variabile
y = f"Those who know {binary} and those who {do_not}"

# stampa le variabili
print(x)
print(y)

# stampa una stringa insieme alla variabile 'x' e una con 'y'
print(f"I said: {x}")
print(f"I also said: '{y}'")

# assegna un valore booleano alla variabile
hilarious = True
# assegna la stringa semiformattata alla variabile
joke_evaluation = "Isn't that joke so funny?! {}"
# stampa la stringa, formattandola con la variabile booleana alla fine
print(joke_evaluation.format(hilarious))

# assegna altre stringhe a due variabili
w = "This is the left side of..."
e = "a string with right side"
# stampa l'unione delle variabili
print(w + e)
