# Вам доступен csv файл grades.csv, имеющий следующее содержание:

# name;grade
# Timur;100
# Ruslan;97
# Ниже представлена программа, которая должна открывать данный файл и выводить
# содержимое каждой строки в виде списка. В программе допущена ошибка, поэтому
# она выводит:

# ['n']
# ['a']
# ['m']
# ['e']
# ['', '']
# ['g']
# ['r']
# ['a']
# ['d']
# ['e']
# []
# ['T']
# ...

# Найдите и исправьте ее, чтобы результатом работы программы были строки:

# ['name', 'grade']
# ['Timur', '100']
# ['Ruslan', '97']

import csv

with open('grades.csv', encoding='utf-8') as csv_file:
    rows = csv.reader(csv_file, delimiter=';')
    for row in rows:
        print(row)
    


# При попытке выполнить приведенную ниже программу возникает ошибка. Найдите
# и исправьте ее, чтобы программа создала файл writing_test.csv, имеющий
# следующее содержание:

# first_col,second_col
# value1,value2

import csv

with open('writing_test.csv', 'w', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=['first_col', 'second_col'])
    writer.writeheader()
    writer.writerows([{'first_col': 'value1', 'second_col': 'value2'}])



# Скидки
# Наступил ноябрь, и во многих магазинах начались распродажи, но как многим известно,
# зачастую товары со скидкой оказываются дороже, чем без нее. Вам доступен файл
# sales.csv, который содержит данные о ценообразовании различной бытовой техники.
# В первом столбце записано название товара, во втором — старая цена, в третьем —
# новая цена со скидкой:

# name;old_price;new_price
# Встраиваемая посудомоечная машина De'Longhi DDW 06S;23089;31862
# Вытяжка Falmec Afrodite 60/600;27694;18001
# ...

# Напишите программу, которая выводит названия тех товаров, цена на которые уменьшилась.
# Товары должны быть расположены в своем исходном порядке, каждый на отдельной строке.

# Примечание 1. Разделителем в файле sales.csv является точка с запятой, при этом
# кавычки не используются.

# Примечание 2. Начальная часть ответа выглядит так:

# Вытяжка Falmec Afrodite 60/600
# Духовой шкаф AEG BS 5836600
# Вытяжка MAUNFELD PLYM 60
# ...

import csv

with open('sales.csv', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=';', quotechar='"')
    expensive = list(filter(lambda r: int(r['old_price']) > int(r['new_price']), rows))
    for cost in expensive:
        print(cost['name'])



# Сортировка по столбцу
# Вам доступен файл deniro.csv, каждый столбец которого содержит либо только числа,
# либо только слова:

# Machete,2010,72
# Marvin's Room,1996,80
# Raging Bull,1980,97
# ...

# Напишите программу, которая сортирует содержимое данного файла по указанному столбцу.
# Причем данные должны быть отсортированы в порядке возрастания чисел, если столбец
# содержит числа, и в лексикографическом порядке слов, если столбец содержит слова.

# Формат входных данных
# На вход программе подается натуральное число — номер столбца файла deniro.csv.

# Формат выходных данных
# Программа должна отсортировать содержимое файла deniro.csv по введенному столбцу и
# вывести полученный результат в исходном формате.

# Примечание 1. Нумерация столбцов начинается с единицы.

# Примечание 2. Например, если бы файл deniro.csv имел вид:

# red,4
# blue,3
# green,28
# purple,1

# и его требовалось отсортировать по второму столбцу (в порядке возрастания чисел), то
# программа должна была бы вывести:

# purple,1
# blue,3
# red,4
# green,28

# Примечание 3. Если две какие-либо строки имеют одинаковые значения в столбцах, то
# следует сохранить их исходный порядок следования.

# Примечание 4. Разделителем в файле deniro.csv является запятая, при этом кавычки не
# используются.

import csv

with open('deniro.csv', encoding='utf-8') as file:
    number_column = int(input()) - 1
    reader = list(csv.reader(file, delimiter=','))
    if reader[0][number_column].isdigit():
        sorted_reader = sorted(reader, key=lambda row: int(row[number_column]))
        for row in sorted_reader:
            print(','.join(row))
    else:
        sorted_reader = sorted(reader, key=lambda row: row[number_column])
        for row in sorted_reader:
            print(','.join(row))
            
            
            
# Голодный студент 🌶️
# Дима очень хочет поесть, но денег у него мало. Помогите ему определить самый дешевый продукт, 
#  также магазин, в котором он продается. Вам доступен файл prices.csv, который содержит информацию
# о ценах продуктов в различных магазинах. В первом столбце записано название магазина, а в
# последующих — цена на соответствующий товар в этом магазине:

# Магазин;Творог;Гречка;Рис;Бородинский хлеб;Яблоки;Пельмени;Овсяное печенье;Спагетти;Печеная
# фасоль;Мороженое;Фарш;Вареники;Картофель;Батончик
# Пятерочка;69;133;129;83;141;90;72;123;149;89;88;106;54;84
# Магнит;102;87;95;75;109;112;97;82;101;134;69;61;141;79
# ...

# Напишите программу, которая определяет и выводит самый дешевый продукт и название магазина, в
# котором он продается, в следующем формате:

# <название продукта>: <название магазина>

# Если имеется несколько самых дешевых товаров, то следует вывести тот товар, чье название
# меньше в лексикографическом сравнении. Если один товар продается в нескольких магазинах по одной
# минимальной цене, то следует вывести тот магазин, чье название меньше в лексикографическом
# сравнении.

# римечание 1. Разделителем в файле prices.csv является точка с запятой, при этом кавычки не
# используются.

# римечание 2. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.

# Примечание 3. Пример вывода:

# Клубничный йогурт: ВкусВилл

import csv


with open('D:/Python/Stepik/prices.csv', encoding='utf-8') as file:
    file_reader = csv.DictReader(file, delimiter=';')
    shops_dict = {}
    prices_cheap_products = {}
    
    for dct in file_reader:
        shops_dict[dct['Магазин']] = shops_dict.get(dct['Магазин'], {})
        for product, price in dct.items():
            if product == 'Магазин':
                continue
            shops_dict[dct['Магазин']][int(price)] = shops_dict[dct['Магазин']].get(int(price), []) + [product]

    for shop, products in shops_dict.items():
        prices_cheap_products[shop] = prices_cheap_products.get(min(product), []) + [min(products), *products[min(products)]]

    cheapest_product = min(prices_cheap_products.items(), key=lambda x: x[1][0])
    print(f'{cheapest_product[1][1]}: {cheapest_product[0]}')
