def task6_1(input_file, output_file):
    try:
        # Считываем содержимое файла с клавиатуры
        user_input = input('Введите целые числа через пробел: ')

        # Записываем введенные данные в файл
        with open(input_file, 'w') as f:
            f.write(user_input)

        # Открываем файл для чтения
        with open(input_file, 'r') as f:
            numbers = list(map(int, f.read().split())) # разбиваем на отдельные строки по пробелам,
                                                       # преобразуем каждую строку в целое число с помощью функции int


        if not numbers:
            raise ValueError(
                "Файл пуст или не содержит целых чисел.")  # Если список пуст

        # Открываем файл на запись
        with open(output_file, 'w') as g:
            for i in range(0, len(numbers), 5):  # Проходим по списку numbers с шагом 5
                group = numbers[i:i + 5]         # группа из 5 элементов
                max_value = max(group)           # Находим максимальное значение
                g.write(f"{max_value}\n")        # Записываем максимальное значение в выходной файл

            # Если в последней группе меньше 5 элементов
            if len(group) < 5:
                g.write(f"{max_value}\n")  # Записываем максмальное значение последней группы еще раз в выходной файл

    except FileNotFoundError:  # Если входной файл не найден
        print(f"Ошибка: Файл {input_file} не найден.")

    except ValueError as ve:  # Если пустой файл
        print(f"Ошибка: {ve}")

    except Exception as e:  # Любые другие исключения
        print(f"Произошла ошибка: {e}")



def task6_2(input_text, output_file):
    words = input_text.split()  # Разбиваем текст на слова
    filtered_words = []  # Список для хранения отфильтрованных слов

    for word in words:
        if len(word) > 1:  # Проверяем длину слова
            filtered_words.append(word)  # Добавляем слово в список, если оно больше одной буквы

    filtered_content = ' '.join(filtered_words)  # Соединяем отфильтрованные слова в строку

    # Записываем результат в новый файл
    with open(output_file, 'w', encoding='utf-8') as g:
        g.write(filtered_content)







