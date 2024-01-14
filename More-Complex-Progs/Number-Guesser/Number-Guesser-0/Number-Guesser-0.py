from random import randint


def is_valid(value):
    if value in [str(i) for i in range(1, 101)]:
        return True
    else:
        return False


n = randint(1, 100)

print("Добро пожаловать в числовую угадайку")

while True:
    attempt = input()

    if not is_valid(attempt):
        print("А может быть все-таки введем целое число от 1 до 100?")
        continue

    attempt = int(attempt)

    if attempt > n:
        print("Ваше число больше загаданного, попробуйте еще разок")
        continue
    elif attempt < n:
        print("Ваше число меньше загаданного, попробуйте еще разок")
        continue
    else:
        print("Вы угадали, поздравляем!")
        break

print("Спасибо, что играли в числовую угадайку. Еще увидимся...")

