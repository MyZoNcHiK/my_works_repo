def average(numbers):
    if not numbers:
        return 0  
    return sum(numbers) / len(numbers)

def maximum(numbers):
    if not numbers:
        raise ValueError("Список порожній")
    return max(numbers)

def minimum(numbers):
    if not numbers:
        raise ValueError("Список порожній")
    return max(numbers)

def even_numbers(numbers):
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
    return result
