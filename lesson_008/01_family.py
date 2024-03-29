# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint

# Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.money_count = 100
        self.food_in_fridge = 50
        self.house_mess = 0
        self.cat_food = 30

    def __str__(self):
        return f'Денег в доме - {self.money_count}, еды в холодильнике - {self.food_in_fridge}, ' \
               f'грязи в доме - {self.house_mess}, кошачьей еды - {self.cat_food}'

    def get_dirty(self):
        self.house_mess += 5


class Cat:

    def __init__(self, name, house):
        self.house = house
        self.name = name
        self.fullness = 30

    def __str__(self):
        return 'Котейка {}, сытость {}'.format(self.name, self.fullness)

    def eat(self):
        if self.house.cat_food >= 10:
            self.fullness += 20
            self.house.cat_food -= 10
            print(f'{self.name} ест корм')
        elif 0 < self.house.cat_food < 10:
            self.fullness += self.house.cat_food * 2
            self.house.cat_food -= self.house.cat_food
            print(f'{self.name} доедает остатки корма')
        else:
            self.fullness -= 10
            print(f'{self.name} сегодня голодает, корма нет')

    def sleep(self):
        self.fullness -= 10
        print(f'{self.name} котяшится на кровати')

    def soil(self):
        self.fullness -= 10
        self.house.house_mess -= 5
        print(f'{self.name} дерет обои')

    def act(self):
        if self.fullness == 0:
            return f'{self.name} погибает от голода'
        elif self.fullness <= 20:
            self.eat()
        else:
            dice = randint(1, 6)
            if dice == 1 or dice == 3:
                self.eat()
            elif dice == 2 or dice == 4:
                self.sleep()
            else:
                self.soil()


class Human:

    def __init__(self, name, house):
        self.house = house
        self.name = name
        self.fullness = 30
        self.happiness = 100

    def __str__(self):
        return '{}, сытость - {}, счастье - {}'.format(self.name, self.fullness, self.happiness)

    def eat(self):
        if self.house.food_in_fridge >= 30:
            self.fullness += 30
            self.house.food_in_fridge -= 30
            print('{} ест'.format(self.name))
        elif 0 < self.house.food_in_fridge < 30:
            self.fullness += House().food_in_fridge
            self.house.food_in_fridge -= self.house.food_in_fridge
            print('{} доедает остатки еды из холодильника'.format(self.name))
        else:
            self.fullness -= 10
            print('{} пропускает прием пищи'.format(self.name))

    def act(self):
        if self.fullness <= 0:
            print('{} погибает от голода'.format(self.name))
        elif self.happiness < 10:
            print('{} погибает от депрессии'.format(self.name))
        else:
            pass


class Husband(Human):

    def __init__(self, name, house):
        super().__init__(name=name, house=house)

    def __str__(self):
        return super().__str__()

    def work(self):
        self.fullness -= 10
        self.house.money_count += 150
        print('{} пошел на работу'.format(self.name))

    def gaming(self):
        self.fullness -= 10
        self.happiness += 20
        print('{} катает в танки'.format(self.name))

    def act(self):
        super().act()
        if self.fullness < 30:
            self.eat()
        elif self.house.money_count < 50:
            self.work()
        elif self.happiness < 30:
            self.gaming()
        else:
            dice = randint(1, 6)
            if dice == 1 or dice == 3:
                self.work()
            elif dice == 2 or dice == 4:
                self.eat()
            else:
                self.gaming()


class Wife(Human):

    def __init__(self, name, house):
        super().__init__(name=name, house=house)

    def __str__(self):
        return super().__str__()

    def shopping(self):
        if self.house.money_count >= 200:
            self.fullness -= 10
            self.house.food_in_fridge += 150
            self.house.cat_food += 50
            self.house.money_count -= 200
            print('{} закупает много еды'.format(self.name))
        elif 0 < self.house.money_count < 150:
            self.fullness -= 10
            self.house.food_in_fridge += self.house.money_count
            self.house.money_count -= self.house.money_count
            print('{} покупает еды на остатки денег'.format(self.name))

    def buy_fur_coat(self):
        self.fullness -= 10
        self.house.money_count -= 350
        self.happiness += 60
        print('{} идет в бершку и покупает себе шубу'.format(self.name))

    def clean_house(self):
        if self.house.house_mess >= 100:
            self.fullness -= 10
            self.house.house_mess -= 100
            print('{} убирается в квартире'.format(self.name))
        elif 0 <= self.house.house_mess < 100:
            self.fullness -= 10
            self.house.house_mess -= self.house.house_mess
            print('{} немного прибирается'.format(self.name))

    def act(self):
        super().act()
        if self.fullness < 30:
            self.eat()
        elif self.house.house_mess > 100:
            self.clean_house()
        elif self.house.money_count >= 350 and self.happiness < 40:
            self.buy_fur_coat()
        elif self.house.food_in_fridge < 50 or self.house.cat_food <= 0:
            self.shopping()
        else:
            dice = randint(1, 6)
            if dice == 1 or dice == 3 and self.house.house_mess > 0:
                self.clean_house()
            elif dice == 2 or dice == 4 and self.house.money_count > 0:
                self.shopping()
            elif dice == 5 and self.house.money_count >= 350:
                self.buy_fur_coat()
            else:
                self.eat()


class Child(Human):
    def __init__(self, name, house):
        super().__init__(name=name, house=house)

    def __str__(self):
        return super().__str__()

    def eat(self):
        if self.house.food_in_fridge >= 10:
            self.fullness += 10
            self.house.food_in_fridge -= 10
            print('{} ест'.format(self.name))
        elif 0 < self.house.food_in_fridge < 10:
            self.fullness += House().food_in_fridge
            self.house.food_in_fridge -= self.house.food_in_fridge
            print('{} доедает остатки еды из холодильника'.format(self.name))
        else:
            self.fullness -= 10
            print('{} пропускает прием пищи'.format(self.name))

    def sleep(self):
        self.fullness -= 10
        print(f'{self.name} наелся и спит')

    def act(self):
        if self.fullness <= 30:
            self.eat()
        else:
            self.sleep()


home = House()
serge = Husband(name='Сережа', house=home)
masha = Wife(name='Маша', house=home)
lexus = Child(name='Лексус', house=home)
eva = Cat(name='Ева', house=home)
motya = Cat(name='Мотя', house=home)
aloiz = Cat(name='Алойз', house=home)
murzik = Cat(name='Мурзик', house=home)

for day in range(1, 366):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    lexus.act()
    eva.act()
    motya.act()
    aloiz.act()
    murzik.act()
    home.get_dirty()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(lexus, color='cyan')
    cprint(eva, color='cyan')
    cprint(motya, color='cyan')
    cprint(aloiz, color='cyan')
    cprint(murzik, color='cyan')
    cprint(home, color='cyan')

# Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
