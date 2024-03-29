15.7 Угадайка слов.

## Угадайка слов (Ну или по-русски - виселица) ##

**Описание проекта:** программа загадывает слово, а пользователь должен его угадать. Изначально все буквы слова неизвестны. Также рисуется виселица с петлей. Пользователь предлагает букву,
которая может входить в это слово. Если такая буква есть в слове, то программа ставит букву столько раз, сколько она встречается в слове. Если такой буквы нет, к виселице добавляется круг в петле,
изображающий голову. Пользователь продолжает отгадывать буквы до тех пор, пока не отгадает всё слово. За каждую неудачную попытку добавляется еще одна часть туловища висельника (обычно их 6: голова,
туловище, 2 руки и 2 ноги).

**Составляющие проекта:**

  - Целые числа (тип int);
  - Переменные;
  - Ввод / вывод данных (функции input() и print());
  - Условный оператор (if/elif/else);
  - Цикл while;
  - Бесконечный цикл
  - Операторы break, continue
  - Написание пользовательских функций;
  - Работа с модулем random для генерации случайных чисел.

**Заголовок программы**

  1. Подключите модуль random;
  2. Создайте глобальный список word_list, содержащий слова, которые будут использоваться в игре.

**Функция, возвращающая случайное слово**

Напишите функцию get_word() которая возвращает случайное слово из списка word_list в ~~верхнем~~(*я делал в нижнем*) регистре.

**Функция, возвращающая текущее состояние**

Функция display_hangman() принимает один аргумент tries – количество попыток угадывания слова – и возвращает текущее состояние игры в графическом виде:

  - значение tries = 6 соответствует начальному положению, пустая виселица;
  - ...
  - значение tries = 0 соответствует конечному положению, то есть проигрышу и полностью нарисованному телу повешенного.

Примечание. Для вывода символа бэкслеша \ используется экранирование символа с помощью \, то есть комбинация \\.

**Функция play()**

Напишите функцию play(), в которой будет осуществляться основная логика игры. Функция play() принимает в качестве аргумента слово word, сгенерированное функцией  get_word().

    def play(word):
      # тело функции

Используйте следующие локальные переменные:

    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False                    # сигнальная метка
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6                          # количество попыток

  1. Функция play() в самом начале должна:
      - отобразить текст 'Давайте играть в угадайку слов!';
      - отобразить текущее состояние игры, распечатав результат вызова функции display_hangman() с начальным количеством допустимых промахов tries = 6;
      - отобразить начальное слово word_completion в виде строки с символом _ на каждую букву задуманного слова;
  2. Необходимо обрабатывать ввод букв или слова целиком. Предусмотрите защиту от дурака, на случай если пользователь ввел символ, не являющийся буквой;
  3. Если пользователь вводит уже названную букву или слово, то необходимо ему об этом сообщить, и не засчитывать попытку;
  4. Если пользователь угадал букву, то требуется заменить все символы _ соответствующие этой букве;
  5. Если пользователь угадал слово целиком, то следует его поздравить и вывести текст 'Поздравляем, вы угадали слово! Вы победили!';
  6. Если пользователь исчерпал все свои попытки и не угадал слово, следует вывести загаданное слово.
