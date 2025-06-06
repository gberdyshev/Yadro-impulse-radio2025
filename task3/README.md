# Запуск через Docker

Для передачи параметров (имени файла и слова для поиска) используются переменные окружения. Их можно задать через файл `.env` или любым другим способом.

## Сборка

```bash
docker build -t task 
```
## Запуск

В случае с .env файлом:

```bash
docker run -d --env-file .env task
```

Или через прямую передачу переменных:ы

```bash
docker run -e FILENAME=config.txt -e WORD=path task
```
Путь до файла ``config.txt`` указывается относительно ФС в Docker!


## Пример вывода

```bash
path: /home/user/data
log path: /var/log/app
```

