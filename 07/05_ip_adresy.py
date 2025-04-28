import re

ip_adresa = input("Zadejte IP adresu: ")

rv = re.compile(r"([1-2]?\d?\d\.){3}[1-2]?\d?\d")

platna_ip_adresa = rv.fullmatch(ip_adresa)

if platna_ip_adresa:
    print("Zadaná IP adresa je v pořádku.")
else:
    print("Zadaná IP adresa není platná.")
    