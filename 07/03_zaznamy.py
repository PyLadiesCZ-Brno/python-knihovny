import re

zaznamy = """
searchNumber: pavca.czechitas action: search phone number of user dita
user: pavca action: send sms to phone number +420728123456
user: jirka: action: send 2 sms to phone number +420734123456
"""

rv = re.compile(r"\+420\d{9}")

for tel in rv.findall(zaznamy):
    print(tel)

upravene_zaznamy = rv.sub("X" *12, zaznamy)
print(upravene_zaznamy)