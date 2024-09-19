from sys import argv

script, from_file, to_file = argv

print(f"Copying {from_file} to {to_file}")

indata = open(from_file).read()

to_file = open(to_file, 'w').write(indata)
