from flask import Flask, render_template, request, jsonify
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
# flask in framework 
app = Flask(__name__)

api_key = os.getenv("GOOGLE_GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/research')
def research_page():
    return render_template('research.html')

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/api/research', methods=['POST'])
def research():
    try:
        data = request.json
        topic = data.get('topic', '')
        
        if not topic:
            return jsonify({'error': 'Topic is required'}), 400
        
        prompt = f"""
Do deep research on the following topic:

{topic}

Return the research in approximately 100 words.
"""
        
        interaction = client.interactions.create(
            model="gemini-3.6-flash", 
            input=prompt
        )
        
        return jsonify({
            'success': True,
            'topic': topic,
            'result': interaction.output_text
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/chat/send', methods=['POST'])
def send_message():
    try:
        data = request.json
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'Message is required'}), 400
        
        # Get AI response
        interaction = client.interactions.create(
            model="gemini-3.6-flash", 
            input=user_message
        )
        bot_response = interaction.output_text
        
        return jsonify({
            'success': True,
            'bot_response': bot_response
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)



