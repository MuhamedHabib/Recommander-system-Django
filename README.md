# Recommender System (Django)

> A Django web application for browsing a large movie catalog and generating content-based movie recommendations from genre similarity.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

## Overview

This project is a movie recommender web app built with Django. A dataset of roughly **23,000 movies** (`movies.csv`) is loaded into the database via a custom management command, and a single `movierecommender` app serves a styled catalog page listing movies for the user.

The recommendation approach is **content-based filtering using movie genres**. The design intent (captured in the management command and view logic) is to compare an unwatched movie against the movies a user has already watched and flag it as `recommended` when the genre overlap is high — the intended similarity measure is **Jaccard similarity over the genre sets**.

The web view reflects this two-stage design:

- If any movies are flagged `recommended`, the catalog shows the top recommended, unwatched movies (ordered by `vote_count`).
- If no recommendations have been generated yet, it falls back to a **popularity ranking** — the top unwatched movies by vote count — so the page always has content.

> **Honest status note.** The data pipeline, models, admin, web view, and the fallback popularity ranking are fully working. The genre-based recommendation engine itself (`make_recommendations` command) is currently a **scaffold**: the `check_valid_genres` helper is implemented, but the Jaccard / movie-similarity scoring methods and the command's `handle()` body are left as documented stubs to be filled in. Until that command is completed and run, the catalog operates in its popularity-fallback mode. This README describes the code as it actually exists in the repository.

## Features

- **Bulk catalog ingestion** — load ~23k movies from a CSV file into the database with `pandas` in one management command.
- **Movie data model** — IMDB id, genres, language, title, release date, overview, average vote, vote count, poster path, plus `watched` and `recommended` flags.
- **Django admin** — browse, search (by title/overview), and curate the catalog; mark movies as `watched` to drive recommendations.
- **Content-based recommendation design** — genre-similarity (Jaccard) scaffold that flags unwatched movies similar to watched ones.
- **Popularity fallback** — when no recommendations exist, the catalog surfaces the most-voted unwatched movies so the page is never empty.
- **Styled front end** — responsive catalog, about, contact, and services pages with a Bootstrap/jQuery theme and static assets.

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python |
| Web framework | Django 3.2 |
| Data processing | pandas, NumPy |
| Imaging | Pillow |
| Database | MySQL (configured in `settings.py`) |
| Front end | Django templates, Bootstrap, jQuery, Font Awesome |

## Project Structure

```
Recommander-system-Django/
├── manage.py
├── movies.csv                      # Movie dataset (~23k rows)
├── requirements.txt
├── recommender/                    # Project configuration
│   ├── settings.py                 # Apps, MySQL config, middleware
│   ├── urls.py                     # Root URL routing
│   ├── wsgi.py / asgi.py
└── movierecommender/               # Main application
    ├── models.py                   # Movie model
    ├── views.py                    # Catalog view + recommendation context
    ├── urls.py                     # App routes
    ├── admin.py                    # Movie admin (search, list display)
    ├── migrations/                 # Initial Movie schema
    ├── management/commands/
    │   ├── load_movies.py          # CSV → database loader
    │   └── make_recommendations.py # Genre-similarity recommender (scaffold)
    ├── templates/movierecommender/ # index, movie_list, about, contact, services
    ├── static/                     # CSS, JS, fonts, images
    └── assets/                     # Theme assets
```

## Getting Started

### Prerequisites

- Python 3
- A running **MySQL** server (the project is configured for the MySQL backend)

### 1. Clone and enter the project

```bash
git clone https://github.com/MuhamedHabib/RecommanderDjango.git
cd RecommanderDjango
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> The MySQL backend also requires a driver such as `mysqlclient` (`pip install mysqlclient`).

### 4. Configure the database

Open `recommender/settings.py` and set the `DATABASES` values to match your local MySQL instance (database name, user, password, host, and port). Create the target database in MySQL before migrating.

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Load the movie dataset

```bash
python manage.py load_movies --path movies.csv
```

### 7. (Optional) Generate recommendations

```bash
python manage.py make_recommendations
```

> This command is the genre-similarity scaffold described above. Until its similarity logic is implemented, the catalog uses the popularity fallback.

### 8. Run the development server

```bash
python manage.py runserver
```

Then open the app in your browser:

- Catalog: `http://127.0.0.1:8000/movierecommender/`
- Admin: `http://127.0.0.1:8000/admin/` (create a superuser first with `python manage.py createsuperuser`)

## Notes

- **Recommendation method:** content-based filtering on movie genres (Jaccard similarity); the scoring command is a documented scaffold, and the live view uses a vote-count popularity fallback when no recommendations are present.
- **Database:** configured for MySQL in `settings.py`; adjust the connection settings to your environment before running migrations.
- **Security:** `DEBUG = True` and a development `SECRET_KEY` are committed for local use only. Set `DEBUG = False`, supply a fresh secret key from the environment, and configure `ALLOWED_HOSTS` before any deployment.
- **Dataset:** `movies.csv` contains the movie catalog with IMDB id, genres, language, release date, title, overview, vote average, vote count, and poster path columns.

---
<p align="center">Built by <b>Mohamed Habib Khattat</b> — <a href="https://github.com/MuhamedHabib">GitHub (@MuhamedHabib)</a> · <a href="https://www.linkedin.com/in/mohamed-habib-khattat-2b206a173">LinkedIn</a></p>
