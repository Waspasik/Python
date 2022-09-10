# Файлы в файле 🌶️🌶️
# Вам доступен текстовый файл files.txt, содержащий информацию о файлах. Каждая строка
# файла содержит три значения, разделенные символом пробела — имя файла, его размер
# (целое число) и единицы измерения:

# cant-help-myself.mp3 7 MB
# keep-yourself-alive.mp3 6 MB
# bones.mp3 5 MB
# ...

# Напишите программу, которая группирует данные файлы по расширению, определяя общий
# объем файлов каждой группы, и выводит полученные группы файлов, указывая для каждой
# ее общий объем. Группы должны быть расположены в лексикографическом порядке названий
# расширений, файлы в группах — в лексикографическом порядке их имен.

# Примечание 1. Например, если бы файл files.txt имел вид:

# input.txt 3000 B
# scratch.zip 300 MB
# output.txt 1 KB
# temp.txt 4 KB
# boy.bmp 2000 KB
# mario.bmp 1 MB
# data.zip 900 MB

# то программа должна была бы вывести:

# boy.bmp
# mario.bmp
# ----------
# Summary: 3 MB

# input.txt
# output.txt
# temp.txt
# ----------
# Summary: 8 KB

# ata.zip
# scratch.zip
# ----------
# Summary: 1 GB

# где Summary — общий объем файлов группы.

# Примечание 2. Гарантируется, что все имена файлов содержат расширение.

# Примечание 3. Общий объем файлов группы записывается в самых крупных (максимально
# возможных) единицах измерения с округлением до целых. Другими словами, сначала следует
# определить суммарный объем всех файлов группы, скажем, в байтах, а затем перевести
# полученное значение в самые крупные (максимально возможные) единицы измерения. Примеры
# перевода:

# 1023 B -> 1023 B
# 1300 B -> 1 KB
# 1900 B -> 2 KB

# Примечание 4. Значения единиц измерения такие же, какие приняты в информатике:

# 1 KB = 1024 B
# 1 MB = 1024 KB
# 1 GB = 1024 MB

# Примечание 5. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.

# Примечание 6. При открытии файла используйте явное указание кодировки UTF-8.

with open('D:/Python/Stepik/files.txt', 'r', encoding='utf-8') as file:
    
    def output_sum(res, sum):
        extention = {0: 'B', 1: 'KB', 2: 'MB', 3: 'GB'}
        counter = 0
        
        while True:
            if sum > 1023:
                sum = sum / 1024
                counter += 1
            else:
                sum = round(sum)
                break
        
        res.append('----------')
        sum = f'Summary: {sum} {extention[counter]}'
        res.append(sum)
        return print(*res, sep='\n')
    

    file_list = list(map(lambda line: line.split(), file.readlines()))

    for line in file_list:
        if line[-1] == 'KB':
            line[1] = int(line[1]) * 1024
        elif line[-1] == 'MB':
            line[1] = int(line[1]) * 1024**2
        elif line[-1] == 'GB':
            line[1] = int(line[1]) * 1024**3
    
    file_list = sorted(file_list)
    file_list.sort(key=lambda line: line[0].split('.')[-1])
    result = [file_list[0][0]]
    total_sum = int(file_list[0][1])

    for i in range(1, len(file_list)):
        if file_list[i][0].split('.')[-1] == result[0].split('.')[-1]:
            total_sum += int(file_list[i][1])
            result.append(file_list[i][0])
            if file_list[i] == file_list[-1]:
                output_sum(result, total_sum)
        else:
            output_sum(result, total_sum)
            print()
            result = [file_list[i][0]]
            total_sum = int(file_list[0][1])