import csv

# Возвращет список, где каждый элемент это 1 строка из читаемого файла
def readFileIntoList(filepath):
    list = []
    with open(filepath, mode="r", encoding="utf-8") as file:
        for item in file:
            list.append(item.rstrip().lower())
    return list

if __name__ == '__main__':
    wordsToFind = readFileIntoList('./datasets/авиация.txt')

    vectors = []

    # Ищем слова из нашего словаря в модели
    with open('./models/ruscorpora_upos_cbow_300_20_2019.txt', mode="r", encoding="utf-8") as file:
        for index, item in enumerate(file):
            #Выводим текущий прогресс
            print(index / 237255)

            # Достаем слово из строки и убираем часть речи из нее
            word = item.split(' ')[0].split('_')[0].lower()
            
            if word in wordsToFind:
                item[0]
                vectors.append(item.rstrip())
    # Записываем полученные вектора в файл                
    with open('./vectors/ruscorpora_upos_cbow_300_20_2019/aviation.txt', 'w', encoding="utf-8") as f:
        for line in vectors:
            f.write(f"{line}\n")