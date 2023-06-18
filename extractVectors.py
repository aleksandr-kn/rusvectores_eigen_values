import csv

def readFileIntoList(filepath):
    list = []
    with open(filepath, mode="r", encoding="utf-8") as file:
        for item in file:
            list.append(item.rstrip().lower())
    return list

if __name__ == '__main__':
    wordsToFind = readFileIntoList('./datasets/банки.txt')

    vectors = []

    with open('ruscorpora_upos_skipgram_300_5_2018.vec', mode="r", encoding="utf-8") as file:
        for index, item in enumerate(file):
            #Выводим текущий прогресс
            print(index / 237255)

            # Достаем слово из строки и убираем часть речи из нее
            word = item.split(' ')[0].split('_')[0].lower()
            
            if word in wordsToFind:
                item[0]
                vectors.append(item.rstrip())
                
    with open('./vectors/ruscorpora_upos_skipgram_300_5_2018/banks.txt', 'w', encoding="utf-8") as f:
        for line in vectors:
            f.write(f"{line}\n")