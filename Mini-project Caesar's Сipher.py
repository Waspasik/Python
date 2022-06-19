# Описание проекта: требуется написать программу, способную шифровать и дешифровать текст в соответствии
# с алгоритмом Цезаря. Она должна запрашивать у пользователя следующие данные:

# направление: шифрование или дешифрование;
# язык алфавита: русский или английский;
# шаг сдвига (со сдвигом вправо).
# Примечание 1. Считайте, что в русском языке 32 буквы (буква ё отсутствует).

# Примечание 2. Неалфавитные символы — знаки препинания, пробелы, цифры — не меняются.

# Примечание 3. Сохраните регистр символов. Например, текст: "Умом Россию не понять" при сдвиге на одну
#  позицию вправо будет преобразован в: "Фнпн Спттйя ож рпоауэ".


from string import*

upper_rus_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
lower_rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
upper_eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'

print('Добро пожаловать в программу по шифрованию и дешифрованию текста методом Шифра Цезаря. Программа принимает текст на английском и русском языках.')
print('Введите текст, который требуется зашифровать / расшифровать')
text = input()

language = input('Какой язык используется в тексте: русский или английский? \n').lower()
while language != 'русский' and language != 'английский':
        language = input('Введи название языка правильно \n').lower()

direction = input('Что необходимо сделать с текстом? Шифрование или дешифрование? \n').lower()
while direction != 'шифрование' and direction != 'дешифрование':
        direction = input('Введи нужное действие правильно \n').lower()

def choice_key():

    key = input('Какой ключ будет в вашем шифре? \n')
    while key.isdigit() != True:
        key = input('Введи ключ шифра числом \n')
    
    if direction == 'дешифрование':
        decryption(text, language, key)
    elif direction == 'шифрование':
        encryption(text, language, key)


def decryption(text, language, key):
    if language == 'русский':
        decipher_text = ''
        for i in range(len(text)):
            if text[i].isalpha():
                if text[i] == text[i].upper():
                    index = (upper_rus_alphabet.index(text[i]) - int(key)) % 32
                    decipher_text += upper_rus_alphabet[index]
                elif text[i] == text[i].lower():
                    index = (lower_rus_alphabet.index(text[i]) - int(key)) % 32
                    decipher_text += lower_rus_alphabet[index]
            elif text[i] in punctuation or text[i] == ' ':
                decipher_text += text[i]
        return print(decipher_text)
    elif language == 'английский':
        decipher_text = ''
        for i in range(len(text)):
            if text[i].isalpha():
                if text[i] == text[i].upper():
                    index = (upper_eng_alphabet.index(text[i]) - int(key)) % 26
                    decipher_text += upper_eng_alphabet[index]
                elif text[i] == text[i].lower():
                    index = (lower_eng_alphabet.index(text[i]) - int(key)) % 26
                    decipher_text += lower_eng_alphabet[index]
            elif text[i] in punctuation or text[i] == ' ':
                decipher_text += text[i]
        return print(decipher_text)


def encryption(text, language, key):
    if language == 'русский':
        encipher_text = ''
        for i in range(len(text)):
            if text[i].isalpha():
                if text[i] == text[i].upper():
                    index = (upper_rus_alphabet.index(text[i]) + int(key)) % 32
                    encipher_text += upper_rus_alphabet[index]
                elif text[i] == text[i].lower():
                    index = (lower_rus_alphabet.index(text[i]) + int(key)) % 32
                    encipher_text += lower_rus_alphabet[index]
            elif text[i] in punctuation or text[i] == ' ':
                encipher_text += text[i]
        return print(encipher_text)
    elif language == 'английский':
        encipher_text = ''
        for i in range(len(text)):
            if text[i].isalpha():
                if text[i] == text[i].upper():
                    index = (upper_eng_alphabet.index(text[i]) + int(key)) % 26
                    encipher_text += upper_eng_alphabet[index]
                elif text[i] == text[i].lower():
                    index = (lower_eng_alphabet.index(text[i]) + int(key)) % 26
                    encipher_text += lower_eng_alphabet[index]
            elif text[i] in punctuation or text[i] == ' ':
                encipher_text += text[i]
        return print(encipher_text)


choice_key()

continue_cipher = input('Желаете продолжить? \n').lower()
while True:
    if continue_cipher == 'да':
        choice_key()
    else:
        break