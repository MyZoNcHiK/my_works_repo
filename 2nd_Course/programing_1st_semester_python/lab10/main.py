def generate_prosti(n):
    if not isinstance(n, int) or n<0:
        raise ValueError("n мусить бути цілe, невід'ємне число")

    prosti = []
    for i in range(2, n + 3):
        proste = True

        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                proste = False
                break
        if proste:
            prosti.append(i)

    return prosti
