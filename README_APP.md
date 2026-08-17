# AI Tools Hub - Research & Chatbot

A modern, full-featured application with AI-powered research and chatbot capabilities built with Flask and Google's Gemini API.

## ✨ Features

### 🔍 Research Hub
- Enter any topic and get AI-powered research in ~100 words
- Beautiful, responsive single-page interface
- Search history with quick access to previous queries
- Real-time loading indicators

### 💬 AI Chatbot
- Full conversation history with persistent storage
- Multiple concurrent conversations
- Remember all previous messages
- View and resume past conversations
- Beautiful modern chat UI with timestamps

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Up Environment Variables

Create a `.env` file in the project root:

```
GOOGLE_GEMINI_API_KEY=your_api_key_here
```

Get your API key from: https://ai.google.dev/

### 3. Run the Application

```bash
python app.py
```

The application will be available at: **http://localhost:5000**

## Project Structure

```
.
├── app.py                 # Flask backend server
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables (create this)
├── chat_history.db       # Chat history database (auto-created)
└── templates/
    ├── index.html        # Home page with tool selection
    ├── research.html     # Research tool interface
    └── chatbot.html      # Chatbot interface
```

## How to Use

### Research Hub
1. Click "Start Researching" from the home page
2. Enter a research topic
3. Wait for the AI to generate research findings
4. Click any history item to search again

### AI Chatbot
1. Click "Start Chatting" from the home page
2. Click "+ New Chat" to start a conversation
3. Type your message and press Enter or click the send button
4. View your conversation history in the sidebar
5. Click any previous conversation to resume it
6. All messages are saved automatically

## Technology Stack

- **Backend**: Flask 3.0+ (Python web framework)
- **Database**: SQLite (for chat history)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **AI**: Google Gemini 3.6 Flash API
- **Storage**: Browser LocalStorage + SQLite

## API Endpoints

### Research
- `POST /api/research` - Generate research on a topic

### Chatbot
- `POST /api/chat/new` - Create a new conversation
- `POST /api/chat/send` - Send a message
- `GET /api/chat/history/<id>` - Get chat history
- `GET /api/chat/conversations` - Get all conversations

## Browser Support

- Chrome/Edge 90+
- Firefox 88+
- Safari 14+

## License

MIT
