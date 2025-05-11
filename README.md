# Country Info Hub

This project is a Django-based web application that fetches country data from an external API, stores it in a database, provides RESTful APIs, and displays the data on a secure web interface. The application includes user authentication and follows the requirements outlined in the assignment.

## Project Overview

The application:
- Fetches country data from https://restcountries.com/v3.1/all.
- Stores the data in a Django-managed database.
- Provides RESTful APIs for country-related operations.
- Displays country information on a web interface with search functionality.
- Secures the application with Django's authentication system.

## Database Schema
The following Entity-Relationship Diagram (ERD) illustrates the database structure, including `Capitals`, `Timezones`, `Continents` `Currencies` and `Languages`:

![ERD Diagram](docs/ERD%20Country.png)
## Prerequisites

Ensure you have the following installed:
- Python 3.12.3
- pip (Python package manager)
- Virtualenv (recommended for isolated environments)
- Git

## Installation Steps

1. **Clone the Repository**  
   Clone the project from the public repository:
   ```bash
   git clone https://github.com/imsnto/CountryInfoHub
   cd CountryInfoHub
   ```

2. **Set Up a Virtual Environment**  
   Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**  
   Install the required Python packages listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
   
4. **.env file**
    Create a `.env` file.  and set this
    `COUNTRY_API_URL=https://restcountries.com/v3.1/all`

5. **Set up the database**:
   ```bash
   python manage.py migrate
   ```

6. **Fetch and store country data**:
   Run the data fetching script to populate the database:
   ```bash
   python manage.py fetch_countries
   ```

7. **Create a superuser** (for admin access):
   ```bash
   python manage.py createsuperuser
   

## Running the Application

1. **Start the Django development server**:
   ```bash
   python manage.py runserver
   ```

2. **Access the application**:
   - Web interface: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/
   - API root: http://127.0.0.1:8000/api/
   - Swagger endpoints: http://127.0.0.1:8000/api/docs/


## Project Structure`
```
country_info_hub/
   ├── accounts/
       ├── templates/
       ├── models.py
       ├── serializers.py
       ├── formm.py
       ├── urls.py
       ├── views.py
   ├── countries/
       ├── management
         ├── commands
           ├── fetch_countries.py
       ├── models.py
       ├── serializers.py
       ├── urls.py
       ├── views.py
       ├── filters.py
   ├── country_info_hub/
       ├── settings.py
       ├── urls.py
   ├── docs/
   ├── templates/
   ├── .env
   ├── manage.py
   ├── README.md
   ├── requirements.txt

```
## API Endpoints
### Accessing the API
- **Swagger UI**: View and test endpoints at `http://127.0.0.1:8000/api/docs/`.
- **Schema**: Download the OpenAPI schema at `http://127.0.0.1:8000/api/schema/`.

### Key Endpoints
- accounts
  - `POST /accounts/api-token-auth/` : Get token key 

- api
  - `GET /api/countries/`: List all countries
  - `GET /api/countries/<id>/`: Retrieve specific country details
  - `POST /api/countries/`: Create a new country
  - `PUT /api/countries/<id>/`: Update a country
  - `DELETE /api/countries/<id>/`: Delete a country
  - `GET /api/countries/{id}/region/`: List countries in the same region
  - `GET /api/countries/?languages=<language-name>`: List countries by language
  - `GET /api/countries/?search=<country-name>`: Search countries by name

## Authentication
- Used Token based authentication.
- Obtain a token when login using swagger, it returns a token or run this command in terminal. `curl -X POST -d "username=<your_username>&password=<your_password>" http://127.0.0.1:8000/accounts/api-token-auth/`
- Use token in header `Authorization: Token <token>` (if you use postman)

## Web Interface
- **Home Page**: Displays a table of countries with name, cca2, capital, population, timezone, and flag.
- **Search**: Allows partial name search for countries.
- **Details Button**: Shows same-region countries and spoken languages.
- **Login Page**: Required for accessing the country list and APIs.