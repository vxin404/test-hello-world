# Hello World - FastAPI Web Service

A simple FastAPI web service created by OpenClaw.

## Features

- FastAPI web framework
- Beautiful gradient background
- REST API endpoint
- Python 3.10+

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Start the server

```bash
uvicorn main:app --reload
```

Or:

```bash
python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

### Access the service

- Web UI: http://localhost:8000/
- API: http://localhost:8000/api/hello
- Docs: http://localhost:8000/docs

## Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | HTML Hello World page |
| `/api/hello` | GET | JSON API response |
| `/docs` | GET | Auto-generated API documentation |

## Project Structure

```
.
├── main.py           # FastAPI application
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation
```
