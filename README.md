# Chat Box Using Django

In this project there is an online Chat Box with signup and forgot password verification mail . By this project you will get to know about the Rest framework of django and also large amount of  `Javascript`  In this project  `AJAX LIVE SEARCH` is also used that displays the result of username search In this  audio has been also added while sending and receiving mail.

# [](https://github.com/saloniig/Online-School-System#about-django)About Django

Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

## [](https://github.com/saloniig/Online-School-System#features)Features

-   A split of  `settings.py`  that allows for different values in development versus production
-   Preinstallation of Django's automatic administration panel
-   Preconfiguration of  `urls.py`  to serve static, media and Munin files
-   Preconfiguration of logging options
-   Preinstallation of django-debug-toolbar
-   Preconfiguration of our preferred caching options for development and production
-   Management commands for scheduling database backups retrieving them for local installation.
-   Custom context processors that provide the current site and environment

## [](https://github.com/saloniig/Online-School-System#requirements)Requirements

-   [Django](https://www.djangoproject.com/download/)
-   [virtualenv](http://www.virtualenv.org/en/latest/)

# [](https://github.com/saloniig/Online-School-System#getting-started)Getting started

## [](https://github.com/saloniig/Online-School-System#table-of-contents)Table of Contents

-   [Part 1 - Getting Started](https://simpleisbetterthancomplex.com/series/2017/09/04/a-complete-beginners-guide-to-django-part-1.html)
-   [Part 2 - Fundamentals](https://simpleisbetterthancomplex.com/series/2017/09/11/a-complete-beginners-guide-to-django-part-2.html)
-   [Part 3 - Advanced Concepts](https://simpleisbetterthancomplex.com/series/2017/09/18/a-complete-beginners-guide-to-django-part-3.html)
-   [Part 4 - Authentication](https://simpleisbetterthancomplex.com/series/2017/09/25/a-complete-beginners-guide-to-django-part-4.html)
-   [Part 5 - ORM](https://simpleisbetterthancomplex.com/series/2017/10/02/a-complete-beginners-guide-to-django-part-5.html)
-   [Part 6 - Class-Based Views](https://simpleisbetterthancomplex.com/series/2017/10/09/a-complete-beginners-guide-to-django-part-6.html)
-   [Part 7 - Deployment](https://simpleisbetterthancomplex.com/series/2017/10/16/a-complete-beginners-guide-to-django-part-7.html)
-   [Part 8 - Django Reset Password With Email Verification](https://hackace2.wordpress.com/2020/04/11/django-reset-password-with-email-verification/)
-   [Part 9 - How to Create a Password Reset View](https://hackace2.wordpress.com/2020/04/11/how-to-create-a-password-reset-view/)

For the complete tutorial series index  [click here](https://simpleisbetterthancomplex.com/series/beginners-guide/1.11/).

# [](https://github.com/saloniig/Online-School-System#installation)Installation

Please check the official django installation guide for server requirements before you start. Official Documentation

## [](https://github.com/saloniig/Online-School-System#setup)Setup

Create a virtual enviroment to work inside.

`virtualenv my-environment`

Jump in and turn it on.

`cd my-environment`

`. bin/activate`

### [](https://github.com/saloniig/Online-School-System#install-django)Install Django:

`pip install Django`

### Other commands:
`pip install django` 

`pip install django-emoji-picker`

`pip install mysqlclient`

`python -m pip install Pillow`

### [](https://github.com/saloniig/Online-School-System#perform-database-migration)Perform database migration:

`python manage.py makemigrations`

`python manage.py migrate`


### [](https://github.com/saloniig/Online-School-System#run-development-server)Run Development Server

`python manage.py runserver`

You can now access the server at  [http://localhost:8000](http://localhost:8000/)

## [](https://github.com/saloniig/Online-School-System#project-filefolder-structure)Project File/Folder Structure

What I’ve changed ?

-   All Django apps live under  `box/`  folder.
-   All of the models live under  `models.py`  file.
-   All of the admin files live under  `admin.py`  file. -- All of the views live under generated app’s  `views/`  folder.
-   Every app should contain It’s own  `urls.py`.
-   All settings related files will live under  `settings.py`  file.
-   Every environment has It’s own setting such as
-   Every environment/settings can have It’s own package/module requirements.
-   All of the templates live under basedir’s  `templates/APP_NAME`  folder.
-   Additional files such as images, JavaScript, or CSS are live under  `static/box`  folder.
-   Every environment/settings can have It’s own package/module requirements.

#### [](https://github.com/saloniig/Online-School-System#here-is-directoryfile-structure)Here is directory/file structure:

```


Chat-Box/
    manage.py
    Chat/
       __init__.py
       settings.py
       urls.py
       wsgi.py
    box/
       migrations/
               __init__.py
       __init__.py
       admin.py
       static
       templates
       models.py
       tests.py
       views.py

```

## [](https://github.com/saloniig/Online-School-System#documentation)Documentation

You can see the documentation over at  **Read the Docs**:  [django-project-skeleton](http://django-project-skeleton.readthedocs.org/en/latest/)
