# Аве, Цезарь 🌶️
# 
# На вход программе подается строка текста на английском языке, в которой нужно зашифровать все слова.
# Каждое слово строки следует зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова).
# Строчные буквы при этом остаются строчными, а прописные – прописными.

# Формат входных данных 
# На вход программе подается строка текста на английском языке.

# Формат выходных данных
# Программа должна вывести зашифрованный текст в соответствии с условием задачи.

# Примечание. Символы, не являющиеся английскими буквами, не изменяются.


from string import*

upper_eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'

text = input().split()
text_list = []

for i in text:
    count_symbol = 0
    encipher_text = ''
    for l in range(len(i)):
        if i[l] in punctuation:
            count_symbol += 1
    for j in range(len(i)):
        if i[j].isalpha():
            if i[j] == i[j].upper():
                index = (upper_eng_alphabet.index(i[j]) + (len(i) - count_symbol)) % 26
                encipher_text += upper_eng_alphabet[index]
            elif i[j] == i[j].lower():
                index = (lower_eng_alphabet.index(i[j]) + (len(i) - count_symbol)) % 26
                encipher_text += lower_eng_alphabet[index]
        elif i[j] in punctuation:
            encipher_text += i[j]
    text_list.append(encipher_text)
        
print(' '.join(text_list))