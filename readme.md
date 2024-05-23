# Описание:
веб-приложение, которое на любой GET-запрос возвращает html-страницу с подключенными Bootstrap стилями.

## Настройки:
Для работы программы необходимо создать файл `.env` с параметрами запуска сервера:
- HOST - адрес для доступа по сети
- PORT - порт для доступа по сети

## Установка и использование:

Для работы программы необходимо установить зависимости, указанные в файле  pyproject.toml:
- для первичной установки:

  ```poetry install```
- для обновления:

  ```poetry update```

## Запуск:
```python main.py```