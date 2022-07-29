# Используя генератор множеств, дополните приведенный код, так чтобы получить множество,
# содержащее уникальные значения списка items. Результат вывести на одной строке, в
# упорядоченном виде, разделяя элементы одним символом пробела.

# Примечание 1. Обратите внимание, некоторые элементы списка – числа, а некоторые – строки,
# при этом строки необходимо трактовать как числа.

items = [10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45, '67', 12, 10, 90, 23, '45', 56,
        '56', 1, 5, '6', 5]

print(*sorted(set(int(i) for i in items)))



# Используя генератор множеств, дополните приведенный код, так чтобы получить множество,
# содержащее первую букву каждого слова (в нижнем регистре) списка words. Результат вывести
# на одной строке в алфавитном порядке, разделяя элементы одним символом пробела.

words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime', 'Lemon',
        'grapes', 'persimmon', 'tangerine', 'Watermelon', 'currant', 'Almond']

print(*sorted(set(i[0].lower() for i in words)))



# Используя генератор множеств, дополните приведенный код, так чтобы получить множество,
# содержащее уникальные слова (в нижнем регистре) строки sentence. Результат вывести на
# одной строке в алфавитном порядке, разделяя элементы одним символом пробела.

# Примечание. Учтите, что знаки пунктуации не относятся к словам.

sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was
           three, and, save for a pocket of warmth in the darkest past, nothing of her subsists
           within the hollows and dells of memory, over which, if you can still stand my style
           (I am writing under observation), the sun of my infancy had set: surely, you all know
           those redolent remnants of day suspended, with the midges, about some hedge in bloom
           or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer
           dusk; a furry warmth, golden midges.'''

print(*sorted(set(i.lower().strip('.,;:-?-!()') for i in sentence.split())))



# Используя генератор множеств, дополните приведенный код, так чтобы получить множество,
# содержащее уникальные слова  строки sentence длиною меньше 44 символов. Результат вывести
# на одной строке (в нижнем регистре) в алфавитном порядке, разделяя элементы одним символом
# пробела.

# Примечание. Учтите, что знаки пунктуации не относятся к словам.

sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was
           three, and, save for a pocket of warmth in the darkest past, nothing of her subsists
           within the hollows and dells of memory, over which, if you can still stand my style
           (I am writing under observation), the sun of my infancy had set: surely, you all know
           those redolent remnants of day suspended, with the midges, about some hedge in bloom
           or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer
           dusk; a furry warmth, golden midges.'''

print(*sorted(set(i.lower().strip('.,;:-?-!()') for i in sentence.split() if len(i.lower().strip('.,;:-?-!()')) < 4)))



# Используя генератор множеств, дополните приведенный код так, чтобы он выбрал из списка files
# уникальные имена файлов c расширением .png, независимо от регистра имен и расширений. Имена
# файлов вывести вместе с расширением, все на одной строке, в нижнем регистре, в алфавитном
# порядке через пробел.

files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py',
        'book.txT', 'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt',
        'split.pop', 'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git']

print(*sorted(set(i.lower() for i in files if i[-4::].lower() == '.png')))