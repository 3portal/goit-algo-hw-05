import re

from typing import Callable

# функція для ідентифікації дійсних чесел
def generator_numbers(text: str):
    if text is not None and text != '':
        list_of_words_drom_text = text.split(" ")
        pattern = r"([0-9]+\.?[0-9]?)"
        for str_in_list in list_of_words_drom_text:
            if re.search(pattern, str_in_list) is not None:
                yield str_in_list

# функція для обчислення загальної суми чисел
def sum_profit(text: str, func: Callable) -> float:
    all_sum = 0
    for digit in func(text):       
        all_sum += float(digit)
    return all_sum
   
# Обчислення загального прибутку згідно прикладу використання

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")