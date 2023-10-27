with open('text_2_var_8.txt', 'r') as file:
    lines = file.readlines()  # читаем все строки из файла

results = []

for line in lines:
    numbers = line.strip().split(',')  # разделяем строку на числа по запятой
    numbers = [int(num) for num in numbers]  # преобразуем числа из строкового формата в целочисленный
    sum_numbers = sum(numbers)  # считаем сумму чисел
    results.append(sum_numbers)  # добавляем результат в список

with open('output_2_var_8.txt', 'w') as file:
    for result in results:
        file.write(str(result) + '\n')