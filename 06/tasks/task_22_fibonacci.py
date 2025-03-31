# task_22_fibonacci.py

def fibonacci(n: int) -> list[int]:
    """
    Vrátí prvních n členů Fibonacciho posloupnosti.
    """

    fibonacci_list = []

    for num in range(0, n):
        if len(fibonacci_list) < 2:
            fibonacci_list.append(num)
        else:
            num_1 = fibonacci_list[-1]
            num_2 = fibonacci_list[-2]
            fibonacci_list.append(num_1 + num_2)

    return fibonacci_list
