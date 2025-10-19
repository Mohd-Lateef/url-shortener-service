
# URL Shortener API

A simple and efficient URL shortener service built with FastAPI, SQLAlchemy, and PostgreSQL.
This application provides endpoints to create shortened URLs and redirect users to the original long URL.

## Features

* **Shorten URLs:** Converts a long URL into a compact, easy-to-share short URL.
* **URL Redirection:** Automatically redirects users from the short URL to the original destination.
* **Idempotent:** If a URL has already been shortened, the existing short URL is returned.
* **Fast & Asynchronous:** Built with FastAPI for high performance.

## Tech Stack

* **Backend:** Python, FastAPI
* **Database:** PostgreSQL
* **ORM:** SQLAlchemy
* **Server:** Uvicorn

## Project Structure

Here is an overview of the project's file structure:


```

URL-SHORTNER/

├── app/

│ ├── init.py

│ ├── crud.py # Contains core database logic (Create, Read).

│ ├── database.py # Database connection and session management.

│ ├── main.py # Main FastAPI application and API endpoints.

│ ├── models.py # SQLAlchemy database models.

│ ├── schemas.py # Pydantic data validation schemas.

│ └── utils.py # Utility functions (e.g., Base62 conversion).

├── .env # Environment variables (e.g., database URL).

├── .gitignore # Files and directories to be ignored by Git.

├── README.md # Project documentation.

└── requirements.txt # Project dependencies.

```

## Setup and Installation

### 1. Prerequisites

* Python 3.8+
* PostgreSQL

### 2. Clone the Repository

```sh
# Step 1: Download the project from GitHub
git clone https://github.com/Mohd-Lateef/url-shortener-service.git
# Step 2: Move into the newly created project folder
cd url-shortener-service

```

### 3. Create a Virtual Environment

It's recommended to use a virtual environment to manage project dependencies.

Bash

```
# For Windows
python -m venv .venv
.\.venv\Scripts\activate

# For macOS/Linux
python3 -m venv .venv
source .venv/bin/activate

```

### 4. Install Dependencies

Install all the required packages from `requirements.txt`.

Bash

```
pip install -r requirements.txt

```

### 5. Configure Environment Variables

Create a `.env` file in the project root and add your PostgreSQL database connection URL.
```
db_url = postgresql://<user>:<password>@<host>:<port>/<database_name>

# Example:
db_url = postgresql://postgres:password@localhost:5432/url_shortener_db

```

The application will automatically create the necessary `urls` table in your database upon starting.

## How to Run

Start the FastAPI application using Uvicorn.

Bash

```
uvicorn app.main:app --reload

```

The application will be running at `http://127.0.0.1:8000`.

## API Endpoints

### 1. Shorten a URL

-   **Endpoint:** `POST /ShortenURL`
    
-   **Description:** Creates a short URL for a given long URL.
    
-   **Query Parameter:** `url` (string, required) - The original URL to shorten.
    
-   **Success Response (200 OK):**
    
    ```
    "localhost:8000/b"
    
    ```
    
-   **Example using curl:**
    
    Bash
    
    ```
    curl -X 'POST' \
      'http://127.0.0.1:8000/ShortenURL?url=https%3A%2F%2Fwww.google.com/application/json' -d ""
    
    ```
    

### 2. Redirect to Original URL

-   **Endpoint:** `GET /{shortCode}`
    
-   **Description:** Redirects to the original URL corresponding to the provided short code.
    
-   **Path Parameter:** `shortCode` (string, required) - The unique code for the shortened URL.
    
-   **Success Response (307 Temporary Redirect):** Redirects to the original URL.
    
-   **Error Response (404 Not Found):** If the short code does not exist.
    
    JSON
    
    ```
    {
      "detail": "URL not found"
    }
    
    ```
    
-   Example in a browser:
    
    Navigate to http://127.0.0.1:8000/b (using the short code from the previous example), and you will be redirected to https://www.google.com.
    

## How It Works

1.  When a user submits a long URL to the `POST /ShortenURL` endpoint, the application first checks if the URL already exists in the database.
    
2.  If it exists, the existing short URL is returned.
    
3.  If it's a new URL, a new record is created in the `urls` table. This generates a unique integer `id`.
    
4.  This `id` is then converted into a short, URL-safe Base62 string (e.g., `1` -> `b`, `10` -> `k`). This string becomes the `short_code`.
    
5.  The `short_code` is saved to the database record, and the full short URL is returned to the user.
    
6.  When a user accesses the `GET /{shortCode}` endpoint, the application looks up the `short_code` in the database, retrieves the corresponding `original_url`, and issues a 307 redirect.