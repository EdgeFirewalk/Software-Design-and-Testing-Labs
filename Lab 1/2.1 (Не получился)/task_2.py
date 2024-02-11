# Программу написал:
# Лубенский Игорь Викторович
# Студент группы ПИН-222
# Задание 2.1 (НЕ ПОЛУЧИЛОСЬ)

def validate_score(score):
    # Преобразуем значения с кубиков из входного файла в числа и проверяем, находятся ли они в диапазоне от 1 до 6
    try:
        score = int(score)
        if score <  1 or score >  6:
            raise ValueError()
        return score
    except ValueError:
        print('Не удалось преобразовать входные данные в числа или они находятся вне диапазона от 1 до 6.')
        exit(-1)
        
def count_ones(_round):
    return sum(die for die in _round if die == 1)
    
def count_twos(_round):
    return sum(die for die in _round if die == 2)
    
def count_threes(_round):
    return sum(die for die in _round if die == 3)
    
def count_fours(_round):
    return sum(die for die in _round if die == 4)
    
def count_fives(_round):
    return sum(die for die in _round if die == 5)
    
def count_sixes(_round):
    return sum(die for die in _round if die == 6)
    
def count_chance(_round):
    return sum(_round)
    
def count_three_of_a_kind(_round):
    counts = [_round.count(die) for die in _round]
    return sum(_round) if max(counts) >= 3 else 0
    
def count_four_of_a_kind(_round):
    counts = [_round.count(die) for die in _round]
    return sum(_round) if max(counts) >= 4 else 0
    
def count_short_straight(_round):
    # TODO: ПОПРАВИТЬ, ПОТОМУ ЧТО ЧТО-ТО НЕ РОБИТ
    return 25 if sorted(set(_round)) in [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]] else 0
    
def count_long_straight(_round):
    return 35 if sorted(set(_round)) in [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]] else 0
    
def count_full_house(_round):
    counts = [_round.count(die) for die in _round]
    return 40 if len(set(counts)) == 2 and max(counts) == 3 else 0 

# Константы для категорий игр
ONES = 0
TWOS = 1
THREES = 2
FOURS = 3
FIVES = 4
SIXES = 5
CHANCE = 6
THREE_OF_A_KIND = 7
FOUR_OF_A_KIND = 8
SHORT_STRAIGHT = 9
LONG_STRAIGHT = 10
FULL_HOUSE = 11
BONUS = 12

try:
    input_file = open('input_2.txt', 'r')
except:
    print('Файл входных данных "input_2.txt" не был найден...')
file_lines = input_file.readlines()

rounds = []
# Построчно читаем файл и добавляем значения с кубиков
for line in file_lines:
    rounds.append(line.strip().split(' '))

try:
    for i in range(0, len(rounds)):
        for j in range(0, 5):
            rounds[i][j] = validate_score(rounds[i][j])
except IndexError:
    print('Входные данные неполные (недостаточно данных о бросках каком-либо раунде).')
    exit(-1)

# Если было сыграно не целое количество игр или о какой-то игре недостаточно (или наоборот много) информации
if (len(rounds) % 13 != 0) or (sum(len(scores) for scores in rounds) % 5 != 0):
    print('Ошибка входных данных: было сыграно не целое количество игр или данные о каком-либо раунде избыточны.')
    exit(-1)

games_count = int(len(rounds) / 13)

#for i in range(0, len(rounds)):
    #print(rounds[i])

for i in range(0, games_count):
    scores = [0] * 13 # Здесь будут храниться данные обо всех счетах во всех категориях игр
    
    game = rounds[i*13:(i+1)*13]
    
    for _round in game:
        scores[ONES] = count_ones(_round)
        scores[TWOS] = count_twos(_round)
        scores[THREES] = count_threes(_round)
        scores[FOURS] = count_fours(_round)
        scores[FIVES] = count_fives(_round)
        scores[SIXES] = count_sixes(_round)
        scores[CHANCE] = count_chance(_round)
        scores[THREE_OF_A_KIND] = count_three_of_a_kind(_round)
        scores[FOUR_OF_A_KIND] = count_four_of_a_kind(_round)
        scores[SHORT_STRAIGHT] = count_short_straight(_round)
        scores[LONG_STRAIGHT] = count_long_straight(_round)
        scores[FULL_HOUSE] = count_full_house(_round)
        
    if scores[ONES] + scores[TWOS] + scores[THREES] + scores[FOURS] + scores[FIVES] + scores[SIXES] >= 63:
        scores[BONUS] = 35
    
    output = ''
    for i in range(0, len(scores)):
        output += str(scores[i]) + ' '
    output += str(sum(scores))
    
    print(output)