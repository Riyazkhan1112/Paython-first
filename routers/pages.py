from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def index():
    """Main page"""
    return """
    <html>
        <head>
            <title>FastAPI Research App</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 50px; }
                h1 { color: #333; }
                a { display: block; margin: 10px 0; color: #0066cc; text-decoration: none; }
                a:hover { text-decoration: underline; }
            </style>
        </head>
        <body>
            <h1>🚀 Hello World - FastAPI Application</h1>
            <p>Welcome to the FastAPI Research Application</p>
            <h2>Available Endpoints:</h2>
            <a href="/api/health">✅ Health Check</a>
            <a href="/research">📚 Research Page</a>
            <a href="/chatbot">💬 Chatbot Page</a>
            <a href="/docs">📖 API Documentation (Swagger UI)</a>
            <a href="/redoc">📋 ReDoc Documentation</a>
        </body>
    </html>
    """

@router.get("/research", response_class=HTMLResponse)
async def research_page():
    """Research page"""
    return """
    <html>
        <head>
            <title>Research</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 50px; }
                h1 { color: #333; }
                button { padding: 10px 20px; background-color: #0066cc; color: white; border: none; border-radius: 4px; cursor: pointer; }
                button:hover { background-color: #0052a3; }
                #result { margin-top: 20px; padding: 10px; background-color: #f0f0f0; border-radius: 4px; min-height: 100px; }
            </style>
        </head>
        <body>
            <h1>Research Tool</h1>
            <input type="text" id="topic" placeholder="Enter topic to research" style="width: 300px; padding: 8px; margin-right: 10px;">
            <button onclick="research()">Research</button>
            <div id="result"></div>
            <script>
                async function research() {
                    const topic = document.getElementById('topic').value;
                    const response = await fetch('/api/research', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ topic: topic })
                    });
                    const data = await response.json();
                    document.getElementById('result').innerHTML = '<pre>' + JSON.stringify(data, null, 2) + '</pre>';
                }
            </script>
        </body>
    </html>
    """

@router.get("/chatbot", response_class=HTMLResponse)
async def chatbot():
    """Chatbot page"""
    return """
    <html>
        <head>
            <title>Chatbot</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 50px; }
                h1 { color: #333; }
                #chatbox { width: 400px; height: 300px; border: 1px solid #ccc; padding: 10px; overflow-y: auto; margin-bottom: 10px; background-color: #f9f9f9; border-radius: 4px; }
                input { width: 350px; padding: 8px; }
                button { padding: 8px 15px; background-color: #0066cc; color: white; border: none; border-radius: 4px; cursor: pointer; }
                button:hover { background-color: #0052a3; }
            </style>
        </head>
        <body>
            <h1>Chatbot</h1>
            <div id="chatbox"></div>
            <input type="text" id="message" placeholder="Type your message..." onkeypress="if(event.key==='Enter') sendMessage()">
            <button onclick="sendMessage()">Send</button>
            <script>
                function sendMessage() {
                    const message = document.getElementById('message').value;
                    if (message.trim()) {
                        document.getElementById('chatbox').innerHTML += '<p><strong>You:</strong> ' + message + '</p>';
                        document.getElementById('message').value = '';
                    }
                }
            </script>
        </body>
    </html>
    """
