import re

rv = re.compile(r"[a-z]{1,8}")

while True:
    uzivatelske_jmeno = input("Uživatelské jméno: ")

    if rv.fullmatch(uzivatelske_jmeno):
        print("Uživatelské jméno je v pořádku.")
        break
    else:
        print("Nesprávně zadané uživatelské jméno!")