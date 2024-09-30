#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# random_letters = []
# for number in range(0, nr_letters):
#     random_letter = letters[random.randint(0, len(letters) - 1)]
#     random_letters.append(random_letter)
#
# random_symbols = []
# for number in range(0, nr_symbols):
#     random_symbol = symbols[random.randint(0, len(symbols) - 1)]
#     random_symbols.append(random_symbol)
#
# random_numbers = []
# for number in range(0, nr_numbers):
#     random_number = numbers[random.randint(0, len(numbers) - 1)]
#     random_numbers.append(random_number)


characters = ["letter", "symbol", "number"]
letter_count = 0
symbol_count = 0
number_count = 0

password_length = nr_letters + nr_symbols + nr_numbers
password = ""

if nr_letters == 0:
    characters.remove("letter")
if nr_symbols == 0:
    characters.remove("symbol")
if nr_numbers == 0:
    characters.remove("number")

for number in range(0, password_length):
    character = characters[random.randint(0, len(characters) - 1)]

    if character == "letter" and letter_count < nr_letters:
        password += random.choice(letters)
        letter_count += 1
        if letter_count == nr_letters:
            characters.remove("letter")
    elif character == "symbol" and symbol_count < nr_symbols:
        password += random.choice(symbols)
        symbol_count += 1
        if symbol_count == nr_symbols:
            characters.remove("symbol")
    elif character == "number" and number_count < nr_numbers:
        password += random.choice(numbers)
        number_count += 1
        if number_count == nr_numbers:
            characters.remove("number")

print(f"Your password is: {password}")