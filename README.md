# URL Shortener

A full-stack URL shortener application built with a FastAPI backend and a React frontend.

## Tech Stack

* **Backend:** Python, FastAPI, SQLAlchemy, PostgreSQL
* **Frontend:** React, TailwindCSS
* **AI Assisted:** The frontend UI was built with assistance from Claude.ai.

## Features

* Converts long URLs into short, shareable links.
* Redirects short links to their original destination.
* Generates a downloadable QR code for each short link.
* Saves a local history of recently created links.
* Copy-to-clipboard functionality.
* Dark / Light mode toggle.

## How to Run

### Backend (FastAPI)

1.  **Install Dependencies:**
    ```sh
    pip install -r requirements.txt
    ```
2.  **Configure Database:**
    Create a `.env` file in the project root with your PostgreSQL connection string:
    ```
    db_url = postgresql://user:password@localhost/url_shortener_db
    ```
3.  **Run Server:**
    The server will run on `http://127.0.0.1:8000`.
    ```sh
    uvicorn app.main:app --reload
    ```

### Frontend (React)

1.  **Install Dependencies:**
    ```sh
    npm install
    ```
2.  **Run App:**
    The app will run on `http://localhost:3000`.
    ```sh
    npm start
    ```
    *Note: The frontend expects the API to be at `http://localhost:8000`.*

## API Endpoints

* `POST /ShortenURL?url={url}`: Creates a short URL.
* `GET /{shortCode}`: Redirects to the original URL.