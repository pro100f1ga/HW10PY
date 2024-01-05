# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()

import random
import pandas as pd

# Генерация данных: создаем список, состоящий из 10 строк 'robot' и 10 строк 'human'
lst = ['robot'] * 10 + ['human'] * 10

# Перемешиваем элементы списка случайным образом
random.shuffle(lst)

# Создаем DataFrame с одним столбцом 'whoAmI' и заполняем его значениями из списка
data = pd.DataFrame({'whoAmI': lst})

# Преобразование в one-hot вид: создаем новые столбцы с префиксом 'whoAmI' для каждой уникальной категории
one_hot_data = pd.get_dummies(data['whoAmI'], prefix='whoAmI')

# Объединение исходного DataFrame с one-hot представлением: добавляем столбцы one-hot к исходному DataFrame
data_one_hot = pd.concat([data, one_hot_data], axis=1)

# Вывод результата: отображаем первые несколько строк нового DataFrame
print(data_one_hot.head())
