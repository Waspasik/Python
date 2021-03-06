# Китайский гороскоп назначает животным годы в 1212-летнем цикле.
# Напишите программу, которая считывает год и отображает название связанного с ним животного.
# Ваша программа должна корректно работать с любым годом, не только теми, что перечислены в таблице.

# Формат входных данных
# На вход программе подается одно целое число – год.

# Формат выходных данных
# Программа должна вывести текст – название животного.

year = int(input())
animals = ['Обезьяна', 'Петух', 'Собака', 'Свинья', 'Крыса', 'Бык', 'Тигр', 'Заяц', 'Дракон', 'Змея', 'Лошадь', 'Овца']
print(animals[year % 12])



# Дано пятизначное или шестизначное натуральное число. Напишите программу, которая изменит порядок
# его последних пяти цифр на обратный.

# Формат входных данных
# На вход программе подается одно натуральное пятизначное или шестизначное число.

# Формат выходных данных
# Программа должна вывести число, которое получится в результате разворота, указанного в условии
# задачи. Число нужно выводить без незначащих нулей.

n = int(input())
number = []
if 1 <= (n // 10000) < 10:
    m = 1
    for i in range(5):
        number.append(str(n // m % 10))
        m *= 10
    if number[0] == '0':
        for j in range(len(number)):
            if number[0] == '0':
                del number[0]
elif 1 <= (n // 100000) < 10:
    number.append(str(n // 100000))
    m = 1
    for i in range(5):
        number.append(str(n // m % 10))
        m *= 10
print(''.join(number))



# На вход программе подаётся натуральное число. Напишите программу, которая вставляет в заданное
# число запятые в соответствии со стандартным американским соглашением о запятых в больших числах.

# Формат входных данных
# На вход программе подаётся натуральное число n, (0 < n < 10^{100}).

# Формат выходных данных
# Программа должна вывести число с запятыми в соответствии с условием задачи.

n = int(input())
number = []
result = []

def insert(num):
    m = 1
    for i in range(len(str(num))):
        number.append(str(num // m % 10))
        m *= 10
    step = 0
    for j in range(3, len(number), 3):
        number.insert(j + step, ',')
        step += 1
    number.reverse()
    for l in range(len(number)):
        result.append(number[l])
    return print(''.join(result))

if len(str(n)) > 3:
    insert(n)
else:
    print(n)