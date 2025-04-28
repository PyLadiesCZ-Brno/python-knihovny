import re

regularni_vyraz = re.compile(r"\w+\.?\w+@\w+\.cz")

email = input("Zadej e-mail: ")
hledani = regularni_vyraz.fullmatch(email)
if hledani:
    print("E-mail je v pořádku!")
else:
    print("Nesprávný e-mail!")