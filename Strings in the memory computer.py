#На вход программе подаются два числа aa и bb. Напишите программу, которая для каждого кодового значения в диапазоне от aa до bb (включительно), выводит соответствующий ему символ из таблицы символов Unicode.

#Формат входных данных 
#На вход программе подается два натуральных числа, каждое на отдельное строке.

#Формат выходных данных
#Программа должна вывести текст в соотвествии с условием задачи.

a, b = int(input()), int(input())
for i in range(a, b + 1):
    print(chr(i), end=' ')



#На вход программе подается строка текста. Напишите программу, которая переводит каждый ее символ в соответствующий ему код из таблицы символов Unicode.

#Формат входных данных 
#На вход программе подается строка текста.

#Формат выходных данных
#Программа должна вывести кодовые значения символов строки разделенных одним символом пробела.

s = input()
for i in range(len(s)):
    print(ord(s[i]), end=' ')



#Легион Цезаря, созданный в 23 веке на основе Римской Империи не изменяет древним традициям и использует шифр Цезаря. Это их и подвело, ведь данный шифр очень простой. Однако в постапокалипсисе люди плохо знают все тонкости довоенного мира, поэтому ученые из НКР не могут понять как именно нужно декодировать данные сообщения. Напишите программу для декодирования этого шифра.

#Формат входных данных
#В первой строке дается число n \, (1 \le n \le 25)n (1≤ n≤ 25) – сдвиг, во второй строке даётся закодированное сообщение в виде строки со строчными латинскими буквами.

#Формат выходных данных
#Программа должна вывести одну строку – декодированное сообщение. Обратите внимание, что нужно декодировать сообщение, а не закодировать.

shift = int(input())
s = input()
for i in range(len(s)):
    num = ord(s[i])
    print(chr(num - shift), end='')