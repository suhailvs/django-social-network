# Django Social Network

Django Social Network is an open source **enterprise social network** built with [Python][0] using the [Django Web Framework][1].

The project has three basic apps:

* Feed (A Twitter-like microblog)
* Articles (A collaborative blog)
* Question & Answers (A Stack Overflow-like platform)

## Feed App

The Feed app has infinite scrolling, activity notifications, live updates for likes and comments, and comment tracking.


## Articles App

The Articles app is a basic blog, with articles pagination, tag filtering and draft management.


## Question & Answers App

The Q&A app works just like Stack Overflow. You can mark a question as favorite, vote up or vote down answers, accept an answer and so on.


## Technology Stack

- Python 3.8
- Django 3.1.7
- Twitter Bootstrap 3
- jQuery 2


## Installation Guide

	python3 -m venv env
	source env/bin/activate
	pip install -r requirements.txt
	./manage.py migrate
	./manage.py runserver

vist <http://localhost:8000>

## Demo

Try Django Social Network now at [https://djangosocialnetwork.herokuapp.com][2].

[0]: https://www.python.org/
[1]: https://www.djangoproject.com/
[2]: https://djangosocialnetwork.herokuapp.com/