import random
from collections import defaultdict


def train(dataset):
    # Создаем словарь для хранения пар букв и их частотности
    bigram_counts = defaultdict(int)

    # Обходим все имена в датасете
    for name in dataset:
        # Добавляем начало и конец слова для учета биграмм на границах слов
        name = '^' + name + '$'

        # Обходим все пары букв в имени
        for i in range(len(name)-1):
            # Получаем текущую биграмму
            curr_bigram = name[i:i+2]

            # Увеличиваем счетчик для текущей биграммы
            bigram_counts[curr_bigram] += 1

    # Вычисляем общее количество биграмм
    total_bigrams = sum(bigram_counts.values())

    # Создаем словарь для хранения вероятностей биграмм
    bigram_probs = defaultdict(float)

    # Вычисляем вероятность для каждой биграммы
    for bigram, count in bigram_counts.items():
        bigram_probs[bigram] = count / total_bigrams

    # Возвращаем словарь с вероятностями биграмм
    return bigram_probs

def generate_name(bigram_probs):
    # Получаем начальную букву для имени
    current_letter = '^'
    name = ''

    # Генерируем имя, пока не достигнем конца слова
    while current_letter != '$':
        # Создаем список биграмм, которые могут следовать за текущей буквой
        possible_bigrams = [bigram for bigram in bigram_probs if bigram.startswith(current_letter)]

        # Выбираем следующую букву случайным образом на основе вероятностей биграмм
        next_bigram = random.choices(possible_bigrams, [bigram_probs[bigram] for bigram in possible_bigrams])[0]
        next_letter = next_bigram[1]

        # Добавляем выбранную букву к имени и обновляем текущую букву
        name += next_letter
        current_letter = next_letter
    
    if name.__len__() < 4:
          name = generate_name(bigram_probs)
    return name[:name.__len__()-1]

# Open the file
with open('names.txt', 'r') as file:
  # Get all lines as a list
  names_list = file.read().split('\n')
  # Remove the last element, which is empty due to the final newline character
  names_list.pop()

bigram_probs = train(names_list)
print(generate_name(bigram_probs))
print(generate_name(bigram_probs))
print(generate_name(bigram_probs))
print(generate_name(bigram_probs))
print(generate_name(bigram_probs))
print(generate_name(bigram_probs))
print(generate_name(bigram_probs))
print(generate_name(bigram_probs))
print(generate_name(bigram_probs))
print(generate_name(bigram_probs))
print(generate_name(bigram_probs))
print(generate_name(bigram_probs))






# bigram = [(names_list[i], names_list[i + 1])
#            for i in range(len(names_list) - 1)]
# print(bigram[0][1])
# print(bigram[1])
# print(bigram)
