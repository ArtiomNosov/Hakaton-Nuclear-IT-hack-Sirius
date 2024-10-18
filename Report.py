import pandas as pd

# Пример: чтение данных о статистике отзывов и пояснений
reviews_df = pd.read_excel("example_report.xlsx", sheet_name="Статистика")

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

# Вывод текста отчета
print(report_text)