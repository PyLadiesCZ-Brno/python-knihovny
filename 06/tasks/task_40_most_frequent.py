# task_40_most_frequent.py

def most_frequent(items: list) -> any:
    """
    Vrátí nejčastěji se vyskytující prvek v seznamu.
    """
    highest_number = 0
    for item in items:
        number = items.count(item)
        if number > highest_number:
            highest_number = number
            most_frequent_item = item
    return most_frequent_item
