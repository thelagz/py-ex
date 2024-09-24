#Assegna i valori alle variabili
name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
altezza = round( height * 2.54 )
weight = 180 # lbs
peso = round( weight / 2.204623 )
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

#Stampa usando 'f' per inserire il valore della var all'interno della stringa
print(f"Let's talk about {name}.")
print(f"He's {altezza} cm tall.")
print(f"He's {peso} kg heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + altezza + peso
print(f"If I add {age}, {altezza}, and {peso}, I get {total}")
