# ExpensesControl
Web application for money management. The project was created to learn the Django framework. 
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Installation](#installation)
* [Source file overview](#source-file-overview)
* [Inspirations](#inspirations)

## General info
 The main task of the application is to control the user's expenses and income. The app allows registration and login. Users can personalize their profile picture and personal information. It gives us the ability to add, delete and edit new expense and revenue. It displays summaries of the month.

## Technologies
* Python 3.9.9
* Django 3.2.9
* pip 21.3.1
* asgiref 3.4.1
* django-crispy-forms 1.13.0
* Pillow 8.4.8
* pytz 2021.3
* setuptools 58.3.0
* sqlparse 0.4.2
* wheel 0.37.0
* Bootstrap 5

## Installation

First install the packages from the [Technologies](#technologies) chapter. Then download the source files and unzip them on your computer. Open cmd and navigate to the extracted folder, use the command:
```console
c:> python manage.py migrate
c:> python manage.py migrate --run-syncdb
```

And you can run the application with the command:
```console
c:> python manage.py runserver
```

## Source file overview
Basic structure of the project:
* ExpensesControl\
-- Folder containing application settings
* mainApp
-- Folder containing project files related to the operation of the application without a logged on user
* media\
-- Folder containing photos added by the user as a profile photo in the subfolder "profile_pics"
* users\
-- The folder contains the user profile model, files that allow the user to register, log in and manage their account.
* wallet\
-- The folder contains the Expenses and Revenue model, it also contains files to manage them. Performs the task for which the entire application was created
* manage.py
-- A file that manages the entire project

## Inspirations
This app is based on tutorial to Django [Corey Schafer](https://www.youtube.com/watch?v=UmljXZIypDc)
