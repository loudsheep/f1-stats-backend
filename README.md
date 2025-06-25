# F1 Stats Backend

A REST API providing comprehensive Formula 1 statistics, built with Django and FastF1. This backend serves as a data source for various F1 applications, offering information on race results, driver standings, circuit details, and more.

## Features

*   **Race Results:** Retrieve historical race results for specific seasons and rounds.
*   **Session Results:** Access detailed results for practice, qualifying, and race sessions.
*   **Driver and Constructor Standings:** Get up-to-date standings for drivers and constructors.
*   **Circuit Information:** Obtain details about specific circuits, including recent race winners.
*   **Event Schedule:** View the complete F1 event schedule, including country codes and circuit IDs.
*   **Championship Contenders:** Determine which drivers can still mathematically win the championship.
*   **Caching:** Utilizes FastF1's caching mechanism to improve performance and reduce API request load.
*   **REST API:** Provides a clean and well-documented REST API for easy integration.

## Technologies Used

*   **Python:** The primary programming language.
*   **Django:** A high-level Python web framework.
*   **Django REST Framework (DRF):** A powerful toolkit for building Web APIs.
*   **FastF1:** A Python library for accessing and analyzing Formula 1 data.
*   **pycountry:** A library providing ISO country information.
*   **Gunicorn:** A WSGI server for deploying the application.
*   **python-dotenv:** For managing environment variables.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/loudsheep/f1-stats-backend.git
    cd f1-stats-backend
    ```

2.  **Create a virtual environment (optional):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    # venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**

    *   Create a `.env` file in the project root directory.
    *   Add the following variables (replace with your actual values):

        ```
        SECRET_KEY=your_secret_key
        DEBUG=True # Set to False in production
        ALLOWED_HOSTS=* # Comma separated list of allowed hosts or * for all (Not recommended for production)
        ```

5.  **Run the development server:**

    ```bash
    python manage.py runserver
    ```

    The API will be accessible at `http://localhost:8000/`.

## Usage

Here are some example API endpoints:

*   **Get the remaining events for the current season:**

    ```
    GET /api/events_remaining/
    ```

*   **Get driver standings for a specific season:**

    ```
    GET /api/drivers_standings/?season=2023
    ```

*   **Get circuit information for a specific circuit, season, and round:**

    ```
    GET /api/circuit_info/?circuit_id=bahrain&season=2023&round=1
    ```

*   **Get race results for a specific season and round:**

    ```
    GET /api/race_results/?season=2023&round=1
    ```

*   **Get qualifying results for a specific season and round:**

    ```
    GET /api/session_results/?season=2023&round=1&session_name=Qualifying
    ```

## Project Structure

```
f1-stats-backend/
├── api/                      # Django app for the API
│   ├── __init__.py
│   ├── admin.py              # Django admin configuration
│   ├── apps.py               # App configuration
│   ├── models.py             # Database models
│   ├── seriallizers.py       # DRF serializers
│   ├── services/             # Logic for fetching and processing F1 data
│   │   └── fastf1/         # FastF1 related services
│   │       ├── __init__.py   # FastF1 initialization and caching
│   │       ├── circuit.py    # Circuit information retrieval
│   │       ├── results.py    # Race and session results retrieval
│   │       ├── schedule.py   # Event schedule retrieval
│   │       ├── standings.py  # Driver and constructor standings retrieval
│   │       └── whocanwin.py  # Championship contenders calculation
│   ├── tests.py              # Unit tests
│   ├── urls.py               # API URL patterns
│   └── views.py              # API view functions
├── f1stats/                  # Django project settings
│   ├── __init__.py
│   ├── asgi.py               # ASGI configuration
│   ├── settings.py           # Project settings
│   ├── urls.py               # Project URL patterns
│   └── wsgi.py               # WSGI configuration
├── definitions.py          # Project-level definitions (e.g., ROOT_DIR)
├── manage.py               # Django management script
├── requirements.txt        # Project dependencies
└── LICENSE                   # License file
```

## Contributing

We welcome contributions to the F1 Stats Backend! Please follow these guidelines:

1.  **Fork the repository.**
2.  **Create a new branch for your feature or bug fix.**
3.  **Write clear and concise commit messages.**
4.  **Submit a pull request with a detailed description of your changes.**
5.  **Follow the existing code style and conventions.**
6.  **Include unit tests for any new functionality.**

## License

This project is licensed under the GNU Affero General Public License v3.0 - see the [LICENSE](LICENSE) file for details.
