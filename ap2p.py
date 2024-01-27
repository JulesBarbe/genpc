from flask import Flask, request, jsonify, render_template
import chatbot
import knowledge

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    message = request.json.get('message')
    response = chatbot.get_response(message)
    return jsonify({'response': response})

@app.route('/upload-text', methods=['POST'])
def upload_text():
    text_type = request.json.get('type')  # 'global' or 'local'
    text_content = request.json.get('text')
    knowledge.process_text(text_type, text_content)
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)