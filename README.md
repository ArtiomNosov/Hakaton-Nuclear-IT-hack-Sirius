# Hakaton-Nuclear-IT-hack-Sirius
# [Аналитический дашборд на основе ответов сотрудников](https://datalens.yandex/u5r6316442j6h)
![image](https://github.com/user-attachments/assets/813efad9-d424-4915-b0a4-3e960f210947)
# [Ссылка на развёрнутый отчёт](https://disk.yandex.ru/i/3mXH5qQ0W0Agcw)
# Как пользоваться
Открывать через консоль в режиме Администратора

0. Установка Git
- Перейдите на официальный сайт Git: https://git-scm.com/download/win
- Нажмите на ссылку для загрузки установочного файла Git для Windows.
- Откройте загруженный файл и следуйте инструкциям установщика. При установке рекомендуется оставить настройки по умолчанию.

Последовательно копировать строки:

1. ```git clone https://github.com/ArtiomNosov/Hakaton-Nuclear-IT-hack-Sirius```

2. ```cd Hakaton-Nuclear-IT-hack-Sirius```

3. ```pip install virtualenv```

   ```virtualenv envname```

4. ```envname\scripts\activate```

5. ```pip install -r requirements.txt```

6. ```python glob_preprocessing.py```

7. ```python glob_clusterizing.py```

8. ```python thematic_clustering.py```

9. Для получения облака отзывов запустить файл 'result_analysis.py':

    ```python result_analysis.py```

    Появится консоль в которой необходимо выбрать один из трёх вариантов:
    - Для получения облака нейтральных отзывов ввести 0
    - Для получения облка позитивных отзывов ввести 1
    - Для получения облака негативных отзывов ввести 2
   
   Полученные облака отзывов находятся в папке images -- добавь картинку одну из тех что там лежит

10. Для получения рекоменаций по отдельному сотруднику запустить файл 'single_person.py':

    ```python single_person.py```

   ввести отзыв сотрудника строкой в консоль
   Полученный результат находится в папке 'responces' под именем 'recommendation.txt' -- добавить скрин того как открыт оттуда 'recommendation.txt'

11. Для получения report.pdf необходимо
    - ввести в консоль 
