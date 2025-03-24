def is_prime(n):
    # prvocisla pouze od 2!
    if n < 2:
        return False
    # 2 je prvocislo!
    if n == 2:
        return True
    # zbaveni se sudych cisel
    if n % 2 == 0:
        return False
    # overeni lichych
    for i in range(3, int(n) + 1, 2):
        if n % i == 0:
            return True
    return True


print(is_prime(7))
