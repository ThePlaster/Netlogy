
try:
    print('Это программа вычеслений в формате польской нотации!')
    print('Введите знак(+,-,*,/), а затем два числа')
    command, num_1, num_2 = input('Введите выражение: ').split(' ')

except ValueError:
  print('Вы ввели не правильное число аргументов!')


try:
    assert command == '+' or command == '-' \
        or command == '*' or command == '/', \
        'Программа поддерживает только опперации "+", "-", "*", "/"'
    if command == '+':
        num_result = int(num_1) + int(num_2)
    if command == '-':
        num_result = int(num_1) - int(num_2)
    if command == '*':
        num_result = int(num_1) * int(num_2)
    if command == '/':
        num_result = int(num_1) / int(num_2)

except NameError:
    print('Ошибка, операция не найдена.')

except ZeroDivisionError:
    print('На ноль делить нельзя!')

except ValueError:
    print('Вы ввели некоректные данные!')

try:
    print('Результат:', num_1, command, num_2, '=', num_result)

except NameError:
    print('Ненайден ответ, вы ввели некорректные данные')