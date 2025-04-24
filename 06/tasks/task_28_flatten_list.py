# task_28_flatten_list.py

def flatten_list(nested: list[list[int]]) -> list[int]:
    """
    Converts a multi-nested list to a single-dimensional list.
    """
    flat_list = []
    for item in nested:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)

    return flat_list
