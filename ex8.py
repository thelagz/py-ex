# Definisce una variabile
formatter = "{} {} {} {}"

# Definisce altre variabili
x = "Dio" + " Mattone"
y = "Sono" + "\n#"*10
z = "Suntuoso"
l = "Letsgoski"


# Appendere .format() alla variabile inserendo dei valori, fa stampare una stringa coi valori messi in ordine
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(x, y, z, l))
print(formatter.format(formatter, y, formatter, l))
print(formatter.format(
	"Frate sei bianco,",
	"bianco come er latte,",
	"c'hai presente er latte,",
	"quando te lo bevi che è bianco tu sei così"
))
