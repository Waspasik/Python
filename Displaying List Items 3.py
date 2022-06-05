#На вход программе подается натуральное число nn, затем nn строк, затем число kk — количество поисковых запросов, затем kk строк — поисковые запросы. Напишите программу, которая выводит все введенные строки, в которых встречаются все поисковые запросы.

#Формат входных данных
#На вход программе подаются натуральное число nn — количество строк, затем сами строки в указанном количестве, затем число kk, затем сами поисковые запросы.

#Формат выходных данных
#Программа должна вывести все введенные строки, в которых встречаются все поисковые запросы.

#Примечание. Поиск не должен быть чувствителен к регистру символов.

n = int(input())
strings = []
for num in range(n):
    string = input()
    strings.append(string)
k = int(input())
requests = []
for r in range(k):
    request = input()
    requests.append(request)
required_request = []
for i in strings:
    counter = 0
    for j in requests:
        if j.lower() in i.lower():
            counter += 1
        if counter == k:
            required_request.append(i)
print(*required_request, sep='\n')