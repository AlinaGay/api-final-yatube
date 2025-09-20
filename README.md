# api_final  
API for Yatube  

**Yatube** is a blogging platform that allows users to register, create, edit or delete their own posts, comment on other authors' posts, and follow them.

## How to Run the Project

Clone the repository and navigate into it in the command line:
```bash
git clone https://github.com/AlinaGay/api-final-yatube.git
cd yatube_api
```

Create and activate a virtual environment:

```
python3 -m venv env
```

```
source env/bin/activate
```

Install the dependencies from the requirements.txt file:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Apply migrations:

```
python3 manage.py migrate
```

Start the project:

```
python3 manage.py runserver
```

### Some API Request Examples

To view the existing blog posts, send a GET request to:

```
http://127.0.0.1:8000/api/v1/posts/
```
To view comments on a specific post, send a GET request to (replace <post_id> with the desired post ID):
```
http://127.0.0.1:8000/api/v1/posts/<post_id>/comments/
```
By default, the project runs on:

```
http://127.0.0.1:8000
```
However, if you run the server on a different port, use that port in the URLs above.

### Tech Stack

**Backend:**
- Python 5.1.1
- Django (web framework)
- Django REST Framework (REST API)
- Djoser (JWT authentication)
- Pillow (image processing)

**Database**
- SQLite (for development)


### Documentation

After starting the project, the documentation is available at:

```bash

# ReDoc
http://127.0.0.1:8000/redoc/
```

For testing the API, you can use:
- Postman коллекцию (лежит в `/postman_collection/API_for_yatube.postman_collection.json`)

### Author

| [AlinaGay](https://github.com/AlinaGay/) |
| Backend Developer • Python Engineer  
