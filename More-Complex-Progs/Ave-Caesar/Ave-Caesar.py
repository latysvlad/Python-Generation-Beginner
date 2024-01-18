alphabet = 'abcdefghijklmnopqrstuvwxyz'

s_old = input()
words = s_old.split()  # разбиваем строку на слова

s_new = ""
for word in words:
    shift = sum([int(letter.lower() in alphabet) for letter in word])  # считаем длину каждого слова

    for letter in word:
        if letter in alphabet:  # проверяем, что это строчная буква
            old_letter_position = alphabet.index(letter)
            letter = alphabet[(old_letter_position + shift) % 26]

        elif letter.lower() in alphabet:  # проверяем, что это прописная буква
            old_letter_position = alphabet.index(letter.lower())
            letter = alphabet[(old_letter_position + shift) % 26].upper()

        s_new += letter

    s_new += " "

print(s_new)
