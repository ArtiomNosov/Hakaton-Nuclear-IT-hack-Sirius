# Hakaton-Nuclear-IT-hack-Sirius
# [Аналитический дашборд на основе ответов сотрудников](https://datalens.yandex/u5r6316442j6h)
![image](https://github.com/user-attachments/assets/813efad9-d424-4915-b0a4-3e960f210947)
# [Ссылка на развёрнутый отчёт](https://disk.yandex.ru/i/3mXH5qQ0W0Agcw)
![image](https://github.com/user-attachments/assets/19885956-abf8-43dc-8f45-e8efc972c3ba)
PS: развёрнутый отчёт это report.pdf ниже написано как его получить
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

4. ```virtualenv envname```

5. ```envname\scripts\activate```

6. ```pip install numpy==1.26.4```

7. ```pip install -r requirements.txt```

##Получение обработанных данных

8. ```python glob_preprocessing.py```

##Разделение данных на три основных кластера: позитивные, негативные, нейтральные

9. ```python glob_clusterizing.py```

10. Для получения облака отзывов запустить файл 'result_analysis.py':

    ```python result_analysis.py```

    Появится консоль в которой необходимо выбрать один из трёх вариантов:
    - Для получения облака нейтральных отзывов ввести 0
    - Для получения облaка позитивных отзывов ввести 1
    - Для получения облака негативных отзывов ввести 2
   
   Полученные облака отзывов находятся в папке images -- добавь картинку одну из тех что там лежит

11. Для получения рекоменаций по отдельному сотруднику запустить файл 'single_person.py':

    ```python single_person.py```

   ввести отзыв сотрудника строкой в консоль
   Полученный результат находится в папке 'responces' под именем 'recomendation.txt' -- добавить скрин того как открыт оттуда 'recomendation.txt'

12. Для получения report.pdf необходимо
    - ввести в консоль ```result.py``` после чего файл "report.pdf" обновится
