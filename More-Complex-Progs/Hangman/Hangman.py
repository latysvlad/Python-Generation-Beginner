from random import choice


# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


# функция случайного выбора слова
def get_word():
    return choice(word_list)


# функция игры
def play(word):
    # Основные переменные
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток

    print("Давайте играть в угадайку слов!")

    # Вывод текущего состояния игры
    print(display_hangman(tries))
    print(word_completion)

    while True:
        # Попытка угадывания
        print("Введите букву или слово целиком")
        guess = input().lower()

        # Проверка на корректность ввода
        if not guess.isalpha():
            print("Не, надо ввести что-то буквенное")
            continue

        # Проверка, была ли уже введена эта буква/это слово
        if guess in guessed_letters or guess in guessed_words:
            print("Не, такой вариант уже пробовали")
            continue

        # Обработка угадывания буквы
        if len(guess) > 1:
            if guess == word:
                guessed = True
                word_completion = guess
            else:
                print("Вы не угадали слово :-(")
                tries -= 1

            guessed_words.append(guess)
        else:
            if guess in word:
                char_list = list(word_completion)
                word_completion = "".join([guess if word[i] == guess else char_list[i] for i in range(len(char_list))])
            else:
                print("Вы не угадали букву :-(")
                tries -= 1

            guessed_letters.append(guess)
            if word_completion == word:
                guessed = True

        # Проверка на полностью отгаданное слово
        if guessed:
            print("Поздравляем, вы угадали слово! Вы победили!")
            break

        # Вывод текущего состояния игры
        print(display_hangman(tries))
        print(word_completion)

        if tries == 0:
            print("К сожалению вы проиграли. Загаданное слово:")
            print(word)
            break


word_list = ["автомобиль", "звезда", "компьютер", "дружба", "радость", "мечта", "парашют", "мозаика", "красота",
             "зеркало", "парковка", "коллекция", "путешествие", "комета", "семейство", "ландшафт", "магазин",
             "галактика", "процессор", "программа", "технология", "развлечение", "биология", "посещение", "электроника",
             "ресторан", "устройство", "коллега", "университет", "энергия", "композитор", "горизонт", "коммуникация",
             "философия", "эксперимент", "библиотека", "креативность", "реставрация", "реальность", "авантюра",
             "контингент", "оборудование", "производство", "конструкция", "гарантия", "исследование", "декларация",
             "информация", "организация", "коллектив", "компания", "потребление", "политика", "сообщество", "ресурс",
             "операция", "концепция", "комплекс", "реакция", "социология", "продукция", "генерация", "интеграция",
             "активность", "композиция", "категория", "идентификация"]

word = get_word()
print(len(word_list))
play(word)
