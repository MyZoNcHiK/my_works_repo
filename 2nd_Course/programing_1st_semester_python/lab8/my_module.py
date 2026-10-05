def average(numbers):
    return sum(numbers) / len(numbers)

def maximum(numbers):
    return max(numbers)

def minimum(numbers):
    return min(numbers)

def even_numbers(numbers):
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
    return result
