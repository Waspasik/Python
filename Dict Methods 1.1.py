# Дополните приведенный код, чтобы в переменной result хранился словарь, в котором ключи –
# числа от 1 до 15 (включительно), а значения представляют собой квадраты ключей.

# Примечание. Выводить содержимое словаря result не нужно.

result = {}

for i in range(1, 16):
    result[i] = i**2



# Дополните приведенный код так, чтобы он объединил содержимое двух словарей dict1 и dict2
# по ключам, складывая значения по одному и тому же ключу, в случае, если ключ присутствует
# в обоих словарях. Результирующий словарь необходимо присвоить переменной result.

# Примечание. Выводить содержимое словаря result не нужно.

dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

result = dict1.copy()

for key, value in dict2.items():
    result[key] = result.get(key, 0) + value



# Дополните приведенный код так, чтобы в переменной result хранился словарь, в котором для
# каждого символа строки text будет подсчитано количество его вхождений.

# Примечание. Выводить содержимое словаря result не нужно.

text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'

result = {}

for char in text:
    result[char] = result.get(char, 0) + 1



# Дополните приведенный код, чтобы он вывел наиболее часто встречающееся слово строки s.
# Если таких слов несколько, должно быть выведено то, что меньше в лексикографическом порядке.

s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'

count_dict = {}
result = {}

for word in s.split():
    count_dict[word] = count_dict.get(word, 0) + 1

for key in count_dict:
    if count_dict[key] == max(count_dict.values()):
        result[key] = result.get(key)

print(min(result))