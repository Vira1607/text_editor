print('Текстовый редактор')

# Мы продолжаем разрабатывать новый текстовый редактор,
# и в этот раз нам поручили написать для него код,
# который считает количество любой буквы
# и любой цифры в тексте (а не только буквы Ы как раньше).
#
# Функция count_letters принимает на вход текст и подсчитывает,
# какое в нём количество цифр K и букв N.
#
# Функция выводит на экран информацию
# о найденных буквах и цифрах в определенном формате.
#
# Пример:
# Введите текст: 100 лет в обед
# Какую цифру ищем? 0
# Какую букву ищём? л
#
# Количество цифр 0: 2
# Количество букв л: 1

def count_letters(a, b):
  counter = 0
  for symbol in a:
    if symbol == b:
      counter += 1
  return counter

text = input('Введите текст: ').lower()
symbol_digit = input('Какую цифру ищем? ')
symbol_letter = input('Какую букву ищём? ').lower()

number_of_digits = count_letters(text, symbol_digit)
number_of_letters = count_letters(text, symbol_letter)

print(f'\nКоличество цифр {symbol_digit}: {number_of_digits}')
print(f'Количество букв {symbol_letter}: {number_of_letters}')
