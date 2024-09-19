from sys import argv

script, filename = argv

print(f"We're going to erase {filename}")
print("If you don't want to do this hit CTRL-C (^C) ")
print("If you want to do this hit RETURN")

input("?")

print("Now I'm opening the file...")
target = open(filename, 'w')

print("Now I'm truncating the file. Goodbye!")
#target.truncate()

print("Now I'm going to ask you for three lines")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("Now I will write to the file")

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print("And finally, we close it.")
target.close()
