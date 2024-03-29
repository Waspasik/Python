# Корпоративная почта 🌶️
# В онлайн-школе "BEEGEEK" сотрудникам положена корпоративная почта, которая
# формируется как <имя-фамилия>@beegeek.bzz, например, timyr-guev@beegeek.bzz.
# При таком подходе существует проблема тёзок. Для решения такой проблемы было
# решено приписывать справа номер.

# Тогда первый Тимур Гуев получает ящик timyr-guev@beegeek.bzz (без номера),
# второй — timyr-guev1@beegeek.bzz, третий — timyr-guev2@beegeek.bzz, и так далее.

# Вам дан список уже занятых ящиков в порядке их выдачи и имена-фамилии новых
# сотрудников в заранее подготовленном виде (латиницей с символом - между ними).
# Напишите программу, которая раздает корпоративные ящики новым сотрудникам школы.

# Формат входных данных
# На вход программе в первой строке подается целое неотрицательное число n —
# количество выданных ящиков. В следующих n строках перечислены сами ящики в
# порядке выдачи, по одному на строке. На следующей строке задано целое
# неотрицательное число m — количество новых сотрудников, которым нужно раздать
# корпоративные ящики. Каждая из последующих m строк представляет собой имя и
# фамилию сотрудника в подготовленном к использованию формате.

# Формат выходных данных
# Программа должна вывести почтовые ящики (m строк) для новых сотрудников в том
# порядке, в котором они раздавались.

from string import digits

mailbox_names = [input().split('@')[0] for _ in range(int(input()))]
new_users_mailbox = []

for _ in range(int(input())):
    new_name = input()
    counter = 1
    while new_name in mailbox_names:
        new_name = new_name.rstrip(digits) + str(counter)
        counter += 1
    mailbox_names.append(new_name)
    new_name = new_name + '@beegeek.bzz'
    new_users_mailbox.append(new_name)

print(*new_users_mailbox, sep='\n')