from collections import Counter
import re

# Чтение текста из файла
with open('text_1_var_8.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Разделение текста на слова и подсчет частоты каждого слова
words = re.findall(r'\b\w+\b', text.lower())
word_counts = Counter(words)

# Сортировка результатов по убыванию частоты
sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

# Запись результатов в файл
with open('output_1_var_8.txt', 'w', encoding='utf-8') as file:
    for word, count in sorted_words:
        file.write(f'{word}: {count}\n')