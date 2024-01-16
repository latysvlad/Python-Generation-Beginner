15.3 Магический шар 8.

## Магический шар 8 ##

**Описание проекта:** магический шар 8 (шар судьбы) — шуточный способ предсказывать будущее. Программа должна просить пользователя задать некий вопрос, чтобы случайным образом на него ответить.

**Составляющие проекта:**

  - Целые числа (тип int);
  - Переменные;
  - Ввод / вывод данных (функции input() и print());
  - Условный оператор (if/elif/else);
  - Цикл while;
  - Бесконечный цикл;
  - Операторы break, continue;
  - Работа с модулем random для генерации случайных чисел.

**Варианты ответов**

Традиционно шар имеет 20 ответов, которые можно разделить на четыре группы.
| Положительные  | Нерешительно положительные | Нейтральные  | Отрицательные |
| ------------- | ------------- | ------------- | ------------- |
| Бесспорно  | Мне кажется - да  | Пока неясно, попробуй снова  | Даже не думай  |
| Предрешено  | Вероятнее всего  | Спроси позже  | Мой ответ - нет  |
| Никаких сомнений  | Хорошие перспективы  | Лучше не рассказывать  | По моим данным - нет  |
| Определённо да  | Знаки говорят - да  | Сейчас нельзя предсказать  | Перспективы не очень хорошие  |
| Можешь быть уверен в этом  | Да  | Сконцентрируйся и спроси опять  | Весьма сомнительно  |
            
**Заголовок программы**

  1. Подключите модуль random;
  2. Создайте список answers, содержащий 20 потенциальных ответов (Бесспорно, Предрешено, и т.д.).
            
**Приветствие пользователя**

  1. Выведите текстовое сообщение: 'Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.';
  2. Уточните как зовут пользователя;
  3. Выведите слова приветствия, например, 'Привет Тимур'.

**Основной цикл программы**

  1. Организуйте цикл, который будет запрашивать у пользователя данные;
  2. Запросите у пользователя вопрос;
  3. Выведите случайный ответ с помощью функции choice() передав список answers в качестве аргумента;
  4. Уточните у пользователя, хочет ли он задать еще один вопрос, если да, то вернитесь в основной цикл программы, если нет выведите сообщение 'Возвращайся если возникнут вопросы!' и завершите программу.