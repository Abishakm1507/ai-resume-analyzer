import re
import spacy

# Load spaCy model (small English model)
nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    """
    Cleans and preprocesses text:
    - Lowercase
    - Remove special characters
    - Remove extra spaces
    """
    text = text.lower()
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()

    return text


def preprocess_with_spacy(text):
    """
    Lemmatizes and removes stopwords using spaCy.
    """
    doc = nlp(text)
    processed_tokens = [
        token.lemma_ for token in doc
        if not token.is_stop and not token.is_punct
    ]

    return " ".join(processed_tokens)