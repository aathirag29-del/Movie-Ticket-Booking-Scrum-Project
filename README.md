# Movie Ticket Booking Application

**Agile/Scrum Mini-Project — Assignment 2**

A Flask + SQLite movie ticket booking application with Tamil, English and regional-language movies. It includes registration/login, movie search and filters, show timings, seat selection, demo payment, e-ticket, booking history, reviews and personalized recommendations.

## Features

* 16 sample movies across Tamil, English, Malayalam and Telugu
* Search, language and genre filters
* Cinema/show-time selection
* Seat selection (1–8 seats)
* Demo UPI/Card/Net Banking checkout
* E-ticket and booking history
* Reviews
* Personalized recommendations based on preferred language and high-rated genres
* Responsive UI

## Run

```powershell
python -m venv venv
venv\\\\Scripts\\\\activate
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000`.

## Recommendation Logic

The recommendation feature is intentionally simple and explainable. It first uses the user's preferred language. If the user has given 4/5-star reviews, the genres of those liked movies are used to find matching movies in the preferred language. Otherwise, movies in the preferred language are shown.

## Assignment 2

The supplied Assignment 2 guidelines require a working app, organized source, meaningful commits, a feature/development branch and merge, README, testing evidence, application screenshots, GitHub screenshots and a PDF report. See `docs/` for supporting material.

\## Development Update



The movie booking application was developed using Flask, SQLite, HTML, CSS and JavaScript. The project supports user registration, movie browsing, seat selection, booking, payment demo and e-ticket generation.

