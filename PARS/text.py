def count_numbers(number):
    numbers = str(number)
    if len(numbers) == 8:
        return True
    else:
        return False
print(count_numbers(13414123))