from flask import Flask, request, jsonify
from utils.pdf_parser import extract_text_from_pdf
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Resume Analyzer Backend Running 🚀"


@app.route("/upload", methods=["POST"])
def upload_resume():
    if "resume" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["resume"]

    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    file_path = "temp_resume.pdf"
    file.save(file_path)

    extracted_text = extract_text_from_pdf(file_path)

    os.remove(file_path)

    return jsonify({
        "extracted_text_preview": extracted_text[:500]
    })


if __name__ == "__main__":
    app.run(debug=True)