import my_module as my
import random

numbers = list(map(int, input().split()))

print("Середнє значення:", my.average(numbers))
print("Найбільше число:", my.maximum(numbers))
print("Найменше число:", my.minimum(numbers))
print("Парні числа:", my.even_numbers(numbers))

print("Випадкове число від 1 до 100:", random.randint(1, 100))
print("Випадковий елемент списку:", random.choice(numbers))
