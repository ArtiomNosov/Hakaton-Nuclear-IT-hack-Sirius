# считать файл
import pandas as pd

def read_excel_to_df(file_path, sheet_name=None):
    """
    Читает Excel файл и возвращает DataFrame.
    
    Параметры:
    - file_path (str): Путь к файлу Excel.
    - sheet_name (str или None): Название листа, который нужно считать. Если None, читается первый лист.
    
    Возвращает:
    - pd.DataFrame: Данные из Excel в виде DataFrame.
    """
    try:
        if sheet_name:
            df = pd.read_excel(file_path, sheet_name=sheet_name)
        else:
            df = pd.read_excel(file_path)  # По умолчанию, считываем первый лист
        print(f"Файл успешно загружен. Размер данных: {df.shape}")
        return df
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return None

# Пример использования
file_path = 'Исходный_датасет_ответы_сотрудников_и_HR.xlsx'  # Замените на свой путь к файлу
df = read_excel_to_df(file_path, sheet_name='ответы сотрудников')  # Или используйте sheet_name=None, чтобы считать первый лист
df

client_id = "3567880b-5163-43df-b3f9-6dd33cd45a64"
secret = "e66862d6-97e4-4a4c-b158-9626e5e9fa2d"
auth = "MzU2Nzg4MGItNTE2My00M2RmLWIzZjktNmRkMzNjZDQ1YTY0OmU2Njg2MmQ2LTk3ZTQtNGE0Yy1iMTU4LTk2MjZlNWU5ZmEyZA=="

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

payload={}
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
    while True:
        try:
            time.sleep(0.1)  # Имитация задержки
            # Основная часть, где вызывается GPT API
            return get_chat_completion(giga_token, answer).json()['choices'][0]['message']['content']
        except Exception as e:
            response = get_token(auth)
            if response != 1:
                print(response.text)
                giga_token = response.json()['access_token']  # Вызов функции foo() при возникновении ошибки
            # Можно также вывести сообщение об ошибке для отладки
            print(f"Ошибка: {e}")
            # После вызова foo выполнение повторяется (while True)
gpt('Что такое нейронка')

prompt = '''
Привет! Мы провели опрос сотрудников о причинах ухода из компании. На каждый вопрос сотрудник дал развёрнутый ответ.

Вопрос: "{}"
Ответ: "{}"

Проанализируй ответ и отнеси его к одному или нескольким из следующих классов причин:
"Зарплата"
"Карьерные перспективы"
"Взаимоотношения в коллективе"
"Условия труда"
"График работы"
"Управление и руководство"
"Личностные причины"
"Другие причины"

Верни названия классов причин, к которым относится этот ответ. Если причин несколько, укажи каждую отдельно в кавычках. Пример ответа: "Карьерные перспективы", "Условия труда".
'''

import time
import pandas as pd

# Функция для сохранения промежуточных результатов
def save_intermediate_result(df, filename='intermediate_result.csv'):
    df.to_csv(filename, index=False)
    print(f"Промежуточные результаты сохранены в {filename}")

# Функция gpt с обработкой ошибок и возможностью повторного вызова
def gpt(answer):
    while True:
        try:
            time.sleep(0.1)  # Имитация задержки
            # Основная часть, где вызывается GPT API
            return get_chat_completion(giga_token, answer).json()['choices'][0]['message']['content']
        except Exception as e:
            response = get_token(auth)
            if response != 1:
                print(response.text)
                giga_token = response.json()['access_token']  # Вызов функции foo() при возникновении ошибки
            print(f"Ошибка: {e}")
            # Продолжаем цикл до успешного выполнения

# Пробуем восстановить с промежуточного результата, если файл существует
try:
    df_result = pd.read_csv('intermediate_result.csv')
    print("Успешно загружены промежуточные результаты.")
except FileNotFoundError:
    print("Нет промежуточных результатов, начинаем заново.")
    df_result = pd.DataFrame(columns=df.columns)  # Создаём пустой DataFrame с колонками из df_10

# Основной процесс обработки с сохранением результатов
def process_df(df_10, prompt):
    global df_result  # Для сохранения промежуточных данных
    for col in df_10.columns:
        if col not in df_result.columns:
            df_result[col] = None  # Добавляем колонку, если её нет

        for idx, x in df_10[col].items():
            # Пропускаем уже обработанные строки
            if not pd.isna(df_result.get(col, pd.Series()).get(idx)):
                continue
            
            # Обрабатываем данные и добавляем в DataFrame
            result = gpt(prompt.format(col, x))
            print(f'result: {result}')
            df_result.at[idx, col] = result
            
            # Сохраняем промежуточные результаты каждые 10 шагов
            if idx % 10 == 0:
                save_intermediate_result(df_result)

    # Сохранение окончательного результата
    save_intermediate_result(df_result, 'final_result.csv')

# Применяем функцию к DataFrame df_10
process_df(df, prompt)

import pandas as pd
import re
from collections import Counter

def extract_and_count(df):
    result_dict = {}
    
    for col in df.columns:
        # Извлекаем строки между кавычками в каждом столбце
        values_in_quotes = df[col].apply(lambda x: re.search(r'"(.*?)"', x).group(1) if isinstance(x, str) and '"' in x else None)
        
        # Считаем частоты строк и сохраняем в словарь
        frequencies = Counter(values_in_quotes.dropna())
        result_dict[col] = dict(frequencies)
    
    return result_dict

# Применяем функцию к DataFrame
result_dict = extract_and_count(df_result)

# Выводим результат
print(result_dict)

# Преобразование словаря в DataFrame
data = {'Вопрос': [], 'Ответ': [], 'Количество': []}

# Проход по словарю
for question, reasons in result_dict.items():
    for reason, count in reasons.items():
        data['Вопрос'].append(question)
        data['Ответ'].append(reason)
        data['Количество'].append(count)

# Создание DataFrame
df_proc = pd.DataFrame(data)

# Вывод результата
print(df_proc)

df_proc.to_csv('df_proc.csv')
# получаем уже обработанные файлы

import pandas as pd
df = pd.read_csv('df_proc.csv')
df

# диаграмма

# текст
# Для тональности чуть позже
'''
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

from secret import *


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

payload={}
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

print('aaaaaaaaaaaa', gpt('Что такое нейронка'))

# Простой комментарий без gpt

# Функция для генерации рекомендаций HR
def generate_hr_message(question, top_answer, answer_assign):
    # Пример базового текста
    message = f"Больше всего покинуло компанию из-за '{top_answer}'. "

    prompt = '''
        Привет! Мы провели опрос сотрудников по различным вопросам, касающимся их опыта работы и причин увольнения. Я приведу тебе один из вопросов и распределение ответов по частоте. На основании этих данных составь аналитику, выдели ключевые тенденции и причины, и сделай выводы о наиболее частых мотивах для сотрудников. Проанализируй данные и выведи основные инсайты.

        Вопрос: "{}"
        Распределение ответов:
        {}

        Пожалуйста, предоставь развернутую аналитику на основании этих данных, выделив наиболее важные моменты. Структура ответа:
        категория, процент, рекомендации по улучшению для hr
    '''

    # Получаем рекомендацию на основе самого популярного ответа
    action = gpt(prompt.format(question, answer_assign))

    # Возвращаем сообщение для HR
    return message + action


# Процесс анализа каждого вопроса
for question in df['Вопрос'].unique():
    # print(df.columns)
    # print(df['Unnamed: 0'].unique())
    df_curr = df[df['Вопрос'] == question].reset_index()
    # print(df_curr)
    # Выводим процентное распределение по каждому ответу
    print(f"### {question}")
    print("Процентное распределение ответов:")
    answer_assign = ''
    for row in df_curr.iterrows():
        # print(row)
        answer_assign += f"- {row[1]['Ответ']}: {round(row[1]['Количество']*100/df_curr['Количество'].sum()):.0f}%"
        print(f"- {row[1]['Ответ']}: {round(row[1]['Количество']*100/df_curr['Количество'].sum()):.0f}%")
    
    # Определяем самый частый ответ
    # print(df_curr['Количество'])
    print(df_curr.shape)
    print(df_curr['Количество'].idxmax())
    top_answer = df_curr.iloc[df_curr['Количество'].idxmax()]['Ответ']

    # Генерация сообщения для HR
    hr_message = generate_hr_message(question, top_answer, answer_assign)

    # Вывод сообщения для HR
    print(hr_message)
    print("\n")


# pdf

import pandas as pd
df = pd.read_csv('df_proc.csv')
df

import matplotlib.pyplot as plt
from fpdf import FPDF
import os

# Функция для создания графика
def create_plot(df, question, max_answers=7):
    # Фильтрация данных по вопросу
    question_data = df[df['Вопрос'] == question]
    
    # Сортировка по количеству ответов
    question_data = question_data.sort_values(by='Количество', ascending=False)
    
    # Если вариантов больше max_answers, агрегация оставшихся в "Другое"
    if len(question_data) > max_answers:
        top_responses = question_data.iloc[:max_answers]
        other_responses = question_data.iloc[max_answers:]
        # Добавляем суммарное количество для категории "Другое"
        other_sum = other_responses['Количество'].sum()
        other_row = pd.DataFrame({'Ответ': ['Другое'], 'Количество': [other_sum]})
        top_responses = pd.concat([top_responses, other_row], ignore_index=True)
    else:
        top_responses = question_data
    
    # Построение линейчатой диаграммы
    top_responses = top_responses.sort_values(by='Количество', ascending=True)
    plt.figure(figsize=(10, 6))
    plt.barh(top_responses['Ответ'], top_responses['Количество'], color='skyblue')
    plt.xlabel('Количество')
    plt.ylabel('Ответы')
    plt.title(f'Распределение ответов на вопрос: {question}')
    
    # Сохраняем график во временный файл
    plt.savefig(f"temp.png", bbox_inches='tight')
    plt.close()

# Функция для добавления графика и текста в PDF
def add_plot_to_pdf(pdf, question, df, text, title):
    # Создаем график
    create_plot(df, question)
    
    # Добавляем новый лист в PDF
    pdf.add_page()

    # Заголовок
    # pdf.set_xy(10, 120)
    # pdf.set_font('Arial', '', 20)
    # pdf.multi_cell(0, 10, title)
    
    # Добавляем график
    pdf.image(f"temp.png", x=20, y=20, w=180)
    
    # Добавляем текст ниже графика
    pdf.set_xy(10, 120)
    pdf.set_font('Arial', '', 12)
    # text_after = '\n\n\n\n' + text
    print(text)
    pdf.multi_cell(0, 10, text)

# Основной процесс для генерации PDF отчета
def generate_pdf_report(filename, df):
    pdf = FPDF()

    # Указываем путь к шрифту arial.ttf (замени путь на актуальный для твоей системы)
    font_path = 'C:/Windows/Fonts/arial.ttf'  # Путь к файлу шрифта на Windows
    pdf.add_font('Arial', '', font_path, uni=True)
    
    for question in df['Вопрос'].unique():
        # Данные для примера
        title = f"График для вопроса '{question}'"

        # print(df.columns)
        # print(df['Unnamed: 0'].unique())
        df_curr = df[df['Вопрос'] == question].reset_index()
        # print(df_curr)
        # Выводим процентное распределение по каждому ответу
        print(f"### {question}")
        print("Процентное распределение ответов:")
        answer_assign = ''
        df_curr = df_curr.sort_values(by='Количество', ascending=False)
        counter = 0
        for row in df_curr.iterrows():
            # print(row)
            if counter < 5:
                answer_assign += f"{row[1]['Ответ']}: {round(row[1]['Количество']*100/df_curr['Количество'].sum()):.0f}%."
            counter += 1
            print(f"- {row[1]['Ответ']}: {round(row[1]['Количество']*100/df_curr['Количество'].sum()):.0f}%")
        
        # Определяем самый частый ответ
        # print(df_curr['Количество'])
        print(df_curr.shape)
        print(df_curr['Количество'].idxmax())
        top_answer = df_curr.iloc[df_curr['Количество'].idxmax()]['Ответ']

        # Генерация сообщения для HR
        hr_message = generate_hr_message(question, top_answer, answer_assign)

        text = answer_assign + '\n' + hr_message
        text = text.replace('#', '').replace('*', '')
        # Добавляем график и текст в PDF
        add_plot_to_pdf(pdf, question, df, text, title)
        
        # Удаляем временный файл с графиком
        if os.path.exists(f"temp.png"):
            os.remove(f"temp.png")
    
    # Сохраняем итоговый PDF файл
    pdf.output(filename)
    
    

generate_pdf_report("report.pdf", df)