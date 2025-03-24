# task_06_filter_by_age.py

def filter_by_age(people: list):
    """
    Napiš funkci filter_by_age, která vezme seznam slovníků, kde každý slovník
    představuje osobu (s klíči name a age), a vrátí seznam osob, které jsou
    starší než 18 let.
    """
    return [person for person in people if person['age'] > 18]


people = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 17},
    {"name": "Charlie", "age": 22},
    {"name": "David", "age": 18}
]

result = filter_by_age(people)
print(result)
