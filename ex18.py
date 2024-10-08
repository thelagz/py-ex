# definisce una funzione che si comporta in modo simile ad argv
def print_two(*args):
	arg1, arg2 = args
	print(f"arg1: {arg1}, arg2: {arg2}")

# definisce una funzione che esegue le stesse operazioni della prima, ma ha un numero di parametri prestabilito
def print_two_again(arg1, arg2):
	print(f"arg1: {arg1}, arg2: {arg2}")

# definisce una funzione con un singolo parametro
def print_one(arg):
	print(f"arg1: {arg}")

# definisce una funzione senza parametri
def print_none():
	print("I got nothin'.")

print_two("Zeb", "Lezzo")
print_two_again("Penzola", "Sgocciola")
print_one("First!")
print_none()
