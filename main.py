from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Hello World Service")

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello World</title>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            }
            h1 {
                color: white;
                font-size: 3rem;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            }
        </style>
    </head>
    <body>
        <h1>Hello World 🤖</h1>
    </body>
    </html>
    """

@app.get("/api/hello")
async def api_hello():
    return {"message": "Hello World", "service": "OpenClaw FastAPI"}
