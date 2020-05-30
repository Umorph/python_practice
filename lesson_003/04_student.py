# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000

i = 0
total_amount_request = 0
while i < 10:
    # Считаем сколько не хватает
    loan_amount = expenses - educational_grant
    total_amount_request += loan_amount
    # Теперь считаем рост цен
    expenses = expenses * 1.03
    i += 1
print('Студенту надо попросить', round(total_amount_request), 'рублей')