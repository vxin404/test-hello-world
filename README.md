# Advanced Calculator - FastAPI Web Service

A full-featured web calculator with scientific functions, built with FastAPI.

## Project Structure

```
test-hello-world/
├── app/
│   ├── __init__.py
│   ├── api/                    # API routes
│   │   ├── __init__.py
│   │   ├── calculator.py       # Calculator API endpoints
│   │   └── pages.py            # Page routes
│   ├── core/                   # Core application
│   │   ├── __init__.py
│   │   └── app_factory.py      # App factory
│   ├── models/                 # Pydantic models
│   │   ├── __init__.py
│   │   └── calculator.py
│   ├── services/               # Business logic
│   │   ├── __init__.py
│   │   └── calculator_service.py
│   ├── static/                 # Static assets
│   │   ├── css/
│   │   │   └── calculator.css
│   │   └── js/
│   │       └── calculator.js
│   └── templates/              # HTML templates
│       └── calculator.html
├── main.py                     # Application entry point
├── requirements.txt            # Dependencies
├── README.md                   # Documentation
└── .gitignore                  # Git ignore rules
```

## Installation

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Start the server

```bash
# Development mode with auto-reload
uvicorn main:app --reload

# Production mode
uvicorn main:app --host 0.0.0.0 --port 8000
```

Or:

```bash
python main.py
```

### Access the service

- **Web UI**: http://localhost:8000/
- **API Docs**: http://localhost:8000/docs
- **API Endpoint**: http://localhost:8000/api/calculate

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Calculator web page |
| `/api/calculate` | POST | Calculate expression |
| `/api/hello` | GET | Health check |
| `/docs` | GET | Auto-generated API documentation |

### Calculate API

**Request:**
```json
POST /api/calculate
Content-Type: application/json

{
    "expression": "2 + 3 * 4"
}
```

**Response:**
```json
{
    "result": "14",
    "success": true,
    "error": null
}
```

## Features

- Basic arithmetic: `+`, `-`, `*`, `/`
- Scientific functions: `sin`, `cos`, `tan`, `sqrt`, `log`, `ln`, `pow`, `factorial`
- Constants: `pi`, `e`
- Unit conversion: `deg`, `rad`
- Calculation history
- Keyboard support
- Responsive design

## Architecture

- **MVC Pattern**: Models, Views (Templates), Controllers (API routes)
- **Service Layer**: Business logic separated from routes
- **Factory Pattern**: Application creation via factory function
- **Static File Serving**: CSS/JS served from static directory
