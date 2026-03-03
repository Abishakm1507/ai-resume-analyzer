from flask import Flask, request, jsonify
from utils.pdf_parser import extract_text_from_pdf
from utils.text_cleaner import clean_text, preprocess_with_spacy
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

    try:
        # Extract text from PDF
        extracted_text = extract_text_from_pdf(file_path)

        # Clean and process text
        cleaned_text = clean_text(extracted_text)
        processed_text = preprocess_with_spacy(cleaned_text)

        return jsonify({
            "extracted_preview": extracted_text[:300],
            "cleaned_preview": cleaned_text[:300],
            "processed_preview": processed_text[:300]
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if os.path.exists(file_path):
            os.remove(file_path)


if __name__ == "__main__":
    app.run(debug=True)