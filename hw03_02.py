import random

def get_numbers_ticket(min, max, quantity):
    random_numbers = set()
    if (min >= 1) and (max <= 1000) and (max > min) and (max - min) >= quantity:
        while len(random_numbers) != quantity:
            random_numbers.add(random.randrange(min, max))
        random_numbers = list(random_numbers)
        random_numbers.sort()
        return random_numbers
    else:
        random_numbers = list(random_numbers)
        return random_numbers


lottery_numbers = get_numbers_ticket(10, 35, 5)
print("Ваші лотерейні числа:", lottery_numbers)