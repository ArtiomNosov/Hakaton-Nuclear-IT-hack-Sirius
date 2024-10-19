''' Version 0
import pandas as pd

# Пример: чтение данных о статистике отзывов и пояснений
reviews_df = pd.read_excel("C:\\Users\\arkha\\OneDrive\\Desktop\\tyoi\\example_report.xlsx", sheet_name="Статистика")

# Генерация текста для отчета
positive_reviews = reviews_df[reviews_df['Тональность'] == 'Положительная']
negative_reviews = reviews_df[reviews_df['Тональность'] == 'Отрицательная']
neutral_reviews = reviews_df[reviews_df['Тональность'] == 'Нейтральная']

report_text = f"""
### Отчет по отзывам сотрудников
Всего отзывов: {len(reviews_df)}
Положительные отзывы: {len(positive_reviews)}
Отрицательные отзывы: {len(negative_reviews)}
Нейтральные отзывы: {len(neutral_reviews)}

Основные причины положительных отзывов:
- {positive_reviews['Причина'].value_counts().index[0]}

Основные причины отрицательных отзывов:
- {negative_reviews['Причина'].value_counts().index[0]}
"""
C:\\Users\\arkha\\OneDrive\\Desktop\\tyoi\\test_questions.xlsx
# Вывод текста отчета
print(report_text)'''


''' Version 1
import pandas as pd

# Загрузка данных из Excel
df = pd.read_excel("C:\\Users\\arkha\\OneDrive\\Desktop\\tyoi\\test_questions.xlsx")


# Функция для генерации рекомендаций HR
def generate_hr_message(question, top_answer):
    # Пример базового текста
    message = f"Больше всего покинуло компанию из-за '{top_answer}'. "

    # Пример ПРОМТа для генерации рекомендаций
    recommendations = {
        "Не хотели повышать зарплату": "Необходимо пересмотреть политику повышения зарплат, провести оценку рынка и предложить конкурентные условия для сотрудников.",
        "Скучные задачи, неинтересная работа": "Следует предоставить больше возможностей для карьерного роста, повышения квалификации, а также разнообразить рабочие задачи.",
        "Усталость и жажда перемен": "Рекомендуется рассмотреть программы по улучшению баланса работы и личной жизни, а также создание возможностей для внутренней ротации сотрудников."
    }

    # Получаем рекомендацию на основе самого популярного ответа
    action = recommendations.get(top_answer,
                                 "Рекомендуется провести дополнительный анализ, чтобы предложить шаги по улучшению.")

    # Возвращаем сообщение для HR
    return message + action


# Процесс анализа каждого вопроса
for index, row in df.iterrows():
    question = row['Вопрос']
    answers = row['Ответы']

    # Разделяем ответы по разделителю ";"
    answers_list = answers.split(";")

    # Убираем лишние пробелы в ответах
    answers_list = [answer.strip() for answer in answers_list if answer.strip()]

    # Подсчитываем количество каждого ответа и процентное распределение
    answer_counts = pd.Series(answers_list).value_counts(normalize=True) * 100

    # Выводим процентное распределение по каждому ответу
    print(f"### {question}")
    print("Процентное распределение ответов:")
    for answer, percent in answer_counts.items():
        print(f"- {answer}: {percent:.2f}%")

    # Определяем самый частый ответ
    top_answer = answer_counts.idxmax()

    # Генерация сообщения для HR
    hr_message = generate_hr_message(question, top_answer)

    # Вывод сообщения для HR
    print(hr_message)
    print("\n")
'''
import pandas as pd
import requests


# Функция для отправки запроса к Сбер API
def get_hr_recommendation(question, top_answer):
    api_url = "https://api.sberbank.ru/v1/recommendations"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer YOUR_API_KEY"
    }
    data = {
        "prompt": f"Сформируйте рекомендации для HR, учитывая, что больше всего сотрудников покинуло компанию по причине: {top_answer}.",
        "max_tokens": 100
    }
    response = requests.post(api_url, headers=headers, json=data)
    if response.status_code == 200:
        recommendation = response.json().get("recommendation", "Рекомендации не найдены")
        return recommendation
    else:
        return "Не удалось получить рекомендации от API"


# Загрузка данных из Excel
df = pd.read_excel("path_to_your_file.xlsx")

# Процесс анализа каждого вопроса
for index, row in df.iterrows():
    question = row['Вопрос']
    answers = row['Ответы']

    # Разделяем ответы по разделителю ";"
    answers_list = answers.split(";")

    # Убираем лишние пробелы в ответах
    answers_list = [answer.strip() for answer in answers_list if answer.strip()]

    # Подсчитываем количество каждого ответа и процентное распределение
    answer_counts = pd.Series(answers_list).value_counts(normalize=True) * 100

    # Выводим процентное распределение по каждому ответу
    print(f"### {question}")
    print("Процентное распределение ответов:")
    for answer, percent in answer_counts.items():
        print(f"- {answer}: {percent:.2f}%")

    # Определяем самый частый ответ
    top_answer = answer_counts.idxmax()

    # Получение рекомендаций от Сбер API
    hr_message = get_hr_recommendation(question, top_answer)

    # Вывод сообщения для HR
    print(hr_message)
    print("\n")

    import requests
    import uuid


    def get_token(auth_token, scope='GIGACHAT_API_PERS'):
        """
          Выполняет POST-запрос к эндпоинту, который выдает токен.

          Параметры:
          - auth_token (str): токен авторизации, необходимый для запроса.
          - область (str): область действия запроса API. По умолчанию — «GIGACHAT_API_PERS».

          Возвращает:
          - ответ API, где токен и срок его "годности".
          """
        # Создадим идентификатор UUID (36 знаков)
        rq_uid = str(uuid.uuid4())

        # API URL
        url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

        # Заголовки
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',
            'RqUID': rq_uid,
            'Authorization': f'Basic {auth_token}'
        }

        # Тело запроса
        payload = {
            'scope': scope
        }

        try:
            # Делаем POST запрос с отключенной SSL верификацией
            # (можно скачать сертификаты Минцифры, тогда отключать проверку не надо)
            response = requests.post(url, headers=headers, data=payload, verify=False)
            return response
        except requests.RequestException as e:
            print(f"Ошибка: {str(e)}")
            return -1

    response = get_token(auth)
    if response != 1:
        print(response.text)
        giga_token = response.json()['access_token']

    import requests

    url = "https://gigachat.devices.sberbank.ru/api/v1/models"

    payload = {}
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {giga_token}'
    }

    response = requests.request("GET", url, headers=headers, data=payload, verify=False)

    print(response.text)

    import requests
    import json


    def get_chat_completion(auth_token, user_message):
        """
        Отправляет POST-запрос к API чата для получения ответа от модели GigaChat.

        Параметры:
        - auth_token (str): Токен для авторизации в API.
        - user_message (str): Сообщение от пользователя, для которого нужно получить ответ.

        Возвращает:
        - str: Ответ от API в виде текстовой строки.
        """
        # URL API, к которому мы обращаемся
        url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"

        # Подготовка данных запроса в формате JSON
        payload = json.dumps({
            "model": "GigaChat",  # Используемая модель
            "messages": [
                {
                    "role": "user",  # Роль отправителя (пользователь)
                    "content": user_message  # Содержание сообщения
                }
            ],
            "temperature": 1,  # Температура генерации
            "top_p": 0.1,  # Параметр top_p для контроля разнообразия ответов
            "n": 1,  # Количество возвращаемых ответов
            "stream": False,  # Потоковая ли передача ответов
            "max_tokens": 512,  # Максимальное количество токенов в ответе
            "repetition_penalty": 1,  # Штраф за повторения
            "update_interval": 0  # Интервал обновления (для потоковой передачи)
        })

        # Заголовки запроса
        headers = {
            'Content-Type': 'application/json',  # Тип содержимого - JSON
            'Accept': 'application/json',  # Принимаем ответ в формате JSON
            'Authorization': f'Bearer {auth_token}'  # Токен авторизации
        }

        # Выполнение POST-запроса и возвращение ответа
        try:
            response = requests.request("POST", url, headers=headers, data=payload, verify=False)
            return response
        except requests.RequestException as e:
            # Обработка исключения в случае ошибки запроса
            print(f"Произошла ошибка: {str(e)}")
            return -1


    import time


    def gpt(answer):
        time.sleep(0.1)
        return get_chat_completion(giga_token, answer).json()['choices'][0]['message']['content']

    gpt('Что такое нейронка')
