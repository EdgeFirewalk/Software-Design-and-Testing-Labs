# Программу написал:
# Лубенский Игорь Викторович
# Студент группы ПИН-222
# Задание 3.1

from collections import deque  # Для работы с очередью

def is_dublet(word1, word2):
    diff_count =  0  # Счетчик различий между словами
    for c1, c2 in zip(word1, word2): # Проходим по символам пары слов одновременно
        if c1 != c2:  # Если символы различаются
            diff_count +=  1  # Увеличиваем количество разниц в словах
    return diff_count ==  1  # Если разница была только одна, то слова - дублеты

def find_dublet_sequence(word1, word2, dictionary):  # Функция ищет последовательность дублетов от word1 к word2
    queue = deque([(word1, [word1])])  # Инициализируем очередь с начальным словом и путем, содержащим только это слово (т. к. началом пути должно быть само слово)
    visited = set([word1])  # Слова из словаря, по которым уже проходились
    while queue:  # Пока очередь не пуста
        current_word, path = queue.popleft()  # Берем первое слово и путь из очереди
        if current_word == word2:  # Если текущее слово совпадает с конечным словом
            return path  # Возвращаем путь
        for next_word in dictionary:  # Проходим по всем словам в словаре
            if next_word not in visited and is_dublet(current_word, next_word):  # Если слово еще не посещено и является дублетом
                visited.add(next_word)  # Добавляем слово в те, по которым уже прошлись
                queue.append((next_word, path + [next_word]))  # Добавляем слово в очередь с обновленным путем
    return None  # Путь не найден

def main():
    dictionary = set()  # Создаем множество для хранения словаря
    with open("input.txt", "r") as file:
        for line in file:
            if line.strip() == "":  # Если строка пустая
                break  # Прерываем цикл чтения (словарь закончился)
            dictionary.add(line.strip())  # Добавляем слово в словарь
        pairs = []  # Создаем список для хранения пар слов
        for line in file:
            if line.strip() == "":  # Если строка пустая
                break  # Прерываем цикл чтения
            word1, word2 = line.strip().split() # Разделяем строку на два слова
            pairs.append((word1, word2)) # Добавляем пару слов в список

    for word1, word2 in pairs:  # Проходим по всем парам слов
        sequence = find_dublet_sequence(word1, word2, dictionary)  # Ищем последовательность дублетов
        if sequence:  # Если последовательность найдена
            print("\n".join(sequence) + "\n")  # Выводим последовательность
        else:
            print("No solution.\n")

main()
