# MyLife - a Plan for Life tool

![Heroku](https://img.shields.io/badge/Deployed-Heroku-blueviolet)
![Built With](https://img.shields.io/badge/Built%20With-Django%20%7C%20PostgreSQL%20%7C%20Heroku-green)
![Auth](https://img.shields.io/badge/Auth-User%20Login%20%26%20Permissions-brightgreen)
![Status](https://img.shields.io/badge/Status-LIVE-success)

links:

- [Project Planning Link: https://trello.com/b/UTyEg6Mh/myplanforlife ](https://trello.com/b/UTyEg6Mh/myplanforlife)

- [GitHub Repo Link: https://github.com/kjwagner613/MyPlanForLife.git](https://github.com/kjwagner613/MyPlanForLife.git):

- [Deployed Project Link: https://lifeplan-69c616f99dcc.herokuapp.com/ ](https://lifeplan-69c616f99dcc.herokuapp.com/)

A little about why this application.
It seems to me that the people who love us are usually more interested in our wellbeing then we are. I know I put more energy into the wellness of my wife, and when she could. she put a lot into mine.
its not that personal wellness isn't important to me, just that it always seemed selfish to spend time like that on me when there is always so much needing to be done to increase quality of life for those I love.
so i started to make this, but instead of me entering my info and creating my schedules to take care of myself, why not allow someone who has the motivation to do so create it with you and I with them.
Adding doctor recommendations, appointments, special meal requirements, considering spiritual, mental and physical wellness in one place, where the development of the data and adherence to the program you set, is shared with
those closest to you.
Fringe benefit that I began to discover is that just in using something like that. The time spent in such close space with a partner, family member, will realize mental, emotional and spiritual benefits all by itself.

A personal wellness application built with Django, deployed to Heroku.

## 💡 Overview

MyPlanForLife is a self-help web application that empowers users to create structured spiritual and meal plans for personal growth. It features weekly planning, a calendar view, and gentle reminders to support a balanced life.

## 🚀 Features

- User registration and login
- Create/edit/view/update personalized wellness plans
- Meal plan creation
- Calendar view of plans
- Friendly custom error pages
- Responsive design with visual enhancements

## 🧑‍💻 Technologies Used

- Python
- Django
- PostgreSQL
- HTML/CSS
- Bootstrap
- Heroku
- WhiteNoise (for static file serving)

## 📁 File Structure

- `myplanforlife/` — Django project settings
- `mylife/` — Main application for meal and spiritual plans
- `templates/` — HTML templates
- `static/` — Stylesheets and static assets

## 🌐 Deployed App

[Heroku App](https://myplanforlife-05b1598c3053.herokuapp.com)

## ☁️ Deploy to Heroku (Postgres)

This project is already configured for Heroku with:

- `Procfile` for web + release (migrations)
- `runtime.txt` for Python version
- `DATABASE_URL` support in Django settings
- WhiteNoise static file serving

### 1. Create app and Postgres

```bash
heroku login
heroku create your-app-name
heroku addons:create heroku-postgresql:essential-0 --app your-app-name
```

### 2. Set required config vars

```bash
heroku config:set SECRET_KEY="replace-with-a-strong-secret" --app your-app-name
heroku config:set DEBUG=False --app your-app-name
heroku config:set ALLOWED_HOSTS="your-app-name.herokuapp.com" --app your-app-name
```

`DATABASE_URL` is set automatically by the Postgres add-on.

### 3. Deploy

```bash
git push heroku main
```

### 4. Create admin user

```bash
heroku run python manage.py createsuperuser --app your-app-name
```

### 5. Open app

```bash
heroku open --app your-app-name
```

## 🧪 Run Locally for Demo

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py runserver
```

If you want local Postgres instead of sqlite, set `DATABASE_URL` in `.env`.

## Next for this app:

- Build out the programs to make them pre-defined, or custom input, possible engage cosultants interested
- Pilot group w/ doctor office and client partner app so office staff can provide content to patient mobiles.
- Basically, build out everything. this is was just enough i hope to present the idea.
- If to continue, assess viability by pilot w/Dr office.

## 🙏 Author

Kevin Wagner — Full-stack developer in training,
