from random import choice


def get_num_of_passwords():
    while True:
        value = input()
        if not value.isdigit():
            print("Введенное число паролей должно быть целым неотрицательным")
            continue
        else:
            return int(value)


def get_len_of_passwords():
    while True:
        value = input()
        if not value.isdigit() or not int(value):
            print("Введенная длина паролей должна быть натуральным числом")
            continue
        else:
            return int(value)


def to_include_request(symbol_type, symbols):
    while True:
        print(f"Включать ли {symbol_type} {symbols}?")
        response = input()
        if response.lower() in ["да", "yes", "д", "y"]:
            return True
        elif response.lower() in ["нет", "no", "н", "n"]:
            return False
        else:
            print("Простите, я Вас не понял.", end=" ")
            continue


def to_exclude_request():
    while True:
        print(f"Исключать ли неоднозначные символы {ambiguous_symbols}?")
        response = input()
        if response.lower() in ["да", "yes", "д", "y"]:
            return True
        elif response.lower() in ["нет", "no", "н", "n"]:
            return False
        else:
            print("Простите, я Вас не понял.", end=" ")
            continue


def generate_password(length, symbols):
    password = ""
    for _ in range(length):
        password += choice(symbols)
    return password


digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
symbol_types = ["цифры", "строчные буквы", "прописные буквы", "символы"]
symbols_list = [digits, lowercase_letters, uppercase_letters, punctuation]
ambiguous_symbols = "il1Lo0O"
chars = ''

print("Введите число паролей для генерации")
num = get_num_of_passwords()
if num:
    print("Введите желаемую длину генерируемых паролей")
    password_length = get_len_of_passwords()
    for i in range(len(symbol_types)):
        if to_include_request(symbol_types[i], symbols_list[i]):
            chars += symbols_list[i]
    else:
        if to_exclude_request():
            for c in ambiguous_symbols:
                chars = chars.replace(c, "")
    for i in range(num):
        print(generate_password(password_length, chars))
else:
    print("Ну, нет так нет.")
