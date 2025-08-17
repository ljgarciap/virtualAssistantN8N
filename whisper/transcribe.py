from flask import Flask, request, jsonify
from faster_whisper import WhisperModel
import tempfile
import os

ALLOWED_EXTENSIONS = {'mp3', 'ogg', 'wav', 'm4a'}

app = Flask(__name__)
model = WhisperModel(os.getenv('WHISPER_MODEL', 'small'), device='cpu')

@app.route('/asr', methods=['POST'])
def transcribe():
    if 'file' not in request.files:
        return jsonify({"error": "No audio file"}), 400
        
    file = request.files['file']
    if file.filename.split('.')[-1].lower() not in ALLOWED_EXTENSIONS:
        return jsonify({"error": "Unsupported file type"}), 400
        
    with tempfile.NamedTemporaryFile(suffix='.ogg') as temp:
        file.save(temp.name)
        segments, _ = model.transcribe(temp.name, beam_size=5)
        text = " ".join(segment.text for segment in segments)
        return jsonify({"text": text.strip()})
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)