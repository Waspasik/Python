from random import*

print('Всем Ку, гайз!', 'Олды на месте 😎.', 'Добро пожаловать в игру "Подвесь Папича".')
word_list = ['папич', 'микрочелик', 'величайший', 'помойка', 'работяги', 'богдан', 'вика', 'тварына', 'соляного', 'нереалистично', 'очередняра']

def get_word():
    return choice(word_list).upper()
    
def display_hangman(tries):
    stages = [  # финальное состояние Папича: голова, торс, обе руки, обе ноги 
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние Папича
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return print(stages[tries])

def wish_word_check(word):
    upper_rus_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    true_value = 0
    while True:
        for i in range(len(word)):
            if word[i].upper() in upper_rus_alphabet:
                true_value += 1
        if true_value == len(word):
            return True
        else:
            print('Введи букву или слово кириллицей')
            continue

def play(word):
    word_completion = '_' * len(word)
    guessed = True
    guessed_letters = []
    guessed_words = []
    tries = 6
    if word == word_list[0].upper():
        print('Это величайший игрок, непризнанный игрок № 1 в DOTA 2, бригадир работяг.')
    elif word == word_list[1].upper():
        print('Папич так называет все мелкое и то, что похоже на ребенка.')
    elif word == word_list[2].upper():
        print('Официальный титул Папича.')
    elif word == word_list[3].upper():
        print('Дота. Для этого слова Папич придумал отдельный смайлик, описывающий самое дно в этой игре.')
    elif word == word_list[4].upper():
        print('Название комьюнити Папича. Каждый из участников комьюнити гордо носит звание этого трудолюбивого человека.')
    elif word == word_list[5].upper():
        print('Культовый, но мифический персонаж. Появился в начале стримов, когда работяга скинул донат з рофлом про некоего "дядю". Папаня бурно отреагировал на гомофобычах.')
    elif word == word_list[6].upper():
        print('Фаворитка Папича.')
    elif word == word_list[7].upper():
        print('Это слово переводится с украинского как "животное". Плюс, оно хорошо звучит, поэтому Папич взял себе это слово.')
    elif word == word_list[8].upper():
        print('Культовый боевый крик Величайшего. Означает - в соло - в одного - в одиночку. Первая буква "в" отсутствует.')
    elif word == word_list[9].upper():
        print('Каждый раз, когда Папич проиграл только через свой "острой ум" или кривые пальцы, то он орет - ... .')
    elif word == word_list[10].upper():
        print('Так Величайший называет очередного игрока, который по воле судьбы попался Папичу под нож.')
    display_hangman(tries)
    print(word_completion)

    while tries > 0 or guessed == False:
        wish_word = input('Введи одну букву или целое слово, если ты знаешь ответ \n').upper()
        while wish_word.isalpha() == False or wish_word in guessed_letters or wish_word in guessed_words:
            wish_word = input('Ты на рофланах? Введи букву или слово правильно, дебилыч. \n').upper()
        if len(wish_word) == 1 and wish_word in word:
            for i in range(len(word)):
                if word[i] == wish_word:
                    word_completion = word_completion[:i] + wish_word + word_completion[i + 1:]
            guessed_letters.append(wish_word)
            display_hangman(tries)
            print(word_completion)
            if word_completion == word:
                guessed = True
                print('Ты никогда не будешь в безопасности, сын мой, - никто не в безопасности, пока я жив.')
                break
        elif len(wish_word) == 1 and wish_word not in word:
            guessed_letters.append(wish_word)
            tries -= 1
            print('Сын бляди, убить лучшего в мире задумал!')
            display_hangman(tries)
            print(word_completion)
        elif len(wish_word) == len(word):
            if wish_word == word:
                display_hangman(tries)
                print(wish_word)
                print('И что, Шейкер, у меня есть жизнь. Я не умру. Я буду жить вечно!')
                guessed = True
                break
            else:
                guessed_words.append(wish_word)
                tries -= 1
                print('Помогите мне! Твари! Животные! Сыновья шлюх!')
                display_hangman(tries)
                print(word_completion)
                guessed = False
        elif len(wish_word) > len(word):
            guessed_words.append(wish_word)
            tries -= 1
            print('Не надо, дядя!')
            display_hangman(tries)
            print(word_completion)
            guessed = False
    if tries == 0:
        print('Ноль помощи.')

while True:
    play(get_word())
    continue_game = input('Желаете попытать счастье и спасти Папизи от верной гибели? Введи "да" или "нет". \n').lower()
    if continue_game == 'да':
        continue
    else:
        break