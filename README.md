# Book-List-Project

A dynamic, user-focused library management application built with Python, Django, PostgreSQL, and the Google Books API.

## Key Features

-   User authentication
-   Real-time book search via Google Books API
-   Personalized reading list creation

## Prerequisites

Make sure you have installed the following:

-   Python 3.8 or later
-   PostgreSQL
-   Django 3.0 or later

## Database Setup

Ensure that PostgreSQL is running on port 5432.

Create a database using the following settings:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## Running the Application

To run the application, navigate to the directory where you have cloned or downloaded this repository and type the following command:

`python manage.py runserver`

Now, open your browser and navigate to http://127.0.0.1:8000/ to see the application running.

## Contributing

We welcome contributions to this project. Feel free to open an issue or submit a pull request.
