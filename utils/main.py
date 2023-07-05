from utils.work_function import hh_function, sj_function


def main():
    """Основная функция программы"""
    print('Здравствуйте! Хотите найти подходящую для вас работу?')

    while True:  # Цикл для проверки ответа
        while True:  # Цикл для проверки ответа
            first_question = input('\nВыберите платформу для поиска вакансий:\n'
                                   '1 - Head Hunter\n'
                                   '2 - Super Job\n'
                                   'Введите цифру от 1 до 2: ')
            if first_question == '1' or first_question == '2':
                break

            else:
                print("\nТакой платформы не существует!\n")
                continue

        while True:  # Цикл для проверки ответа
            keyword = input('\nВведите название вакансии: (например: python)\n')
            if len(keyword.lower()) <= 2:
                print("\nНет вакансий, соответствующих заданным критериям!")
                continue
            else:
                break

        while True:  # Цикл для проверки ответа
            count_vacancy = input('\nСколько вакансий Вам показать? (Не более 100)\n')
            try:
                if int(count_vacancy) > 1:
                    break
                else:
                    print("\nВведите другое количество вакансий!")
                continue

            except ValueError:
                print("\nВы ничего не вводите!\n")
                continue

        while True:  # Цикл для проверки ответа
            city = input('\nВ каком городе ищем?\n')
            if len(city.lower()) <= 2:
                print("\nНазвание города слишком короткое!\n")
                continue
            else:
                break

        keyword_end = keyword + ' ' + city  # Составляем запрос для поиска вакансий

        if first_question == '1':
            hh_function(keyword_end, count_vacancy)  # вызываем функцию для поиска с параметрами пользователя

        elif first_question == '2':
            sj_function(keyword_end, count_vacancy)  # вызываем функцию для поиска с параметрами пользователя

        while True:  # Цикл для проверки ответа
            answer_end = input('\nПоказать Вам другие вакансии? Да/Нет\n')
            if answer_end.lower() == 'да' or answer_end.lower() == 'lf':
                break
            elif answer_end.lower() == 'нет' or answer_end.lower() == 'ytn':
                print('\nДо встречи!')
                exit()

            else:
                print('\nПоказать Вам другие вакансии? Да/Нет\n')
                continue


if __name__ == '__main__':
    main()
