15.4 Генератор безопасных паролей.

## Генератор безопасных паролей ##

**Описание проекта:** программа генерирует заданное количество паролей и включает в себя умную настройку на длину пароля, а также на то, какие символы требуется в него включить, а какие исключить.

**Составляющие проекта:**

  - Целые числа (тип int);
  - Переменные;
  - Ввод / вывод данных (функции input() и print());
  - Условный оператор (if/elif/else);
  - Цикл for;
  - Написание пользовательских функций;
  - Работа с модулем random для генерации случайных чисел.

**Заголовок программы**

  1. Подключите модуль random;
  2. Создайте строковые константы:
     
     - digits: 0123456789;
     - lowercase_letters: abcdefghijklmnopqrstuvwxyz;
     - uppercase_letters: ABCDEFGHIJKLMNOPQRSTUVWXYZ;
     - punctuation: !#$%&*+-=?@^_.
    
  3. Создайте переменную chars = '', которая будет содержать все символы, которые могут быть в генерируемом пароле.
            
**Считывание пользовательских данных**

  1. Количество паролей для генерации;
  2. Длину одного пароля;
  3. Включать ли цифры 0123456789?
  4. Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?
  5. Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?
  6. Включать ли символы !#$%&*+-=?@^_?
  7. Исключать ли неоднозначные символы il1Lo0O?

**Настройка генерируемых паролей**

На основании введенной пользователем информации, сформируйте переменную chars, содержащую все символы, которые могут быть в генерируемом пароле.

**Генерации пароля**

Напишите функцию generate_password(), которая принимает два аргумента:

- length: длину пароля;
- chars: алфавит из символов которого состоит пароль;

и возвращает пароль.

Используя цикл for, сгенерируйте необходимое количество паролей.
