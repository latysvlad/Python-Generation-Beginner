def input_encrypting_settings():
    print("Выберите направление шифрования:\n'+' - шифрование\n'-' - дешифрование?")
    while True:
        direction = input().lower()
        if direction != "+" and direction != "-":
            print("Выберите пожалуйста '+'(шифрование) или '-'(дешифрование)")
            continue
        else:
            break

    print("Введите шаг шифрования")
    while True:
        increment = input()
        if not increment.isdigit() or not increment:
            print("Введите натуральное число для определения шага шифрования")
            continue
        else:
            break

    print("Выберите используемый язык:\n'1' - английский\n'2' - русский")
    while True:
        language = input().lower()
        if language != "1" and language != "2":
            print("Выберите '1'(английский) или '2'(русский)")
            continue
        else:
            break

    return int(direction + increment), (int(language) - 1)


def encryption_algorithm(text):
    new_text = ""
    for c in to_the_input:
        if c.isalpha():
            new_c = chr(first_char + (ord(c.upper()) + step % mod - first_char) % mod)
            new_text += new_c if c.isupper() else new_c.lower()
        else:
            new_text += c
    return new_text


alph = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ']
step, lang = input_encrypting_settings()
mod = len(alph[lang])
first_char = ord(alph[lang][0])
to_the_input = input("Введите шифруемый/дешифруемый текст\n")
to_the_output = encryption_algorithm(to_the_input)
print(to_the_output)
