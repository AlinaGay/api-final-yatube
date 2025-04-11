# api_final
### API для Yatube

Yatube — это платформа для блогов. Этот блог-сервис предполагает возможность зарегистрироваться, создать, отредактировать или удалить собственный пост, прокомментировать пост другого автора и подписаться на него.


### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/AlinaGay/api-final-yatube.git
```

```
cd yatube_api
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Некоторые примеры запросов к API:

Чтобы посмотреть имеющиеся посты в блоге можно сделать GET-запрос на следующий URL:

```
http://127.0.0.1:8000/api/v1/posts/
```
Чтобы посмотреть комментарии к конкретному посту можно сделать GET-запрос на следующий URL, поставив post_id  в запрос:
```
http://127.0.0.1:8000/api/v1/posts/<post_id>/comments/
```
По умолчанию проект запускается на порту:

```
http://127.0.0.1:8000
```
Однако порт может быть изменен. В таком случае, необходимо подставить другой адрес порта в вышеуказанные примеры запросов.

### Технологический стек

**Backend:**
- Python 5.1.1
- Django (веб-фреймворк)
- Django REST Framework (REST API)
- Djoser (аутентификация по JWT)
- Pillow (обработка изображений)

**База данных:**
- SQLite (разработка)


### Документация

После запуска проекта документация доступна:

```bash

# ReDoc
http://127.0.0.1:8000/redoc/
```

Для тестирования API можно использовать:
- Postman коллекцию (лежит в `/postman_collection/API_for_yatube.postman_collection.json`)

### Автор

| [Alina Opolskaia](https://github.com/AlinaGay/) |
| Backend Developer • Python Engineer  
