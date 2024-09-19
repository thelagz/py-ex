def print_two(*args):
	arg1, arg2 = args
	print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1, arg2):
	print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg):
	print(f"arg1: {arg}")

def print_none():
	print("I got nothin'.")

print_two("Zeb", "Lezzo")
print_two_again("Penzola", "Sgocciola")
print_one("First!")
print_none()
