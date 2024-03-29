# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом

month_numbers = {
    1: 'Январь',
    2: 'Февраль',
    3: 'Март',
    4: 'Апрель',
    5: 'Май',
    6: 'Июнь',
    7: 'Июль',
    8: 'Август',
    9: 'Сентябрь',
    10: 'Октябрь',
    11: 'Ноябрь',
    12: 'Декабрь'
}

amount_of_days = {
    'Январь': 31,
    'Февраль': 28,
    'Март': 31,
    'Апрель': 30,
    'Май': 31,
    'Июнь': 30,
    'Июль': 31,
    'Август': 31,
    'Сентябрь': 30,
    'Октябрь': 31,
    'Ноябрь': 30,
    'Декабрь': 31
}

user_input = input('Введите, пожалуйта, номер месяца: ')
print('Проверяю валидность типа введеных данный')
if user_input.isnumeric():
    print('Тип данных валиден, продолжаю работу')
    month = int(user_input)
    print('Проверяю корректность номера месяца')
    if 1 <= month <= 12:
        print('Данные верны, продолжаю работу')
        month_name = month_numbers.get(month)
        month_days = amount_of_days.get(month_name)
        print('Месяц -', month_name, 'Количество дней -', month_days)
    else:
        print('Данные неверны, введите корректный номер месяца (от 1 до 12)')
else:
    print('Введеные тип данных некорректен, пожалуйста, введите номер месяца')
