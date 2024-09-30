import random

def get_numbers_ticket(min, max, quantity):
    random_numbers = set()
    if min >= 1 and max <= 1000:
        for count in range(1, quantity+1):
            random_numbers.add(random.randint(min, max))
        random_numbers = list(random_numbers)
        random_numbers.sort()
        return random_numbers
    else:
        random_numbers = list(random_numbers)
        return random_numbers


lottery_numbers = get_numbers_ticket(1, 49, 16)
print("Ваші лотерейні числа:", lottery_numbers)