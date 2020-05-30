#!/usr/bin/env python
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =
garden_set = set(garden)
meadow_set = set(meadow)

# выведите на консоль все виды цветов
all_plants_set = garden_set | meadow_set
print(all_plants_set)

# выведите на консоль те, которые растут и там и там
common_plans_set = garden_set & meadow_set
print(common_plans_set)

# выведите на консоль те, которые растут в саду, но не растут на лугу
garden_unique_set = garden_set - meadow_set
print(garden_unique_set)

# выведите на консоль те, которые растут на лугу, но не растут в саду
# TODO здесь ваш код


