🚀 Xplore Trends

A full-stack project that scrapes the top 5 trending topics from X (Twitter) and displays them on a simple dashboard.
This project was built as part of the FullStackIntern Assignment.

📖 Project Overview

Xplore Trends is designed to help users stay updated with the latest trending topics on X (formerly Twitter).
The project automatically scrapes trending topics, stores them in a PostgreSQL database, and provides a React frontend dashboard for easy viewing.

Goals of the project:

Learn and demonstrate full-stack development using Django and React.

Work with web scraping (Selenium) to fetch real-time trending data.

Build a RESTful API to serve frontend data dynamically.

Store and manage data reliably in PostgreSQL.

🛠️ Tech Stack

Frontend: React (Vite)

Backend: Django + Django REST Framework

Scraper: Selenium (without IP rotation)

Database: PostgreSQL

Other: Axios (frontend API calls), Python-dotenv for environment variables

📂 Project Structure
Xplore_Trends/
├── frontend/              # React frontend (Vite)
├── X_scraper/             # Django backend
│   ├── X_scraper/         # Django project settings
│   ├── trends_scraper/    # Django app + scraper scripts
│   ├── db.sqlite3         # (if using local dev database)
│   └── manage.py
├── .gitignore
└── README.md

⚙️ Setup Instructions
1️⃣ Clone the repository
git clone https://github.com/Baishnavi007/Xplore_Trends.git
cd Xplore_Trends

2️⃣ Backend Setup (Django)
cd X_scraper


# Install dependencies
pip install -r requirements.txt

# Setup environment variables
cp .env.example .env
# Edit .env to add your SECRET_KEY, DATABASE_URL, etc.

# Migrate database
python manage.py migrate

# Run development server
python manage.py runserver
# Backend will start at http://127.0.0.1:8000

3️⃣ Frontend Setup (React)
cd frontend
npm install
npm run dev
# Frontend will start at http://localhost:5173

🔗 API Endpoints (Django REST Framework)
Method	Endpoint	Description
GET	/api/trends/	Fetch list of top trending topics
GET	/api/trends/<id>	Fetch details of a single trend
POST	/api/add/	Add a new trend (if authentication allows)
POST	/api/login/	Authenticate a user and get token

Authentication is handled by Django’s built-in auth system (if any endpoints require login).

🗄️ Database

PostgreSQL stores all scraped trends.

Each trend includes:

Title

Description

Link (to original post)

Timestamp of scraping

📸 Example Database Table Screenshot:
Here is the PostgreSQL table where scraped data is stored:  

![Database Screenshot](https://github.com/user-attachments/assets/e1300662-ca1d-4177-8304-b1a611a69252)


💻 Scraper

Selenium is used to scrape the top 5 trending topics from X (Twitter).

Currently, scraping is manual (run the script via Django management command or directly in trends_scraper/scraper.py).

Stores results directly in the PostgreSQL database via Django ORM.

🖥️ Frontend Features

Displays the latest trends in a clean, responsive dashboard.

Each trend shows: title, description, and link.

Can fetch updated trends using the backend API.



🚀 Deployment

Currently designed for local development.

To deploy:

Use Gunicorn + Nginx for backend on a Linux server.

Frontend can be built with npm run build and served as static files.

Ensure .env is configured with SECRET_KEY and DATABASE_URL.

✅ Evaluation Checklist

 Scraper reliably fetches top 5 trends

 Data stored in PostgreSQL

 Backend REST API working

 Frontend displays results clearly

 Easy to setup with README

📝 Special Notes

Selenium requires a valid X (Twitter) account login.

.env contains sensitive keys and is not uploaded. Create your own .env based on .env.example.

⚡ Future Improvements

Automate scraping using Django management commands + cron jobs.

Add pagination for large number of trends.

Enhance UI/UX with trend categories and search functionality.

Implement user authentication to allow adding or favoriting trends.
