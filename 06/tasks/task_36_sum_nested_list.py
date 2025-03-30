# task_36_sum_nested_list.py

def sum_nested_list(nested: list) -> int:
    """
    Sečte všechna čísla v (potenciálně zanořeném) seznamu.
    Nápověda: isinstance(), rekurze
    """
    sum = 0
    for i in nested:
        if isinstance(i, list):
            sum += sum_nested_list(i)
        else:
            sum += i
    return sum
