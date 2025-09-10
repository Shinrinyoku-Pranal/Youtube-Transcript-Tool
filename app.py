# app.py
from flask import Flask, request, jsonify
from transcribe import download_audio, transcribe_audio
import os

app = Flask(__name__)

@app.route("/transcribe", methods=["GET"])
def transcribe():
    url = request.args.get("url")
    if not url:
        return jsonify({"error": "Missing URL"}), 400

    try:
        audio_file = download_audio(url)
        text = transcribe_audio(audio_file)
        os.remove(audio_file)  # cleanup
        return jsonify({"transcript": text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
